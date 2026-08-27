# MineSkynet 프로젝트 작업 보고 로그

> 문서 역할: 구현 과정에서 이미 보고한 내용과 당시의 완료·미완료 판단을 시간순으로 누적한다. 과거 보고는 후속 결과로 덮어쓰거나 삭제하지 않고, 새 검증 결과는 별도 보고 항목으로 추가한다. 목표와 다음 순서는 마일스톤에서 관리하고, 교수님께 제시할 내용은 `labmeeting_temp.md`에서 선별·편집한다. 각 단위 테스크당 보고 템플릿/예시는 아래와 같다. 불렛포인트(-)/번호 목록(1))/체크포인트([X])/표(|---|---|---|) 등은 이해를 돕기 위해 적절히 사용한다. 반드시 /home/pluto2479/Documents/MineSkynet/research/AGENTS.md 의 원칙을 준수하라.

```markdown
# MineSkynet 프로젝트 작업 보고 로그

## YYYY-MM-DD — 단위 테스크 제목 1

...

### n. 하위 테스크 이름

...

#### n.m. 하위 테스크의 세부사항 (논리상/분량상 구분할 필요가 있을경우)

...

## YYYY-MM-DD — 단위 테스크 제목 2

...

```

## 2026-08-19~20 — Odyssey 환경·의존성 진단과 현대화 범위 확정

작성일: 2026-08-19~20  
대상 코드: 공개 Odyssey와 당시 `experiment/mvp-core` 진단 환경

### 1. 논문상 기능과 진단 목적

Odyssey는 Minecraft environment에서 open-world skill library, semantic skill retrieval과 planner–actor–critic을 연결한다. 당시 가장 먼저 해결해야 할 문제는 model 성능이 아니라 Minecraft server → Mineflayer → JavaScript skill → state-based verification으로 이어지는 실행 고리를 안정화하는 것이었다.

원본 공개 코드는 작은 행동을 실행할 때에도 planner, critic, embedding model, Chroma, launcher와 model provider를 함께 초기화했다. 이 결합 때문에 오류가 어느 논문 기능에서 발생했는지 구분하기 어렵고, 사용하지 않는 legacy dependency까지 모든 환경에 설치해야 했다.

문제를 분리하기 위해 E0~E4 gate를 임시 진단 도구로 사용했다. 이 gate는 결함 격리 과정의 역사적 이름이며, 이후 MineSkynet 연구 개발 순서나 최종 연구 기여로 사용하지 않는다.

### 2. 진단에서 확정한 원칙

#### 2.1 논문 기능과 실행환경의 분리

Planner–actor–critic, semantic retrieval과 skill library는 보존해야 할 Odyssey의 논문 기능이다. 반면 Multiplayer Server Pause bundle, launcher와 특정 model provider SDK는 특정 실행 방식에 필요한 dependency이므로 profile로 격리할 수 있다.

따라서 기본 profile에서 비활성화하는 것과 연구 시스템에서 기능을 제거하는 것을 구분한다.

#### 2.2 현대화의 연구 범위 제한

Odyssey 현대화의 목적은 legacy보다 빠르거나 우수함을 증명하는 것이 아니라, 구형 dependency issue로부터 안전한 MineSkynet 실험 기반을 만드는 것이다. `master`는 논문 기능과 공개 구현을 확인하는 source reference로 사용하며 legacy runtime의 성공률·latency 재측정은 완료 조건으로 삼지 않는다.

#### 2.3 신뢰받는 외부 구현의 보존

Sentence Transformer, Chroma와 LangChain은 semantic retrieval의 서로 다른 기능을 담당한다. 구형 API와 지원 조합은 갱신할 수 있지만, 이들을 근거 없이 자체 구현으로 교체하지 않는다. 변경 전후에 동일 corpus의 index 생성·재로드와 candidate retrieval contract를 먼저 보존한다.

#### 2.4 Model 성공과 embodied agent 성공의 구분

Minecraft 질문에 답하거나 training loss가 감소하는 것은 Actor가 올바른 skill을 선택해 environment state를 바꿨다는 증거가 아니다. Model 평가는 candidate-valid selection과 실제 Minecraft state delta까지 연결해야 한다.

### 3. 교수 피드백과 현재 해석

| 과거 피드백 | 현대화에 남긴 원칙 |
|---|---|
| 환경 설정이 최우선 | model·분산 연구 전에 반복 가능한 executor와 state verification을 확보한다. |
| 최소 dependency만 유지 | 기능을 삭제하지 않고 executor, retrieval, model, launcher, combat와 training profile을 분리한다. |
| 작은 model의 성능이 부족할 수 있음 | local model은 자유 계획·code generation보다 bounded skill selector부터 평가한다. |
| LoRA의 의미가 약하면 중단 | zero-shot/base model과 동일 task에서 비교하고 online 성공 개선이 없으면 학습을 연구 핵심에서 제외한다. |
| 새 기억이 기존 능력을 훼손할 수 있음 | 기본 MineSkynet Actor는 read-only registry를 사용하고 능동 skill lifecycle은 별도 Voyager/Full profile에서 검증한다. |
| 복잡한 문제를 더 복잡하게 만들지 말 것 | 한 고리씩 격리하되 component smoke를 전체 시스템 완료로 표기하지 않는다. |

### 4. E0 실행 계층에서 먼저 확인한 결과

Model 없이도 기존 Odyssey skill이 modernized Mineflayer 환경에서 반복 실행되고, failure 뒤 bridge가 다시 요청을 받을 수 있는지 확인했다.

- Minecraft `1.19.4`, Java `17`, Node `20.13.1` 조합 고정
- Mineflayer `4.25.0`과 관련 Prismarine dependency를 lockfile에 고정
- `/pause` 없는 mod-free server에서 raw 원목 채집과 작업대 제작을 각각 10/10 통과
- chat message가 아니라 inventory delta로 success 판정
- 잘못된 연결, 연속 reset과 의도적 skill error 뒤 bridge recovery 확인
- 실행 계층 결과를 commit `a157205`와 tag `odyssey-modernized-executor-1.19.4`로 고정

이 결과는 Minecraft execution layer의 범위이며 Odyssey 전체 논문 환경 재현을 뜻하지 않는다. 환경 snapshot과 반복 결과는 바로 다음 E0 증거 보고에 상세히 기록한다.

### 5. 실행 계층에서 분리·해결한 결합

| 문제 | 연구자가 이해할 한 줄 의미 | 처리 |
|---|---|---|
| Multiplayer Server Pause bundle | model 응답을 기다리는 동안 world를 멈추는 legacy 장치이며 raw skill 실행에는 필요하지 않음 | modernized executor 기본 경로에서 제외하고 Python legacy adapter에만 남김 |
| global bot lifecycle | 이전 bot의 늦은 종료가 새 bot까지 종료해 서로 다른 request의 상태가 섞임 | request-local bot과 identity check 적용 |
| non-finite motion | chunk 준비 전 physics가 잘못된 position packet을 보낼 수 있음 | chunk readiness와 finite-state guard 적용 |
| offline operator UUID | 새 world에서 bot이 reset command 권한을 얻지 못함 | 재현 가능한 offline UUID profile 고정 |
| mutable Node dependency tree | 설치 시점마다 protocol·physics dependency 조합이 달라질 수 있음 | exact package-lock과 health/version response 고정 |

### 6. E0 이후 다시 연결할 논문 기능

다음 기능은 E0에서 제거한 것이 아니라 modernized Odyssey에 다시 연결해야 할 범위로 남겼다.

- 40 primitive + 183 compositional skill corpus
- Sentence Transformer 기반 description/query embedding
- top-5 기본·top-10 별도 profile의 semantic retrieval
- MineMA Actor의 exact candidate selection
- recursive prerequisite execution
- planner–actor–critic feedback과 replanning
- 논문 benchmark의 task·prompt·success condition

Voyager의 curriculum, code generation/repair와 dynamic skill commit도 삭제하지 않는다. 공개 Odyssey의 fixed-library baseline과 분리해 `voyager-lifelong`과 `odyssey-full` profile에서 보존한다.

### 7. 당시 상태와 해석

E0~E4 gate는 dependency 결함을 격리하는 데 유용했지만, 각 gate의 최소 통과를 연구 목표로 확대해서는 안 된다고 판단했다. 이후에는 “원본 논문 기능을 재현하되 불안정하거나 비효율적인 dependency 고리를 제거·대체·업데이트한다”는 방향으로 마일스톤을 재편했다.

### 8. 근거 파일

- [원본 환경·의존성 진단 문서](MVP_report.md)
- [E0 원시 증거](E0_test_evidence_2026-08-20.md)
- [현대화 마일스톤](milestone_goal/modernization_milestone.md)
- [논문–코드–dependency 대응표](paper_code_dependency_map.md)

## 2026-08-20 — E0 Minecraft execution layer 검사 증거

작성일: 2026-08-20  
검사 profile: `e0-executor` 후보 환경

### 1. 논문상 기능과 증거 범위

이 검사는 model과 Planner를 제외하고, Actor가 선택할 JavaScript skill을 Mineflayer가 실제 Minecraft state change로 실행할 수 있는지 확인했다. 구체적으로 raw Odyssey skill의 반복 실행, inventory delta 기반 success 판정과 failure 이후 bridge recovery를 검증했다.

이는 Odyssey의 Minecraft execution layer에 대한 증거이며 semantic retrieval, MineMA Actor와 planner–actor–critic 전체 재현을 의미하지 않는다. 원시 world와 cache는 Git 밖의 `Odyssey/runtime/`에 유지했다.

### 2. 환경 snapshot

- Git 기준 commit: `80a42fcbd2b5da53ecf7e58f1036981e428c9590` (`origin/experiment/mvp-core`); 검사 시점에는 E0 관련 uncommitted change가 존재
- Docker image: `itzg/minecraft-server:java17`
- image ID: `sha256:5b3e96bcd7dace8ab7be89c245dc9ba0b1573fdef2f01d3e101ac40e7843fa70`
- Minecraft `1.19.4`, Fabric Loader `0.15.11`, Java `17.0.15+6`
- world seed: `7634567288700934061`
- Node `20.13.1`, npm `10.5.2`
- offline-mode bot operator UUID: `67128b5b-2e6b-3ad1-baa0-1b937b03e5c5` (`OfflinePlayer:bot`)
- operator profile: `Odyssey/server-profile/e0/ops.json`
- `package-lock.json` SHA-256: `5555e896e0c5d19c635965bc9338b0cd60a248092bc9c8ff65a6c678943a6b7c`

직접 Node dependency는 다음 조합으로 고정했다.

| Dependency | Version |
|---|---:|
| mineflayer | 4.25.0 |
| minecraft-data | 3.83.0 |
| mineflayer-pathfinder | 2.4.2 |
| mineflayer-tool | 1.2.0 |
| local mineflayer-collectblock | 1.4.1 |
| express | 4.18.2 |
| vec3 | 0.1.8 |
| typescript | 4.9.5 |
| @types/node | 18.19.130 |
| prismarine-entity | 2.4.0 |
| prismarine-item | 1.15.0 |

`npm ci` 감사에서는 16 vulnerabilities(3 low, 6 moderate, 7 high)가 보고됐다. 호환성이 검증된 묶음을 임의 변경하지 않기 위해 `npm audit fix`는 실행하지 않고 warning과 영향 범위를 후속 관리 대상으로 남겼다.

#### 2.1 기존 optional mod bundle snapshot

| JAR | Version | SHA-256 |
|---|---:|---|
| Multiplayer Server Pause | 1.3.1 | `fe6fe7e5c398415578f2be355de4bcd74ed5f11ebb5929d1aa91381fa8074d24` |
| CompleteConfig | 2.3.1 | `f7d5c7c82df363305b726f6fad651a68dad8404322d4b7a0f46d948882affcc2` |
| Fabric API | 0.87.2+1.19.4 | `a92650d48a9f672dc74e8b1eaefedb28dc83a13a80431215900181aa3a8675d8` |
| iChunUtil | 1.0.2 | `661b800c180d8f0dfca2467bebfbd57c41cd6b9e22cac989fb8979e3137d6475` |

이 JAR은 legacy pause fixture의 snapshot이며 mod-free raw executor의 필수 dependency로 판정하지 않았다.

### 3. Dependency와 interface 정적 검사

1. 활성 dependency tree에서 과거 `mineflayer-collectblock/node_modules`를 분리한 뒤 `npm ci`가 성공했다.
2. `npm run check`가 local collectblock TypeScript build, `node --check index.js`, `npm ls --depth=0`을 모두 통과했다. `npm ci` 뒤에도 하위 `mineflayer-collectblock/node_modules`는 생성되지 않았다.
3. `/health`와 `/version`은 pinned Minecraft `1.19.4`와 dependency version을 반환했다.

### 4. Minecraft runtime 반복 결과

#### 4.1 Connection과 finite state

Modded fixture에서 bot 연결과 finite position을 0·5·10·15·20·25·30초에 확인해 7/7 통과했다. Clean `npm ci` 직후에도 30초 연결, 원목 1회와 작업대 1회를 다시 실행해 모두 통과했다.

#### 4.2 Raw skill state delta

매회 hard reset과 empty inventory로 두 raw skill을 각각 10회 실행했다.

| Raw skill | 반복 | Before | After | State-based success | Error |
|---|---:|---|---|---|---|
| `mineWoodLog` | 10/10 | `{}` | `spruce_log: 1` | log delta `+1` | `onError: []` |
| `craftCraftingTable` | 10/10 | `{}` | `crafting_table: 1` | table delta `+1` | `onError: []` |

`Odyssey/scripts/e0_regression.py`로 기존 fixture에서 두 작업을 다시 실행한 최종 회귀도 총 20/20, 모든 목표 delta `+1`, 모든 `onError: []`로 통과했다.

#### 4.3 Mod-free executor

별도 임시 Fabric server는 같은 image ID, Minecraft version, Fabric Loader와 seed를 사용하되 외부 mod JAR를 넣지 않았다. Server log의 mod 목록은 Minecraft, Java, Fabric Loader와 내장 MixinExtras뿐이었다.

이 server에 `soft`로 접속해 finite position 30초, 원목 채집과 empty inventory의 작업대 제작을 각각 통과했다. 실행 경로는 `/health`, `/start`, `/step`만 호출하고 `/pause`를 호출하지 않았다. 따라서 raw E0 execution에는 Multiplayer Server Pause, iChunUtil, CompleteConfig와 Fabric API가 필요하지 않음을 확인했다.

### 5. Failure recovery와 bot lifecycle

`/start`가 request별 bot instance를 capture하도록 수정하고 pending start response와 old-bot disconnect를 분리했다. 다음 recovery fixture를 통과했다.

- 연속 hard `/start` 2회 뒤 새 bot 15초 생존
- 잘못된 port의 400 response 뒤 bridge 생존 및 정상 hard reset recovery
- 의도적인 `/step` JavaScript error 뒤 connection 유지
- request-local process exception listener 정리 뒤 다음 request 수신

새 offline-mode server에서는 `OPS=bot`이 online UUID를 기록해 hard reset timeout을 일으키는 문제를 확인했다. 올바른 offline UUID를 담은 `OPS_FILE`을 Compose에 고정한 뒤 외부 mod 없는 새 server의 첫 번째·두 번째 hard reset, 15초 finite position, 원목과 작업대를 모두 통과했다.

### 6. Latency 관찰값

| Raw skill | 평균 action latency | P95 action latency |
|---|---:|---:|
| `mineWoodLog` | 10,829.307 ms | 20,384.104 ms |
| `craftCraftingTable` | 13,172.842 ms | 23,990.514 ms |

Latency는 modernized가 legacy보다 빠르다는 비교 증거가 아니라, 당시 반복 실행의 환경 관찰값으로만 보존한다.

### 7. 해결한 결함과 증거 위치

- old bot의 늦은 disconnect가 새 global bot을 종료하던 race를 request-local bot capture와 identity check로 해결했다.
- `/step` process-level exception listener가 request-local bot을 사용하고 response `finish`/`close`에서 정리되게 했다.
- 새 offline server의 hard reset timeout 원인을 잘못된 online OP UUID로 식별하고 Compose가 traceable offline UUID `OPS_FILE`을 사용하게 했다.
- 최종 raw 결과는 `Odyssey/odyssey/env/results/e0/20260820T021925+0900/`에 저장했다. `environment.json`, 실행별 JSON 20개, `summary.json`, `minecraft_latest.log`를 포함하며 local runtime 결과라 Git에서 제외된다.
- 검사 당시에는 success commit/tag를 만들지 않았고, 이후 변경을 `a157205` (`E0 finished`)에 commit한 뒤 `odyssey-modernized-executor-1.19.4` annotated tag로 local·remote에 고정했다.

### 8. 당시 상태와 해석

Minecraft execution layer는 clean install, raw action success와 대표 failure recovery를 반복 통과했다. 이 결과로 model·retrieval과 분리된 mod-free executor baseline을 확보했다. 다만 E0는 Odyssey 전체 재현이 아니며, semantic retrieval, Actor selection, recursive prerequisite와 planner–actor–critic은 별도 component 검증으로 남았다.

### 9. 근거 파일

- [원본 E0 검사 증거](E0_test_evidence_2026-08-20.md)
- [E0 regression script](../../Odyssey/scripts/e0_regression.py)
- [E0 server profile](../../Odyssey/server-profile/e0/ops.json)
- [환경·dependency 진단 기록](MVP_report.md)
- [현대화 마일스톤](milestone_goal/modernization_milestone.md)

---

## 2026-08-27 — Primitive runtime 결함 정리

작성일: 2026-08-27
대상 브랜치: `experiment/odyssey-modernized`

### 1. 논문상 기능과 작업 범위

Odyssey의 open-world skill library는 40개 primitive skills와 183개 compositional skills로 구성된다. Primitive skills는 Mineflayer JavaScript API 위에서 parameterized input을 받는 foundational interfaces이며, compositional skill이 더 복잡한 task와 prerequisite를 재귀적으로 수행할 때 사용하는 저수준 실행 단위다. 논문은 시각 입력이 없는 환경에서 precise positioning과 orientation을 담당하는 spatial skills가 특히 중요하다고 설명한다.

이번 작업은 Odyssey-added spatial primitive 가운데 `goto`와 `getAnimal`을 대상으로 했다.

- `goto`: 지정 좌표의 허용 오차 안으로 bot을 이동시킨다.
- `getAnimal`: 동물 종류에 맞는 먹이를 들고 해당 동물을 지정 좌표까지 유인한다.

목적은 두 함수를 새 행동으로 대체하는 것이 아니라, compositional skill이 호출했을 때 조용히 성공하거나 무한 대기하지 않고 논문상 primitive contract를 실제 Minecraft state로 확인할 수 있게 하는 것이었다.

### 2. 확인한 결함

| Primitive | 공개 코드 결함 | 논문 기능에 미치는 영향 |
|---|---|---|
| `goto` | `bot.entity.positon` 오타 | 현재 위치를 읽을 수 없어 이동 contract 실행 불가 |
| `goto` | x·y·z 세 축이 모두 오차를 벗어날 때만 반복하는 조건 | 한 축만 멀어도 성공으로 종료할 수 있음 |
| `goto` | timeout과 최종 위치 검증 부재 | pathfinder 정지·부분 이동을 성공과 구분하기 어려움 |
| `getAnimal` | `type = "sheep"` 형태의 대입 조건과 항상 참인 `|| "cow"` | 입력 animal type과 무관하게 잘못된 먹이 분기로 진입 |
| `getAnimal` | `chichken` 오타와 입력·먹이 검증 부재 | chicken branch와 failure 원인을 신뢰할 수 없음 |
| `getAnimal` | 동물을 찾은 뒤 target으로 bot만 이동 | 동물이 실제 target까지 따라왔는지 확인하지 않음 |

### 3. 수정 내용

`goto`는 finite coordinate와 positive timeout을 검사하고, Mineflayer pathfinder의 `GoalNear`를 사용해 반경 2블록 안으로 이동하게 했다. 이동 전·후 위치를 검사하고 timeout이나 pathfinder failure가 발생하면 goal을 취소한 뒤 `[goto]` 오류로 반환한다.

`GoalNear`는 실수 좌표를 Minecraft block-grid로 내림해 반경을 계산한다. 따라서 초기 구현처럼 실수 target과 bot 중심 사이의 Euclidean distance를 후조건으로 사용하면 pathfinder는 성공했는데 primitive가 실패하는 불일치가 생긴다. 최종 contract는 `GoalNear`와 동일한 block-grid distance 2 이하로 통일했다.

`getAnimal`은 animal–food mapping을 다음과 같이 명시했다.

- sheep·cow → wheat
- chicken → wheat seeds
- pig → carrot

지원하지 않는 animal type, 먹이 부재, 32블록 안에서 animal을 찾지 못한 경우를 명시적 오류로 분리했다. 동물을 찾으면 먼저 접근해 바라보고, 먹이를 든 상태에서 `goto`로 target까지 이동한 뒤 animal이 target 반경 4블록 안에 들어왔는지 최대 100 tick 동안 확인한다.

### 4. Offline fixture 결과

mock bot과 pathfinder를 사용한 state-based fixture 14개가 모두 통과했다.

- `goto` 6개: 이미 반경 안인 경우, 정상 GoalNear 이동, 실제 실패 좌표의 block-grid 회귀, 비정상 좌표, timeout·goal 취소, target 미도달 실패
- `getAnimal` 8개: 네 animal–food mapping, 지원하지 않는 type, 먹이 부재, animal 탐색 실패, target까지 따라오지 않는 경우

```text
14/14 primitive offline fixtures passed
```

### 5. Minecraft online fixture 결과

`getAnimal(cow)`은 bot 근처에 cow 한 마리와 wheat를 준비하고 현재 위치에서 x축 8블록 떨어진 target까지 유인했다. 최종 bot–target 거리는 약 `0.842`, cow–bot 거리는 약 `2.223`이었고 `onError` 없이 통과했다.

`goto` 첫 실행은 6블록 이동 뒤 실수 target 거리 `2.154`에서 primitive 오류를 반환했다. 그러나 이는 pathfinder 이동 실패가 아니라 `GoalNear`의 block-grid 반경과 실수 좌표 후조건의 불일치였다. 실제 관측 좌표를 offline regression fixture에 추가하고 contract를 통일한 뒤 다시 실행했다.

재실행에서는 다음 결과로 통과했다.

```text
bot_distance_to_target: 1.3954
bot_block_distance_to_target: 1.4142
onError: []
PASS: goto state-based online fixture
```

### 6. 당시 상태와 해석

`goto`와 `getAnimal`은 offline 14/14와 실제 Minecraft online fixture를 통과했다. 이는 두 spatial primitive의 contract를 확인한 component 결과이며 primitive 40개 전체 또는 Odyssey end-to-end 재현 완료를 뜻하지 않는다. 나머지 primitive contract와 Voyager-inherited interface fixture는 후속 검증으로 남겼다.

### 7. 근거 파일

- [Primitive 40 working manifest](../manifest/odyssey_primitive_40.json)
- [Offline primitive fixture](../../Odyssey/scripts/primitive_runtime_offline.js)
- [Online primitive fixture](../../Odyssey/scripts/primitive_runtime_online.py)
- [실행 절차](../README.md#37-primitive-runtime-online-fixture)
- [현대화 마일스톤](milestone_goal/modernization_milestone.md)

---

## 2026-08-27 — Semantic encoder 조건 고정

작성일: 2026-08-27  
대상 브랜치: `experiment/odyssey-modernized`

### 1. 논문상 기능과 이번 작업의 목적

Odyssey의 LLM Actor는 Planner가 생성한 text-based subgoal을 바로 실행 코드로 바꾸지 않는다. 먼저 subgoal을 **query context**로 encoding하고, open-world skill library에 저장된 **skill description**과의 vector similarity를 계산해 **semantic closeness**가 높은 skill을 retrieval한다. Actor는 이렇게 제시된 top-5 relevant skills 중 subgoal 실행에 가장 적절한 code를 선택한다.

Skill library 쪽에서는 각 skill의 complete program code를 바탕으로 자연어 description을 생성하고, Sentence Transformer가 이 description을 vector representation으로 변환한다. 따라서 semantic encoder는 다음 두 입력을 같은 의미 공간에 배치하는 논문 기능이다.

- Planner가 생성한 자연어 subgoal: retrieval의 query context
- 183개 compositional skill의 자연어 description: 검색 대상 corpus

이번 작업의 목적은 이 논문 기능을 제거하거나 자체 구현으로 대체하는 것이 아니라, 공개 Odyssey 코드가 사용한 Sentence Transformer의 checkpoint와 text-to-vector 변환 조건을 명시적으로 고정해 dependency 변경 뒤에도 같은 semantic skill retrieval을 재현할 수 있게 하는 것이다.

### 2. 감사에서 확인한 재현 위험

논문은 Sentence Transformer를 통한 query context encoding과 skill similarity retrieval을 설명하지만 정확한 checkpoint 이름은 명시하지 않는다. 반면 공개 코드의 `conf/config.json`은 `paraphrase-multilingual-MiniLM-L12-v2`를 지정한다. 따라서 이 모델은 **논문이 명시한 checkpoint가 아니라 공개 코드가 선택한 modernized 재현 기준**으로 구분해야 한다.

또한 기존 구현은 `HuggingFaceEmbeddings(model_name=...)`에 model 경로만 전달했다. 이 상태에서는 normalization, precision과 batch 설정이 설치된 Sentence Transformers·LangChain 버전의 기본값에 의존한다. 동일 model 파일을 사용하더라도 dependency 변화가 vector scale이나 retrieval score에 영향을 줄 가능성이 있었다.

마지막으로 `SkillManager`의 기본 retrieval 수는 5였지만 상위 `Odyssey` 생성자의 기본값은 10으로 남아 있어, 논문 본문의 top-5 skill selection 및 현재 profile 정책과 실제 runtime 기본값이 일치하지 않았다.

### 3. 수행 내용

#### 3.1 공개 코드 checkpoint의 provenance 고정

modernized baseline의 model ID를 `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`로 기록하고, 로컬 Hugging Face download metadata에서 revision을 다음과 같이 확인했다.

```text
e8f8c211226b894fcb81acc59f3b34ba3efd5f42
```

로컬 model directory에는 PyTorch, ONNX, OpenVINO와 TensorFlow용 중복 artifact가 함께 존재한다. 현재 Odyssey의 Sentence Transformer 실행에는 PyTorch safetensors 경로를 사용하므로, `model.safetensors`와 tokenizer·pooling·model config 등 runtime에 필요한 11개 파일만 canonical artifact로 정하고 각각의 크기와 SHA-256을 manifest에 기록했다. 사용하지 않는 변환·양자화 artifact는 재현 checksum 범위에서 제외했다.

#### 3.2 Query context와 skill description의 encoding 조건 고정

checkpoint 내부 설정과 현재 adapter 동작을 대조해 다음 text-to-vector contract를 고정했다.

| 항목 | 고정값 | 논문 기능상 의미 |
|---|---:|---|
| vector dimension | 384 | query context와 skill description을 비교하는 공통 vector representation |
| maximum sequence length | 128 tokens | 긴 text 입력이 잘리는 동일한 경계 |
| pooling | attention-mask-aware mean pooling | token representation을 하나의 sentence representation으로 결합 |
| case folding | 사용하지 않음 | 입력 대소문자를 임의로 변경하지 않음 |
| normalization | 사용하지 않음 | 기존 공개 adapter의 vector scale을 보존 |
| precision | float32 | canonical embedding 계산 정밀도 |
| batch size | 32 | corpus encoding의 기본 처리 단위 |
| adapter preprocessing | newline을 ASCII space로 치환 | query와 description에 동일한 text 전처리 적용 |

query와 document는 서로 다른 encoder를 사용하지 않는다. LangChain adapter의 `embed_query`가 document encoding 경로를 공유하도록 유지해, subgoal과 skill description이 동일한 model·pooling·normalization 조건에서 비교되게 했다.

#### 3.3 Skill retrieval과 Planner QA retrieval의 encoder 설정 통일

기존에는 `SkillManager`와 `PlannerAgent`가 각각 `HuggingFaceEmbeddings`를 직접 생성했다. 두 경로가 dependency update 과정에서 서로 다른 설정을 갖지 않도록 공통 factory인 `odyssey/retrieval_embedding.py`를 추가했다.

두 retrieval 경로는 이제 다음 값을 명시적으로 공유한다.

- `normalize_embeddings=False`
- `precision="float32"`
- `batch_size=32`
- progress output 비활성화

또한 `Odyssey` runtime의 기본 skill retrieval 수를 논문 본문과 결정된 profile에 맞춰 top-5로 수정했다. top-10은 제거하지 않고 autonomous exploration 등을 위한 별도 retrieval profile로 남겨, 다음 단계에서 동일 corpus와 distance metric을 사용한 회귀 fixture로 검증한다.

#### 3.4 재현 manifest와 fixture 작성

`odyssey_semantic_encoder.json`에 model provenance, canonical artifact checksum, transformation contract, 관찰된 dependency version과 top-k 정책을 기록했다.

`semantic_encoder_fixture.py`는 두 단계로 실행된다.

1. **Static contract fixture:** model inference 없이 revision, 11개 artifact checksum, vector dimension, maximum sequence length, pooling과 source의 명시적 설정을 검사한다.
2. **Runtime contract fixture:** CPU에서 고정된 한국어·영어 문장을 실제로 encoding해 `(3, 384)` shape, NaN/Inf 부재, 반복 실행 오차와 newline/space 전처리 동등성을 검사한다.

현재 static contract fixture는 모든 항목을 통과했다. 실제 embedding runtime fixture는 연구자 실행 전이므로 semantic encoder 전체를 완료로 표시하지 않았다.

### 4. 당시 상태와 해석

| 논문상의 단계 | 당시 확보한 근거 | 상태 |
|---|---|---|
| skill description을 vector representation으로 변환 | checkpoint·pooling·전처리·artifact checksum 고정 | 정적 검증 완료 |
| text-based subgoal을 query context로 encoding | skill description과 동일한 공통 encoder factory 적용 | 정적 검증 완료 |
| query context와 skill description의 similarity matching | distance metric과 실제 candidate 순위 미확정 | 다음 단계 |
| top-5 relevant skills 제시 | runtime 기본값을 top-5로 통일 | 정책·코드 반영 완료 |
| Actor가 적절한 code 선택 | MineMA Actor 연결 전 | 범위 밖·후속 단계 |

즉, 이 시점의 결과는 Odyssey의 semantic skill retrieval 전체 성공이 아니라, retrieval 입력을 생성하는 **semantic encoder 조건을 반복 가능한 상태로 고정한 것**이다. top-5/top-10 후보 결과, vector-store persist/reload와 Actor의 최종 skill selection은 별도 검증으로 남아 있었다.

### 5. 당시 다음 확인 작업

Minecraft server, Mineflayer bridge와 MineMA backend 없이 다음 명령을 연구자 실행 단계로 남겼다.

```bash
cd ~/Documents/MineSkynet
Odyssey/.venv/bin/python Odyssey/scripts/semantic_encoder_fixture.py --run-model --device cpu
```

당시 통과 기준은 세 입력의 384차원 vector 출력, finite 값, 반복 encoding 최대 절대 오차 `1e-6` 이하, newline/space 입력 동등성과 마지막 `PASS` 출력이었다. 이 실행 결과를 확보한 뒤 embedding checksum·vector norm과 현재 dependency 조합을 manifest에 기록하기로 했다.

### 6. 당시 근거 파일

- [Semantic encoder manifest](../manifest/odyssey_semantic_encoder.json)
- [Semantic encoder fixture](../../Odyssey/scripts/semantic_encoder_fixture.py)
- [공통 retrieval encoder 설정](../../Odyssey/odyssey/retrieval_embedding.py)
- [현대화 마일스톤](milestone_goal/modernization_milestone.md)
- [논문–코드–dependency 대응표](paper_code_dependency_map.md)

---

## 2026-08-27 — Semantic encoder runtime 및 top-5 retrieval 추가 보고

작성일: 2026-08-27  
대상 브랜치: `experiment/odyssey-modernized`

### 1. 추가 확인 목적

최초 보고에서 미실행으로 남긴 CPU encoder fixture를 수행하고, 고정한 checkpoint와 183개 skill description으로 논문의 query context encoding → similarity matching → top-5 relevant skills 흐름이 실제 동작하는지 확인했다.

### 2. Semantic encoder runtime 결과

CPU runtime fixture에서 세 입력이 `(3, 384)` float32 vector로 변환됐고, NaN/Inf가 없으며 반복 실행과 newline/space 입력의 최대 절대 오차가 모두 `0.0`임을 확인했다. 고정 입력 embedding의 SHA-256은 `4f5de76040931c0558f63c1e6083f6779c61f1611b81f9d456aa9b7263d32c6b`이다.

### 3. Semantic skill retrieval smoke test

기존 문서와 로그에는 query 원문, candidate 이름과 score가 함께 남은 실행 증거가 없었다. 따라서 고정한 encoder로 `skills.json`의 183개 skill description을 모두 Chroma에 indexing하고, 논문의 query context encoding → similarity matching → top-5 relevant skills 흐름을 직접 실행했다.

| Text-based subgoal/query context | 기대 skill | top-1 결과 | L2 score |
|---|---|---|---:|
| `Craft a wooden pickaxe.` | `craftWoodenPickaxe` | `craftWoodenPickaxe` | 16.1350 |
| `Mine diamond ore using an iron pickaxe.` | `mineDiamond` | `mineDiamond` | 11.6207 |
| `Breed two cows using wheat.` | `breedCow` | `breedCow` | 25.7432 |
| `밀을 사용해서 소 두 마리를 번식시킨다.` | `breedCow` | `breedCow` | 16.0217 |

183개 description이 모두 index에 들어갔고, 네 query 모두 기대 skill이 top-5에 포함됐을 뿐 아니라 rank 1로 반환됐다. 이 smoke set의 known-query recall@5는 `4/4 = 1.0`이다. 따라서 현재 고정 checkpoint와 corpus로 **실제 semantic skill retrieval이 가능하다**고 보고할 수 있다. 이는 네 개의 대표 query에 대한 기능 smoke 결과이며 전체 skill corpus의 일반적인 retrieval 정확도를 의미하지는 않는다.

표의 L2 score는 확률이나 정확도가 아니라 query vector와 description vector 사이의 거리이며, 같은 profile 안에서는 값이 작을수록 더 가까운 candidate다.

실행 중 다음 현대화 경고도 관찰했다.

- LangChain의 기존 `HuggingFaceEmbeddings` wrapper가 `langchain-huggingface`로 이전 예정이라는 deprecation 경고
- LangChain의 기존 Chroma wrapper가 `langchain-chroma`로 이전 예정이라는 deprecation 경고
- Chroma telemetry의 `capture()` signature 불일치 경고

세 경고는 이번 indexing과 candidate retrieval을 중단시키지 않았다. 그러나 구형 dependency issue로부터 안전한 실행환경을 만들기 위해 wrapper 지원 조합과 telemetry 설정은 후속 작업에서 정리해야 한다.

### 4. 현재 상태와 해석

| 논문상의 단계 | 현재 확보한 근거 | 상태 |
|---|---|---|
| skill description을 vector representation으로 변환 | 183개 description 전체 indexing | runtime 검증 완료 |
| text-based subgoal을 query context로 encoding | 영어 3개·한국어 1개 query 실제 encoding | runtime 검증 완료 |
| query context와 skill description의 similarity matching | L2 top-5 candidate와 score 기록 | smoke 검증 완료 |
| top-5 relevant skills 제시 | 기대 skill rank 1: 4/4, recall@5: 1.0 | smoke 검증 완료 |
| Actor가 적절한 code 선택 | MineMA Actor 연결 전 | 범위 밖·후속 단계 |

즉, semantic encoder 조건 고정을 넘어 183개 공개 skill corpus에서 top-5 semantic retrieval이 실제로 동작함을 확인했다. 다만 이것은 제한된 known-query smoke test이며, 별도 top-10 profile, index persist/reload 뒤 candidate 순서 유지와 Actor의 최종 skill selection은 검증하지 않았다.

### 5. 재현 명령과 남은 작업

Minecraft server, Mineflayer bridge와 MineMA backend 없이 다음 명령으로 encoder와 top-5 retrieval 결과를 각각 재현할 수 있다.

```bash
cd ~/Documents/MineSkynet
Odyssey/.venv/bin/python Odyssey/scripts/semantic_encoder_fixture.py --run-model --device cpu
Odyssey/.venv/bin/python Odyssey/scripts/semantic_retrieval_smoke.py
```

두 fixture는 2026-08-27 CPU 실행에서 통과했다. 다음에는 같은 corpus·encoder·metric에서 top-10을 별도 profile로 실행하고, 저장한 Chroma index를 다시 열어도 candidate 순서가 유지되는지 확인한다. LangChain embedding/Chroma wrapper의 deprecated API와 telemetry warning도 기능 회귀를 유지하면서 정리해야 한다.

### 6. 추가 보고 근거 파일

- [Semantic encoder manifest](../manifest/odyssey_semantic_encoder.json)
- [Semantic encoder fixture](../../Odyssey/scripts/semantic_encoder_fixture.py)
- [Semantic retrieval smoke fixture](../../Odyssey/scripts/semantic_retrieval_smoke.py)
- [Semantic retrieval 실행 로그](../log/semantic_retrieval_smoke_2026-08-27.json)
- [공통 retrieval encoder 설정](../../Odyssey/odyssey/retrieval_embedding.py)
- [현대화 마일스톤](milestone_goal/modernization_milestone.md)
- [논문–코드–dependency 대응표](paper_code_dependency_map.md)

---

## 2026-08-27 — Retrieval fixture 완성

작성일: 2026-08-27  
대상 브랜치: `experiment/odyssey-modernized`

### 1. 논문상 기능과 이번 작업의 목적

Odyssey는 Planner의 text-based subgoal을 query context로 encoding하고, open-world skill library의 description vector와 similarity matching해 relevant skills를 Actor에게 제시한다. 이번 작업은 이 semantic skill retrieval을 다음 두 실행 profile과 반복 가능한 vector-store contract로 고정하는 것이 목적이다.

- 기본 `top5`: 논문 본문의 Actor candidate selection 조건이자 연산 부담을 줄인 기본 profile
- 별도 `top10`: 부록과 autonomous exploration 조건을 보존하는 확장 profile

검증 대상은 자연어 subgoal → 183개 description index → 순서와 score를 가진 candidate 반환까지다. MineMA Actor의 최종 선택과 Minecraft skill 실행은 이번 fixture의 범위가 아니다.

### 2. 구현한 retrieval contract

공통 retrieval 설정에 `top5=5`, `top10=10` profile과 기본 profile `top5`를 명시했다. `SkillManager`와 상위 `Odyssey` 생성자는 이 기본값을 공유하며, Chroma collection의 distance metric은 `L2`로 고정했다.

Fixture는 임시 persist directory에서 183개 description의 index를 새로 만들고 검색한 뒤, 첫 프로세스를 종료한다. 이후 별도 프로세스가 같은 저장 index를 다시 열어 동일 query와 profile을 검색한다. 이 구조는 같은 in-memory object를 반복 호출한 결과가 아니라 실제 index 재로드 뒤의 결과를 비교한다.

### 3. 대표 자연어 subgoal 결과

영어 세 개와 한국어 한 개의 대표 query를 사용했다. fresh index와 reloaded index에서 결과가 같았으므로 아래에는 top-1과 fresh index의 score를 요약한다. 각 query의 top-10 전체 후보와 score는 실행 로그에 저장했다.

| Text-based subgoal/query context | 기대 skill | top-1 결과 | L2 score |
|---|---|---|---:|
| `Craft a wooden pickaxe.` | `craftWoodenPickaxe` | `craftWoodenPickaxe` | 16.1350 |
| `Mine diamond ore using an iron pickaxe.` | `mineDiamond` | `mineDiamond` | 11.6207 |
| `Breed two cows using wheat.` | `breedCow` | `breedCow` | 25.7432 |
| `밀을 사용해서 소 두 마리를 번식시킨다.` | `breedCow` | `breedCow` | 16.0217 |

L2 score는 확률이나 정확도가 아니라 query와 description vector 사이의 거리다. 같은 profile에서는 값이 작을수록 semantic closeness가 높다.

### 4. Profile과 index reload 결과

| 검사 | Fresh index | Reloaded index | 판정 |
|---|---:|---:|---|
| corpus/index 수 | 183 | 183 | 통과 |
| top-5 known-query recall@5 | 4/4 | 4/4 | 통과 |
| top-10 known-query recall@10 | 4/4 | 4/4 | 통과 |
| top-5가 top-10의 1~5위와 일치 | 4/4 | 4/4 | 통과 |
| fresh/reload candidate 순서 | 비교 기준 | 두 profile·네 query 전부 동일 | 통과 |
| fresh/reload 최대 score 차이 | 비교 기준 | `0.0` | 통과 |

따라서 고정한 encoder·183개 corpus·L2 조건에서 기본 top-5와 별도 top-10 retrieval이 모두 가능하며, index를 재생성하고 저장본을 다시 연 뒤에도 후보 순서와 score가 유지된다고 보고할 수 있다. 이는 네 known query에 대한 retrieval contract 회귀이며 전체 183개 skill의 일반적인 검색 정확도나 Actor 선택 성공률을 의미하지 않는다.

### 5. 관찰된 경고와 남은 작업

이번 경고는 현재 semantic retrieval 결과가 틀렸다는 뜻은 아니다. 다만 지금 사용한 library 연결부가 향후 update나 새 설치 환경에서 같은 기능을 계속 제공한다는 보장이 약하다는 신호이므로, 구형 dependency issue로부터 안전한 연구 기반을 만들기 위해 정리해야 한다.

| 용어·경고 | 간략한 의미 | 위험한 이유 |
|---|---|---|
| `wrapper` | Odyssey 코드가 Sentence Transformer나 Chroma의 내부 API를 직접 다루지 않도록 LangChain이 중간에서 공통 interface로 감싼 adapter다. | wrapper가 바뀌면 model과 DB 자체가 정상이어도 import 경로, 설정 전달 또는 반환 score 형식이 달라져 retrieval 고리가 끊길 수 있다. |
| `deprecation` | 현재는 동작하지만 해당 class·import 경로를 앞으로 제거할 예정이라는 유지보수 경고다. | 지금 무시해도 즉시 실패하지 않지만, 이후 LangChain upgrade에서 `HuggingFaceEmbeddings`나 `Chroma` class가 삭제되면 clean install 또는 실행이 중단될 수 있다. |
| `langchain-huggingface` | Hugging Face embedding wrapper를 LangChain 본체에서 분리해 관리하는 새 공식 package다. | 기존 wrapper와 model option·version 호환성이 완전히 같다고 가정하고 교체하면 vector scale이나 전처리가 달라져 candidate score·순위가 조용히 바뀔 수 있다. |
| `langchain-chroma` | Chroma vector DB 연결 wrapper를 별도 package로 옮긴 새 공식 package다. | Chroma client의 저장 방식, collection 설정이나 score 반환 계약이 달라지면 기존 index를 열지 못하거나 재로드 뒤 후보 순서가 바뀔 수 있다. |
| `telemetry` | Chroma가 client 시작이나 collection 추가 같은 사용 event를 수집·전송하려는 진단 기능이며 skill description이나 embedding 계산 자체는 아니다. | 연구 기능에는 불필요한 외부 동작이고, 실패 메시지가 반복되면 실제 DB 오류를 로그에서 가리거나 제한된 network 환경에서 불필요한 실패 원인이 될 수 있다. |
| `capture() signature` 불일치 | telemetry event를 보내는 쪽과 받는 함수가 기대하는 인자 개수가 다르다는 뜻으로, 관련 package version 조합이 맞지 않음을 보여준다. | 현재는 telemetry만 실패했지만 같은 dependency 조합의 다른 API에서도 호환성 문제가 잠복했을 가능성이 있으며, warning을 error로 처리하는 환경에서는 실행을 막을 수 있다. |
| `clean environment`와 `exact lock` | 기존 cache나 우연히 설치된 package 없이 새 환경을 만들고, 검증한 package의 정확한 version 조합만 다시 설치하는 절차다. | 현재 `.venv`에만 존재하는 간접 dependency 덕분에 우연히 통과한 경우 다른 PC나 재설치에서 재현되지 않는다. version을 고정하지 않으면 같은 명령도 설치 시점에 따라 다른 결과를 낼 수 있다. |

이번 실행에서는 위 경고가 index 생성·persist·reload와 검색을 중단시키지 않았고, fresh/reload 후보 순서와 score도 일치했다. 따라서 현재 retrieval fixture는 통과로 유지하되 dependency 안전성은 완료로 올리지 않는다.

다음 dependency 정비에서는 `langchain-huggingface`와 `langchain-chroma`의 지원 version 조합을 별도 환경에서 검토하고, encoder vector contract와 이번 retrieval fixture를 모두 통과한 조합만 lock한다. telemetry는 끄거나 호환되는 version으로 맞추되, 경고를 숨기는 것만으로 해결했다고 판정하지 않는다. 별도 clean environment의 exact lock 설치와 재실행은 아직 완료하지 않았다.

### 6. 재현 명령과 근거 파일

```bash
cd ~/Documents/MineSkynet
Odyssey/.venv/bin/python Odyssey/scripts/semantic_retrieval_fixture.py
```

- [Retrieval profile fixture](../../Odyssey/scripts/semantic_retrieval_fixture.py)
- [Top-5·top-10 후보와 reload 실행 로그](../log/semantic_retrieval_profiles_2026-08-27.json)
- [Semantic encoder·retrieval manifest](../manifest/odyssey_semantic_encoder.json)
- [공통 retrieval profile 설정](../../Odyssey/odyssey/retrieval_embedding.py)
- [현대화 마일스톤](milestone_goal/modernization_milestone.md)
- [논문–코드–dependency 대응표](paper_code_dependency_map.md)

---

## 2026-08-27 — Retrieval wrapper migration 작업 기준

작성일: 2026-08-27
기준 커밋: `9d626f6`

### 1. 브랜치와 과거 기준점

- 임시 작업 브랜치 `experiment/retrieval-wrapper-migration`: `langchain-huggingface`와 `langchain-chroma` 이전, telemetry 정리와 clean-install 후보 검증만 수행한다.
- 과거 기준 annotated tag `odyssey-modernized-retrieval-legacy-wrapper`: 기존 LangChain community wrapper로 encoder와 top-5·top-10 fresh/reload fixture를 통과한 `9d626f6`을 변경 없이 보존한다.
- 기준 브랜치 `experiment/odyssey-modernized`: migration 결과가 합격하기 전까지 기존 검증 상태를 유지한다.

### 2. 병합 기준

신규 wrapper 조합은 기존과 같은 encoder revision·183개 corpus·L2 조건에서 encoder contract, top-5 기본·top-10 별도 profile, fresh index와 별도 프로세스 reload를 모두 통과해야 한다. 후보 순서와 score 차이를 legacy-wrapper tag 결과와 비교하고, telemetry 경고가 실제로 제거됐으며 exact version의 clean-install 후보를 제시해야 한다.

위 조건을 충족하고 연구자가 최종 dependency 조합을 승인한 뒤에만 임시 브랜치를 `experiment/odyssey-modernized`에 병합한다. 승인 전에는 기존 작동 조합을 제거하거나 신규 조합을 최종 lock으로 확정하지 않는다. 병합 뒤 임시 브랜치는 삭제하되 과거 상태는 tag와 이 보고 기록으로 보존한다.

---

## 2026-08-27 — Retrieval wrapper migration clean-install 검증

작성일: 2026-08-27
작업 브랜치: `experiment/retrieval-wrapper-migration`
비교 기준: `odyssey-modernized-retrieval-legacy-wrapper` (`9d626f6`)

### 1. 논문상 기능과 작업 목적

이번 작업은 자연어 subgoal과 183개 skill description을 같은 encoder로 변환하고 semantic closeness 순으로 candidate를 제시하는 Odyssey 기능을 보존하면서, 제거 예정인 LangChain community wrapper와 Chroma 0.3 저장 고리를 지원되는 공식 partner package로 분리할 수 있는지 확인했다.

현대화의 판정 대상은 새 package가 더 빠른지가 아니라 다음 retrieval contract의 보존 여부다.

- 공개 코드 checkpoint와 text-to-vector 변환 조건 유지
- top-5 기본·top-10 별도 profile 유지
- 183개 corpus의 candidate 순서와 L2 score 관찰
- fresh index와 별도 프로세스 reload의 동일성
- clean install과 telemetry·deprecated warning 제거

### 2. 호출 지점과 version 결합 감사

기존 환경은 `langchain 0.2.17`, `langchain-community 0.2.19`, `langchain-core 0.2.43`, `chromadb 0.3.29`와 `posthog 7.27.0`을 사용했다. 실제 호출은 다음 세 고리에 있었다.

1. `retrieval_embedding.py`: community `HuggingFaceEmbeddings` 생성
2. `SkillManager`와 `PlannerAgent`: community `Chroma` 생성 및 저장
3. Actor·Planner·Critic 등: `langchain.schema` message class import

`chromadb 0.3.29`는 `posthog`의 상한을 고정하지 않아 현재 `posthog 7.27.0`과 함께 설치됐고, telemetry `capture()` 인자 규약이 맞지 않았다. `pip check`는 package metadata상 의존성 범위만 확인하므로 이 runtime API 불일치를 탐지하지 못했다.

최신 공식 partner package의 요구 조건은 기존 `langchain-core 0.2`와 직접 공존하지 않았다. `langchain-huggingface 1.2.2`는 `langchain-core >=1.2.31`, `langchain-chroma 1.1.0`은 `chromadb >=1.3.5`와 `langchain-core >=1.1.3`을 요구했다. 따라서 import 두 줄만 바꾸지 않고 message class를 `langchain-core`로 옮기고 retrieval wrapper를 profile 경계에서 lazy import하도록 수정했다.

### 3. 기존 API와 신규 API contract 비교

| 항목 | Legacy community wrapper | Modern partner wrapper | 처리 |
|---|---|---|---|
| embedding class | `langchain_community.HuggingFaceEmbeddings` | `langchain_huggingface.HuggingFaceEmbeddings` | profile별 lazy import |
| model 인자 | `model_name=` | `model=` | 공통 factory에서 차이 흡수 |
| encoding 설정 | `encode_kwargs` | `encode_kwargs` | batch 32·float32·normalization 없음 유지 |
| Chroma class | community `Chroma` | `langchain_chroma.Chroma` | 공통 vector-store factory에서 분기 |
| persistence | DuckDB+Parquet와 명시적 `.persist()` | `PersistentClient`와 쓰기 시 자동 저장 | modern profile에서는 `.persist()` 호출 제거 |
| score 반환 | `similarity_search_with_score`의 distance | 동일 method의 distance | L2·candidate·score를 fixture로 비교 |
| telemetry | 기본 활성 및 `capture()` warning | `Settings(anonymized_telemetry=False)` | modern profile에서 warning 부재를 합격 조건으로 검사 |

공식 Chroma migration 문서에 따르면 0.4부터 저장 형식이 DuckDB+Parquet에서 SQLite 기반으로 바뀌고 수동 `.persist()`가 제거됐다. 기존 index는 원본 연구 자산이 아니라 고정 corpus에서 재생성 가능한 파생물이므로 migration하지 않고 183개 description에서 새로 만들었다.

### 4. 별도 시험 profile과 clean-install lock 후보

기존 조합을 제거하지 않고 `legacy-community`와 `modern-partner` 두 wrapper profile을 추가해 시험했다. 검증과 연구자 승인 뒤 `modern-partner`를 modernized 기본값으로 전환했으며 legacy 상태는 기준 tag로 보존한다.

Python 3.10.20의 빈 임시 환경에서 다음 핵심 조합을 설치했다.

| Package | Candidate version |
|---|---:|
| `langchain-core` | 1.6.0 |
| `langchain-huggingface` | 1.2.2 |
| `langchain-chroma` | 1.1.0 |
| `chromadb` | 1.3.5 |
| `posthog` | 5.4.0 |
| `sentence-transformers` | 5.6.0 |
| `transformers` | 5.14.1 |
| `torch` | 2.13.0+cpu |
| `huggingface-hub` | 1.24.0 |
| `tokenizers` | 0.22.2 |
| `numpy` | 1.26.4 |

첫 빈 환경의 전체 resolved version을 lock 후보에 기록한 뒤, 두 번째 빈 환경에 CPU PyTorch와 이 파일을 그대로 설치했다. 두 환경 모두 `pip check`에서 broken requirement가 없었다. 승인 뒤 파일을 `requirements-retrieval-modern.lock.txt`로 고정하고 기본 `requirements.txt`에서 참조하도록 연결했다. 최종 lock SHA-256은 `3fd810577c7f2bb40116bca05fa2b4f2a0bc481c7c0f713b046fbc94a463dbb2`다.

### 5. Encoder·retrieval·warning 결과

두 번째 clean 환경에서 encoder fixture는 `(3, 384)` float32, 반복 오차 `0.0`, newline/space 오차 `0.0`과 기존과 같은 embedding SHA-256 `4f5de76040931c0558f63c1e6083f6779c61f1611b81f9d456aa9b7263d32c6b`로 통과했다. 즉 wrapper 교체가 text-to-vector 결과를 바꾸지 않았다.

신규 Chroma index의 독립 fixture 결과는 다음과 같다.

| 검사 | 결과 |
|---|---:|
| index count | 183 |
| fresh top-5 recall@5 | 4/4 |
| fresh top-10 recall@10 | 4/4 |
| reload top-5·top-10 recall | 각각 4/4 |
| fresh/reload candidate 순서 | 전부 동일 |
| fresh/reload 최대 score 차이 | `0.0` |
| deprecated wrapper warning | 없음 |
| telemetry warning | 없음 |

따라서 신규 partner wrapper 자체의 encoder → index 생성 → reload → 검색 contract와 telemetry 비활성화는 통과했다.

### 6. Legacy 대비 score 차이와 최종 판단

Legacy와 modern의 top-10 후보 순서는 네 query에서 모두 같았지만 L2 score는 다음만큼 달랐다.

| Query | Legacy–modern 최대 절대 score 차이 |
|---|---:|
| `Craft a wooden pickaxe.` | `1.9073486328125e-06` |
| `Mine diamond ore using an iron pickaxe.` | `2.86102294921875e-06` |
| `Breed two cows using wheat.` | `7.62939453125e-06` |
| `밀을 사용해서 소 두 마리를 번식시킨다.` | `3.814697265625e-06` |

전체 최대 차이 `7.62939453125e-06`은 사전에 제안한 절대 허용값 `1e-6`을 넘었다. 그러나 이 값은 동일 구현의 반복 안정성을 확인하기 위한 임시 기준이었고 서로 다른 Chroma 구현의 동등성 기준으로 삼을 근거는 확인되지 않았다. Encoder byte checksum과 모든 후보 순서가 같고 각 modern index의 fresh/reload score는 정확히 같으므로, 이 차이는 stochastic한 변화가 아닌 dependency 내부 L2 수치 구현 차이로 기록한다.

현대화 자체의 성능 비교가 연구 목적이 아니므로 별도의 절대 허용값을 사후 설정하지 않는다. 논문 기능에 직접 대응하는 embedding checksum, top-k 후보 순서와 recall 보존, 동일 modern profile의 fresh/reload score 동일성, clean install과 warning 제거를 병합 기준으로 삼아 modern profile을 승인했다. 관찰된 raw score 차이는 숨기지 않고 진단값으로만 보존한다.

### 7. 근거와 공식 참고자료

- [Migration 실행 로그](../log/retrieval_wrapper_migration_2026-08-27.json)
- [Modern retrieval lock](../../Odyssey/requirements-retrieval-modern.lock.txt)
- [공통 wrapper profile factory](../../Odyssey/odyssey/retrieval_embedding.py)
- [Retrieval comparison fixture](../../Odyssey/scripts/semantic_retrieval_fixture.py)
- [LangChain HuggingFace encode contract](https://reference.langchain.com/python/langchain-huggingface/embeddings/huggingface/HuggingFaceEmbeddings/encode_kwargs)
- [LangChain Chroma API](https://reference.langchain.com/python/langchain-chroma/vectorstores/Chroma)
- [Chroma persistence migration](https://docs.trychroma.com/docs/overview/migration)

---

## 2026-08-27 — Primitive 40 runtime 전 코드 감사

작성일: 2026-08-27
대상 브랜치: `experiment/odyssey-modernized`
범위: 실제 Minecraft fixture를 추가하기 전에 논문 contract, working manifest, JavaScript source와 modern bridge dependency를 대조

### 1. 논문상 기능과 현재 증거

Odyssey의 primitive 40개는 183개 compositional skill이 Minecraft 상태를 바꾸기 위해 사용하는 하위 interface다. 이번 감사는 40개를 모두 온라인으로 실행하는 것이 아니라, 실행 전에 정상 입력에서도 실패할 명백한 오류와 공개 코드의 설계 선택일 수 있어 연구자 의도 확인이 필요한 차이를 분리했다.

- Odyssey 추가 primitive 22개와 Voyager 상속 custom primitive 8개 및 지원 함수는 모두 JavaScript syntax 검사를 통과했다.
- Voyager에서 직접 사용하는 Mineflayer API 10개는 현재 Mineflayer 4.25.0과 pathfinder source에서 interface 존재를 확인했다.
- `goto`와 `getAnimal`은 offline 14/14와 Minecraft online fixture를 통과했다.
- 기존 E0의 원목·작업대 반복 fixture는 `mineBlock`, `craftItem`, `getPlanksCount`와 `exploreUntil`의 일부 실행 경로를 간접적으로 통과했다. 다만 `exploreUntil`의 실제 이동·timeout branch까지 모두 검증한 것은 아니다.

### 2. 명백한 오류

아래 항목은 연구 의도와 무관하게 현재 dependency에서 존재하지 않는 API를 호출하거나, 정상적인 실패 조건 뒤에도 실행을 계속하거나, 선언되지 않은 상태를 사용하는 결함이다. 수정 뒤 offline regression을 먼저 통과해야 한다.

| Primitive·계층 | 코드상 오류 | 예상 결과 |
|---|---|---|
| `killMob`·combat bridge | `killMob`은 `bot.pvp`와 `bot.hawkEye`를 호출하지만 modern bridge는 두 plugin을 설치·load하지 않는다. Legacy에는 `mineflayer-pvp 1.3.2`, `minecrafthawkeye 1.3.6`이 있었다. | entity가 존재하는 실제 전투에서 undefined API 오류 |
| `getItemFromChest` | 설치된 Mineflayer 4.25.0 container에는 없는 `chest.findContainerItem()`을 호출한다. 현재 API는 `containerItems()`, `withdraw()`, `deposit()` 경로다. | chest를 정상적으로 열어도 인출 단계에서 오류 |
| `feedAnimals` | 종별 먹이를 조회하거나 hand에 장착하지 않고 `bot.useOn(animal)`을 호출한다. | 논문의 “appropriate food로 먹인다”는 contract를 수행하지 못함 |
| `cookFood` | coal이 없다는 메시지를 낸 뒤 return하지 않고 furnace 배치와 `smeltItem`을 계속 호출한다. 완료 메시지도 실제 `count`와 무관하게 항상 1개라고 기록한다. | 실패를 성공처럼 이어가거나 잘못된 결과 보고 |
| `killMonsters` | `isAlive`와 반복 변수 `i`를 선언하지 않고, target이 `null`이어도 `monster.position`을 참조하며, death listener를 제거하지 않는다. | 전역 상태 오염, null dereference와 반복 실행 listener 누적 |
| `plantSeeds` | `findBlocks()`의 빈 배열을 `if (!farmland)`로 검사하고 seed 존재를 확인하지 않은 채 equip한다. | farmland·seed가 없는 failure path가 의도대로 종료되지 않음 |
| `eatFood` | 지정 food가 inventory에 없는 경우를 확인하지 않고 `bot.equip(null, "hand")`을 호출한다. | 정상적인 missing-item 조건이 구조화되지 않은 runtime 오류가 됨 |
| `findSuitablePosition` | 세 높이 층의 offset 목록에 `(-1, *, 1)`이 중복되고 대응하는 `(1, *, -1)`이 누락됐다. | 탐색 영역이 의도치 않게 비대칭이 됨 |

`killAnimal`은 자체 syntax보다 `killMob`의 누락 combat plugin에 의해 함께 막힌다. `killMonsters` 또한 같은 blocker를 공유하므로 combat dependency를 복구하거나 별도 지원 profile로 고정하기 전에는 online 성공을 주장할 수 없다.

### 3. 연구자 의도 확인 또는 fixture로 판별할 영역

아래 항목은 위험이 보이지만 공개 코드가 의도적으로 택한 동작일 가능성을 배제할 수 없다. 임의 수정하지 않고 논문 contract와 기존 compositional caller를 함께 보존하는 방향을 정한 뒤 처리한다.

| 항목 | 논문·구현 차이 | 판단할 내용 |
|---|---|---|
| spatial signature | 논문의 `checkBlockAbove`·`checkBlocksAround`은 `(x,y,z)`를 받지만 공개 코드와 기존 compositional skill은 `Vec3`를 전달한다. | 기존 `Vec3` caller를 유지하면서 좌표 signature도 받는 호환 interface로 만들지 결정 |
| placement target | 논문의 `findSuitablePosition`은 대상 block이 `air`여야 하지만 구현과 기존 manifest는 `air` 또는 `water`를 허용한다. | 논문 contract대로 air만 허용할지, water 허용을 공개 코드 profile로 보존할지 결정 |
| pathfinder goal | `plantSeeds`와 `feedAnimals`는 점유된 farmland·entity 좌표에 `GoalBlock`을 사용한다. | 실제 접근 실패인지 online fixture로 확인하고 `GoalNear`·`GoalLookAtBlock` 전환 여부 결정 |
| armor 우선순위 | `equipArmor`는 diamond → iron → gold → chainmail → leather 순이다. “best”가 방어력, 재료 tier 또는 공개 코드 순서를 뜻하는지 명시되지 않았다. | 논문 재현에서는 공개 순서를 보존할지 게임 수치 순으로 정렬할지 결정 |
| drop 회수 책임 | `killMob`이 drop을 수집한 뒤 `killAnimal`이 과거 entity 위치로 다시 이동하고 수집 완료를 출력한다. | primitive 간 책임 중복을 제거할지 공개 orchestration을 유지할지 결정 |
| combat command | `killMonsters`가 `/gamemode survival`을 직접 호출한다. | 일반 primitive에서 OP command를 허용할지, controlled combat profile에만 둘지 결정 |
| exploration randomness | `exploreUntil`은 `Math.random()`으로 10~29 block 이동량을 정한다. | production 탐색은 유지하되 fixture에서 RNG를 주입·고정할지 결정 |

#### 쟁점 이해를 위한 설명과 예시

`Vec3`는 Minecraft의 `(x,y,z)` 좌표를 하나의 3차원 vector 객체로 묶은 자료형이다. 예를 들어 `new Vec3(10, 64, -5)`는 `x=10`, `y=64`, `z=-5`를 가지며, `position.plus(new Vec3(0, 1, 0))`은 바로 위 좌표를, `position.distanceTo(other)`는 다른 위치까지의 거리를 계산한다. 논문의 `checkBlockAbove(bot, "air", 10, 64, -5)`와 공개 코드의 `checkBlockAbove(bot, "air", new Vec3(10, 64, -5))`는 같은 위치를 전달하지만 parameter 표현이 다르다.

`findSuitablePosition`은 crafting table, furnace와 chest 같은 장치를 놓기 전에 bot 주변의 후보 좌표를 순서대로 검사하는 함수다. 후보 위치의 block이 비어 있고 주변 6방향 중 흙·돌처럼 장치를 붙일 reference block이 하나 이상 있으면 해당 좌표를 반환한다. 상위 skill은 `const position = await findSuitablePosition(bot)`으로 좌표를 받은 뒤 `placeItem(bot, "furnace", position)`처럼 사용한다. 따라서 이 함수의 결과는 다수의 crafting·smelting·storage skill의 배치 성공에 함께 영향을 준다. 논문은 대상 위치를 `air`로 설명하지만 공개 구현은 `air`와 `water`를 모두 후보로 검사한다.

`GoalBlock(x,y,z)`은 일반적으로 bot의 발 위치가 지정 block 좌표에 도달하도록 요구하는 pathfinder goal이다. `plantSeeds`는 이미 farmland block이 차지한 좌표를, `feedAnimals`는 계속 움직일 수 있는 entity 좌표를 이 goal에 넣는다. Source만으로 실제 pathfinder의 도달 판정을 확정할 수 없어, 이 항목은 정적 입력·실패 처리와 분리해 Minecraft 상태에서 관찰해야 한다.

`equipArmor`의 “best”는 하나의 수치로 명시돼 있지 않다. 공개 구현은 diamond → iron → gold → chainmail → leather 순으로 먼저 발견한 장비를 선택한다. Minecraft에서는 재료 등급이 대체로 방호력·내구도와 함께 올라가지만 gold는 예외이며, chainmail은 gold보다 내구도가 높고 leggings는 방호력도 더 높다. 따라서 “best”가 공개 코드의 재료 나열 순서인지 실제 방호력·내구도인지에 따라 gold와 chainmail의 상대 순서가 달라진다.

`killAnimal`과 `killMob`의 책임 중복은 다음 상황에서 드러난다. Cow A가 `(10,64,5)`, Cow B가 `(12,64,5)`에 있을 때 `killAnimal`이 먼저 Cow A를 기억하더라도, 내부의 `killMob("cow")`은 `nearestEntity()`를 다시 호출하므로 이동과 거리 변화 뒤 Cow B를 선택할 수 있다. `killMob`이 Cow B를 죽이고 beef·leather까지 수집한 뒤에도 `killAnimal`은 처음 기억한 Cow A의 과거 위치로 이동하고 실제 추가 수집 여부와 관계없이 `Collected dropped items.`를 출력한다. 이 경우 선택 대상, 실제 처치 대상과 성공 메시지가 서로 다를 수 있다.

`/gamemode survival`은 일반 chat이 아니라 OP 권한이 필요한 server command다. 생성된 JavaScript는 전체 `bot` 객체를 받으므로, bot이 OP라면 논리적으로 `bot.chat("/gamemode creative")`, `bot.chat("/give @s diamond 64")` 또는 `bot.chat("/tp @s ...")` 같은 command도 실행할 수 있다. Planner나 orchestrator가 정상적으로 subgoal만 생성할 것이라는 기대와 별개로, 현재 interface 자체는 `/`로 시작하는 command를 기술적으로 차단하지 않는다.

`exploreUntil`의 이동 거리는 `Math.floor(Math.random() * 20 + 10)`으로 계산돼 호출할 때마다 10~29 block 사이에서 달라진다. Production에서는 같은 방향을 탐색해도 12칸 또는 25칸처럼 서로 다른 goal이 만들어질 수 있다. Offline fixture에서 `Math.random()`의 반환값을 잠시 `0`으로 두면 항상 10 block, `0.999`로 두면 항상 29 block이 계산되므로 goal 좌표, cleanup과 timeout 분기를 반복해서 같은 조건으로 관찰할 수 있다. 이는 production 탐색을 고정한다는 뜻이 아니라 fixture 안에서만 난수 결과를 예측 가능하게 만든다는 뜻이다.

이 구분에서 “의도 확인”은 오류 가능성이 낮다는 뜻이 아니다. 논문과 공개 코드 중 어느 쪽을 modernized contract로 삼을지 결정해야 수정 방향이 달라진다는 뜻이다. 특히 `GoalBlock` 접근은 source만으로 실패를 단정하지 않고 Minecraft fixture로 판별한다.

### 4. 권장 검증 순서

1. Spatial·inventory·equipment·count처럼 server가 필요 없는 primitive를 mock bot offline fixture로 묶는다.
2. 위 명백한 오류를 수정하고 성공, 입력 누락, 빈 검색 결과와 실패 후 상태를 회귀로 고정한다.
3. Voyager custom primitive의 placement, smelting과 chest contract를 offline interface fixture로 확인한다.
4. Mineflayer 직접 API 10개는 각각 별도 서버를 띄우지 않고 farming, consume, fishing, sleeping과 entity interaction 대표 fixture로 묶는다.
5. Minecraft online 검증은 farming, placement/cooking, storage, inventory/equipment와 combat의 기능군 단위로 수행한다. Combat은 dependency와 `/gamemode` 정책을 확정한 뒤 마지막에 분리한다.

따라서 최종 `40/40`은 모든 항목에 적어도 syntax·offline contract 또는 direct-interface 증거가 있고, 실제 world state가 필요한 기능군에 대표 online fixture가 있을 때 표시한다. 38개를 각각 별도 online 실행하는 방식은 요구하지 않는다.

### 5. 근거 파일

- [Primitive 40 working manifest](../manifest/odyssey_primitive_40.json)
- [현재 primitive offline fixture](../../Odyssey/scripts/primitive_runtime_offline.js)
- [현재 primitive online fixture](../../Odyssey/scripts/primitive_runtime_online.py)
- [Odyssey 추가 primitive source](../../Odyssey/skill_library/skill/primitive)
- [Voyager 상속 control primitive source](../../Odyssey/odyssey/control_primitives)
- [Modern Mineflayer bridge](../../Odyssey/odyssey/env/mineflayer/index.js)

---

## 2026-08-27 — Primitive 명백 오류 전 선행 정책 6항목

작성일: 2026-08-27
대상 브랜치: `experiment/odyssey-modernized`
범위: 연구자가 확정한 공개-code contract와 실행 권한 경계를 명백 오류 수정 전에 고정. `plantSeeds`·`feedAnimals`의 Pathfinder goal은 이 단계에서 변경하지 않음

### 1. 논문 기능에 대응하는 한 줄 설명

Compositional skill이 공유하는 primitive의 입력 형식·배치 조건·장비 선택·전투 후처리·탐색 난수와 서버 권한 경계를 먼저 고정해, 이후 결함 수정이 공개 Odyssey의 행동 의미를 임의로 바꾸지 않게 했다.

### 2. 확정한 contract와 구현

| 항목 | modernized contract | 구현·증거 |
|---|---|---|
| Spatial position | 공개 compositional caller와 같은 `Vec3`를 사용 | `checkBlockAbove`·`checkBlocksAround`의 `Vec3` 입력과 plain object 거부를 offline fixture로 확인 |
| Placement target | 공개 코드 우선으로 `findSuitablePosition`의 `air` 또는 `water` 후보를 유지 | 인접 reference block이 있는 water 좌표가 반환되는 fixture 통과 |
| Armor order | 사용자가 이해하기 쉬운 공개 재료 순서 diamond → iron → gold → chainmail → leather 유지 | 네 armor slot 모두 gold와 chainmail이 함께 있을 때 gold가 선택됨을 확인 |
| Drop ownership | `killMob`이 target 선택·처치·drop 회수와 결과를 소유하고 `killAnimal`은 sword 장착 뒤 한 번만 위임 | `killAnimal`의 과거 entity 재이동과 중복 수집 메시지를 제거하고 단일 위임 fixture 통과 |
| Server operator boundary | 실행 bot은 non-OP, world 준비·gamemode·summon·reset은 연구자/서버 호스트의 container-local RCON harness가 담당 | modernized `ops.json=[]`, generated skill의 `/` command 차단, hard reset·inventory injection 거부, `host_admin_rcon.py` 추가 |
| Exploration randomness | episode seed 42에서 시작하는 재현 가능한 의사난수 sequence를 사용하되 탐색 거리는 계속 10~29 block 사이에서 변함 | 같은 seed의 8개 값이 일치하고 값들이 고정 상수가 아님을 fixture로 확인 |

`42`는 특별한 Minecraft 의미나 성능 근거가 있는 값이 아니라, 동일한 탐색 조건을 다시 만들기 위한 명시적 기본 seed다. 구현은 32-bit LCG 상태를 episode마다 42로 초기화하며 `/health`에 seed와 현재 RNG state를 노출한다.

### 3. 권한 격리의 의미

Node wrapper의 `/` 차단만으로 보안을 주장하지 않는다. 최종 권한 경계는 Minecraft server의 빈 operator 목록이다. 실행 bot이 잘못 생성된 `bot.chat("/give ...")` 코드를 전달받더라도 server 권한으로 관리자 명령을 수행할 수 없어야 한다. 연구자가 fixture를 준비할 때만 Git에서 제외된 RCON 비밀번호와 `docker compose exec` 기반 host harness를 사용하며, RCON port는 host network에 publish하지 않는다.

기존 E0의 OP bot·hard reset 절차는 과거 tag/profile의 재현 기록으로만 남는다. Modernized Python bridge는 soft reset을 기본값으로 사용하고 world state injection을 명시적으로 거부한다. `/pause`도 기본 no-op이며 명시적 legacy adapter에서만 호출한다.

### 4. 자동검사 결과와 아직 주장하지 않는 것

```text
PASS spatial primitives keep the public Vec3 contract
PASS findSuitablePosition preserves water as a public-code target
PASS equipArmor preserves gold before chainmail
PASS killAnimal delegates target, combat and drop ownership once
PASS exploration seed 42 produces a repeatable non-constant sequence
PASS modernized execution profile contains no bot operator
6/6 primitive policy fixtures passed
```

Offline 결과 뒤 같은 날 modernized server를 실제 재기동해 권한 경계도 확인했다. 첫 RCON 호출은 server가 listener를 열기 1초 전에 도착해 connection refused가 발생했으며, server health 확인 뒤 재실행하면 정상 동작했다. 이 startup race를 반복하지 않도록 host harness는 connection refused에 한해서 1초 간격·최대 10회 재시도한다.

```text
Minecraft: healthy, RCON running on 0.0.0.0:25575
host prepare-player: inventory 3개 제거, player kill/respawn 성공
deop bot: Nothing changed. The player is not an operator
/health: connected=true, position_finite=true, inventory={}
/health: exploration_seed=42, exploration_rng_state=42
/health: operator_commands_enabled=false
agent /gamemode creative: Server commands are restricted to the host-admin RCON harness
RCON playerGameType after denial: 0 (survival)
```

따라서 server-level non-OP, host-only 관리자 경로, agent command 거부와 seed 42 초기 상태까지 online으로 통과했다. `killMob`의 combat plugin 부재 등 기존 감사에서 명백한 오류로 분류한 항목은 아직 수정하지 않았고, `GoalBlock` 판단은 합의한 순서대로 모든 나머지 문제 뒤로 미뤘다.

이번 실행의 `runtime/minecraft/mods`에는 과거 legacy pause JAR 4종이 남아 있어 server가 이를 함께 load했다. 권한 검증 경로는 `/health`, soft `/start`, `/step`과 RCON만 사용해 `/pause`를 호출하지 않았지만, 이 결과를 “mod-free 재검증”으로 확대하지 않는다. Bridge에서는 `physicTick` deprecated-event 경고도 한 번 관찰됐다. 현재 project source는 이미 `physicsTick`을 사용하므로 dependency 내부 발생 여부를 나머지 executor 경고 감사에서 추적한다. 두 관찰 모두 이번 non-OP·seed 판정을 바꾸지는 않았다.

정적 검색 결과 `odyssey/test_env/*`, `givePlacedItemBack`과 compositional `placeMinecartOnRail`에는 여전히 bot이 직접 `/tp`, `/fill`, `/give`, `/summon` 등을 호출하는 과거 경로가 있다. Modernized profile에서는 이 코드가 관리자 권한을 얻는 대신 명시적으로 거부된다. Test environment 준비 명령은 host harness로 옮기고, 논문 기능인 item 회수·minecart 배치는 일반 Mineflayer 동작으로 바꾸거나 별도 controlled fixture로 분류해야 한다. 이 후속 migration은 권한 경계를 무력화하지 않고 나머지 명백 오류와 함께 처리한다.

### 5. 근거 파일

- [Primitive policy offline fixture](../../Odyssey/scripts/primitive_policy_offline.js)
- [Primitive 40 working manifest](../manifest/odyssey_primitive_40.json)
- [Host-only RCON harness](../../Odyssey/scripts/host_admin_rcon.py)
- [Modern server operator profile](../../Odyssey/server-profile/modernized/ops.json)
- [실행·검증 절차](../README.md#32-터미널-1-minecraft-서버-실행)
