# Odyssey 안전한 재현 환경 마일스톤

> 문서 역할: 현재 목표, 수행 순서와 완료 조건을 관리한다. 이미 보고한 과정과 결과는 [`report_log.md`](../report_log.md)에 시간순으로 누적하고 여기서 반복하지 않는다.

최종 갱신: 2026-08-27
참조 브랜치: `master` (`odyssey-legacy`)  
작업 브랜치: `experiment/odyssey-modernized`

## 목표

공개 Odyssey의 핵심 기능을 구형 의존성 문제로부터 분리해, 지원 가능하고 반복 설치 가능한 환경에서 실행한다. 현대화는 독립 연구 주제나 성능 경쟁이 아니라 MineSkynet 가설을 검증하기 위한 안정적인 연구 기반을 만드는 작업이다.

`master`는 논문 기능과 원본 구현을 확인하는 source reference로 보존한다. 원본 bridge나 구형 package를 다시 실행해 modernized와 성공률·latency를 비교할 필요는 없다. 교체 근거는 source/dependency 감사, 기존 오류 기록과 modernized 회귀 결과로 남긴다.

## 보존할 논문 기능

다음 기능은 dependency를 정리한다는 이유로 제거하지 않는다.

- 40개 primitive와 183개 compositional skill 및 자연어 description
- 공개 코드 설정의 `paraphrase-multilingual-MiniLM-L12-v2`: 자연어 subgoal과 skill description을 각각 384차원 vector로 바꿔 의미가 가까운 skill 후보를 찾는 소형 다국어 문장 embedding model이다. 이는 논문이 명시한 checkpoint가 아니라 공개 `conf/config.json`이 선택한 checkpoint이며, modernized 재현 기준으로 사용한다.
- vector similarity 기반 top-5 skill retrieval을 기본 profile로 고정하고, top-10은 별도 retrieval profile로 분리
- recursive prerequisite와 기존 JavaScript skill 실행
- MineMA actor의 candidate 선택과 실행 feedback
- planner–actor–critic, task decomposition, 검증과 재계획
- 논문 task/benchmark, prompt와 성공 조건

Voyager의 automatic curriculum, code generation/repair, self-verification과 dynamic skill commit은 공개 Odyssey의 고정-library baseline과 구분한다. `voyager-lifelong`에서 별도로 보존하고, Odyssey와 결합한 `odyssey-full`은 확장 profile로 명명한다.

## Dependency 안전성 원칙

- 실행에 필요한 dependency와 optional·combat·training dependency를 구분한다.
- 각 profile은 exact lockfile, 지원 Python/Node/Java/CUDA 범위와 clean-install 명령을 가진다.
- executor, retrieval, model service와 training 환경을 분리해 한 package 충돌이 전체 runtime을 막지 않게 한다.
- optional 기능은 lazy import하고 사용하지 않는 model·vector DB·launcher를 eager initialization하지 않는다.
- 외부 library는 신뢰받고 유지보수되는 구현을 우선한다. 이미 검증된 Chroma·LangChain·Sentence Transformer 기능을 근거 없이 직접 재작성하지 않는다.
- version update는 최신화 자체가 목적이 아니다. 지원 상태, 호환성, 보안과 재현성을 기준으로 선택하고 회귀를 통과한 조합을 고정한다.
- timeout, non-2xx, parse error, invalid skill, execution error와 verification failure를 명시적으로 구분한다.
- health check, 실패 뒤 복구와 구조화 로그를 제공한다.
- vulnerability 경고는 기록하고 영향 범위를 판단하되, 호환성 검증 없이 자동 upgrade를 적용하지 않는다.

## 현재 작업 목표 — 2026-08-27

현재 목표는 정적으로 고정한 skill library를 실제 실행 가능한 primitive 계층과 반복 재현 가능한 retrieval 입력 계층으로 올리는 것이다. 이번 작업에서는 모든 primitive와 Odyssey 전체를 한꺼번에 재현하지 않고, compositional skill이 의존하는 핵심 contract가 조용히 실패하지 않는 상태부터 만든다.

### 오늘 목표

- [x] `goto`·`getAnimal` 결함을 수정하고 offline 14/14와 두 Minecraft online fixture를 통과했다.
- [x] semantic encoder revision, canonical artifact checksum, 길이 128, mean pooling, normalization 없음과 newline 전처리를 manifest에 고정했다.
- [x] skill retrieval과 planner QA retrieval이 같은 명시적 encoder 설정을 사용하도록 공통 factory로 묶고 정적 fixture를 통과했다.
- [x] CPU runtime fixture에서 `(3, 384)` float32 출력, 유한값과 반복·newline 전처리 오차 `0.0`을 확인했다.
- [x] 183개 description을 indexing한 top-5 smoke에서 영어 3개·한국어 1개 query의 기대 skill이 모두 rank 1로 반환됐다.
- [x] top-5 기본·top-10 별도 profile을 구현하고, fresh index와 별도 프로세스 reload에서 네 query의 후보 순서와 score가 모두 유지됨을 확인했다.
- [x] 신규 LangChain partner wrapper를 두 clean 환경에서 검증하고 최종 retrieval lock과 기본 profile로 승인했다. Legacy와의 미세한 L2 score 차이는 후보 순서와 recall에 영향을 주지 않는 내부 수치 차이로 기록했다.
- [x] Primitive 선행 정책 중 `Vec3`, air/water 배치, 공개 armor 재료 순서, 단일 drop 책임과 seed 42를 contract fixture로 고정했다.
- [x] 실행 bot을 non-OP로 격리하고 world 준비를 host RCON harness로 분리했다. 실제 server에서 non-OP, host RCON 성공, agent `/gamemode` 거부와 survival 유지까지 확인했다.

코드 감사·수정·offline 자동 검증과 결과 문서화는 구현 작업으로 진행한다. Minecraft server·bridge 기동, world/entity 준비와 장시간 관찰은 연구자가 수행하며, 실행 전 정확한 명령과 확인할 결과를 제공한다.

### 이어서 수행할 순서

1. 선행 정책 6항목의 offline 검증을 기준선으로 삼아, 감사에서 판정한 나머지 명백 오류를 기능군별로 수정·검증한다.
2. 나머지 primitive 문제를 모두 처리한 뒤 `plantSeeds`·`feedAnimals`의 Pathfinder goal을 online fixture에서 마지막으로 판단한다.

오늘은 MineMA actor, planner–actor–critic end-to-end, 능동 skill 생성과 legacy 성능 비교로 범위를 확장하지 않는다. 진행 중 결과는 component 성공을 전체 완료로 올리지 않고 이 절의 checklist와 아래 세부 상태에 함께 반영한다.

## 진행 상태

표시는 `[x]` 완료, `[~]` 일부 근거 확보, `[ ]` 미완료를 뜻한다. 각 절의 첫 문장은 연구자가 확인하려는 논문 기능이고, 아래 checklist는 이를 입증할 구현 증거다.

### 논문–코드–dependency 대응 `[~]`

논문이 설명한 각 기능이 현재 어느 코드와 model에 의해 수행되는지 연결해, dependency를 바꿔도 연구 기능을 잃지 않게 한다.

- [x] 논문의 각 기능을 source file, dependency, model과 input/output에 연결
- [~] task, prompt, **primitive 40 manifest**, 183 skill corpus와 checkpoint 출처·hash 고정
- [x] dependency를 core, executor, retrieval, model, combat, training으로 1차 분류
- [~] retrieval modern profile의 exact version lock과 clean-install 절차 작성·재설치 통과; 나머지 profile lock은 미완료
- [~] license, 보안 경고, deprecated API와 유지보수 상태 기록
- [x] branch 역할과 범위 기반 tag 정책 확정

세부 근거와 미해결 조건은 [`paper_code_dependency_map.md`](../paper_code_dependency_map.md)에 기록했다. primitive 40개의 논문–source working manifest와 compositional code·description 183쌍의 checksum을 고정했다. **Voyager 상속 primitive 18개의 runtime interface fixture와 source상 contract 위험의 수정·검증**은 남았다. Encoder와 retrieval modern profile의 clean-install은 확보했으며 나머지 profile lock은 후속 검증이다.

### Minecraft 실행 계층 `[x]`

actor가 선택한 JavaScript skill이 실제 Minecraft 상태를 바꾸고, 오류가 나도 다음 실행을 계속할 수 있는지 확인한다.

- [x] Mineflayer bridge health/version과 request-local bot lifecycle
- [x] finite position guard와 failure 뒤 bridge 생존
- [x] `/pause` 없이 mod-free server에서 나무와 작업대 각각 10/10
- [x] inventory delta, latency, dependency와 Minecraft log 자동 저장
- [x] bridge·pause bundle·bot lifecycle의 결합 문제와 변경 이유 문서화
- [x] `a157205`를 `odyssey-modernized-executor-1.19.4` annotated tag로 로컬·원격에 고정

원본 bridge의 재실행이나 legacy 대비 latency 표는 요구하지 않는다. 현재 실행 계층이 clean install, 정상 행동과 대표 failure recovery를 반복 통과한 것으로 이 범위를 완료한다.

### Skill library와 semantic retrieval `[~]`

자연어 subgoal과 의미가 가까운 기존 skill을 논문 조건에 따라 반복해서 후보로 제공할 수 있는지 확인한다.

- **[~] primitive 40개의 provenance·API working manifest와 함수 syntax 확인; `goto`·`getAnimal` offline 14/14 및 online 통과, 선행 정책 fixture 6/6 통과, 나머지 명백 오류와 최종 Pathfinder goal 검증은 미완료**
- [x] compositional code 183개와 대응 description 183개의 파일별 SHA-256 기록
- [x] `skills.json` 183 key를 code·description 원본과 동기화하고 runtime bundle checksum 기록
- [x] code가 없는 `killOnePlayer.txt`를 기본 corpus에서 제외하고 orphan으로 기록
- [x] 공개 코드 설정의 encoder를 modernized 재현 기준으로 선정하고 논문 명시 checkpoint가 아님을 기록
- [x] [encoder manifest](../../manifest/odyssey_semantic_encoder.json)에 revision·checksum, 변환 조건과 CPU runtime vector 관찰값 고정
- [x] 자연어 subgoal → 183개 description index → 기본 top-5 candidate 흐름 재현
- [x] top-10을 별도 retrieval profile로 구성
- [x] [profile 실행 로그](../../log/semantic_retrieval_profiles_2026-08-27.json)에 known-query recall@5 `4/4`, recall@10 `4/4`와 전체 후보·L2 score 기록
- [x] L2 metric을 고정하고 fresh index 생성과 별도 프로세스 reload에서 두 profile의 후보 순서 동일·최대 score 차이 `0.0` 확인
- [x] [modern retrieval lock](../../../Odyssey/requirements-retrieval-modern.lock.txt)을 서로 다른 빈 Python 3.10 환경에 설치하고 index 생성·재로드·검색 확인
- [x] `langchain-huggingface 1.2.2`·`langchain-chroma 1.1.0`·`chromadb 1.3.5`에서 deprecated/telemetry 경고 제거와 후보 순서 동일성 통과; legacy 대비 score 최대 차이 `7.62939453125e-06`은 검색 결과에 영향을 주지 않는 내부 수치 차이로 기록

Sentence Transformer와 semantic retrieval은 논문 기능이므로 제거 대상이 아니다. Chroma·LangChain은 기능을 제공하는 구현 선택이며, 변경 기준은 기능 contract, clean install, persist/reload와 유지보수 가능성이다.

### Actor와 model service `[ ]`

MineMA actor가 검색된 후보 안에서 정확한 skill을 선택하고, model service 오류를 잘못된 행동으로 숨기지 않는지 확인한다.

- [ ] 공개 prompt, candidate 표현, model checkpoint와 decoding 조건 확인
- [ ] MineMA actor의 candidate 선택과 실행 feedback 연결
- [ ] model service를 Odyssey runtime과 별도 lock/profile로 격리
- [ ] model·revision·precision을 응답과 trace에 기록
- [ ] timeout, HTTP status, response schema와 retry 상한 적용
- [ ] unknown skill silent fallback을 제거하고 명시적 오류 반환
- [ ] fixed/retrieved candidate의 offline 선택과 online 실행 회귀

deterministic stub endpoint는 service contract와 오류 처리를 검사하는 보조 harness다. stub 자체는 연구 milestone이나 Odyssey 재현 결과가 아니다.

### Planner–actor–critic end-to-end `[ ]`

목표 분해 → skill 검색·선택 → 실행 → 성공 판정·재계획이라는 논문의 전체 순환이 modernized 환경에서 연결되는지 확인한다.

- [ ] task decomposition과 recursive prerequisite 실행
- [ ] actor feedback과 critic 성공 판정
- [ ] retry, reflection/replanning과 checkpoint/resume
- [ ] 대표 논문 task의 state-based 성공 판정과 반복 회귀
- [ ] 전체 경로의 dependency snapshot, trace와 실패 분류 저장

여기서 필요한 것은 구형 runtime과의 속도 비교가 아니라 논문에서 사용하는 기능들이 modernized 환경에서 빠짐없이 연결되고 안정적으로 반복되는지 확인하는 것이다.

### 능동 skill lifecycle 보존 profile `[ ]`

Voyager의 핵심인 새 skill 생성·수정·검증·재사용을 기본 Odyssey 재현과 섞지 않고 별도 profile에서 보존한다.

- [ ] Voyager curriculum → code 생성 → 실행 → 검증 → repair
- [ ] 성공 skill의 description·embedding·provenance와 versioned commit
- [ ] quarantine, rollback, duplicate와 vector index consistency
- [ ] held-out task의 retrieval·reuse·transfer
- [ ] `voyager-lifelong`, `odyssey-legacy`, `odyssey-full` 명칭과 결과 분리

## 변경 판단 절차

dependency 또는 구현 고리를 변경할 때 다음만 확인한다.

1. 해당 고리가 보존해야 할 논문 기능인지 확인한다.
2. 현재 package/API가 설치 충돌, 지원 종료, 불필요한 결합 또는 복구 불가능성을 만드는지 source와 기록으로 확인한다.
3. 유지보수되는 외부 구현과 최소 변경을 우선한다.
4. clean install, import smoke, 기능 회귀와 failure recovery를 실행한다.
5. 기능을 훼손하거나 새 충돌을 만들면 되돌리거나 optional profile로 격리한다.

원본 runtime의 재실행, 동일 fixture 성능표와 “교체 구현이 더 빠르다”는 증명은 기본 요구사항이 아니다. 원인이 불명확해 현재 구현을 고칠 수 없는 경우에만 제한적으로 과거 commit을 실행한다.

변경 기록에는 affected function, 기존 dependency/결합, 변경 이유, 새 version/lock, 회귀 명령과 결과를 남긴다.

## 우선 정비 대상

| 영역 | 확인된 위험 | 안전한 상태 |
|---|---|---|
| Mineflayer bridge와 `/pause` | bot lifecycle, packet과 pause mod bundle 결합 | `/pause` 없는 request-local lifecycle, health와 failure recovery |
| Python 초기화 | raw actor도 planner·embedding·Chroma를 강제 초기화 | profile별 entrypoint와 lazy import |
| Python dependency | 대부분 unpinned이고 executor·retrieval·launcher가 한 환경에 혼재 | 역할별 lock과 import/clean-install smoke |
| model backend | model name·precision·response가 hard-coded | versioned adapter, timeout·status·schema 검증 |
| actor parser | unknown skill을 첫 후보로 바꾸는 silent fallback | exact candidate validation과 명시적 오류 |
| verifier | task 문자열별 hard-coded 판정 | state delta schema와 critic 결과의 명시적 구분 |
| Chroma/LangChain | 구형 API와 version 결합 가능성 | 신뢰받는 구현 유지, 지원 버전 고정과 persist/reload 회귀 |
| combat·launcher·training | core 실행에 필요 없지만 설치 충돌을 전파 | optional profile과 별도 lock |

## Tag 정책

- `odyssey-legacy-<scope>-<version>`: 원본 자산·기능 참조를 고정할 필요가 있을 때 사용
- `odyssey-modernized-<scope>-<version>`: 안전한 실행환경에서 검증된 기능 범위
- `mineskynet-<experiment>-<version>`: MineSkynet 연구 결과

`scope`는 `executor`, `retrieval`, `actor`, `end-to-end`처럼 실제 검증 범위를 명시한다. `odyssey-modernized-executor-1.19.4`는 실행 계층만 의미하며 full Odyssey 재현을 뜻하지 않는다.

## 당장 수행할 순서

1. **Primitive 의미 고정 `[~]`:** [40개 working manifest](../../manifest/odyssey_primitive_40.json)는 작성했다. `goto`, `getAnimal`과 기타 contract 위험을 수정한 뒤 Voyager 상속 interface까지 runtime fixture로 확인한다.
2. **Skill library 동일성 보장 `[x]`:** [checksum manifest](../../manifest/odyssey_skill_corpus.sha256)에 183개 compositional code와 자연어 description, runtime `skills.json`을 고정했다.
3. **Semantic retrieval 재현 `[x]`:** 공개 코드 encoder의 revision·전처리와 L2 metric을 고정하고, 기본 top-5·별도 top-10 후보와 fresh-index/reload 동일성을 회귀로 남겼다.
4. **Dependency 설치 재현 `[~]`:** retrieval modern profile의 exact version·clean-install을 재현하고 최종 lock으로 승인했다. 나머지 Python/Node package를 역할별로 고정한다.
5. **Actor 실행 연결:** MineMA가 검색된 후보에서 정확한 skill을 선택하고 recursive prerequisite까지 실행하게 한다.
6. **논문 전체 순환 연결:** planner–actor–critic의 계획·실행·검증·재계획을 대표 task로 반복 확인한다.
7. **연구 기반 고정:** 완료 commit/tag를 `mineskynet-core`의 base로 지정한다.

## `odyssey-modernized` 완료 조건

- 논문 핵심 기능이 modernized 환경에서 연결되고 대표 task를 반복 수행한다.
- core와 optional dependency가 구분되고 각 실행 profile이 exact lock을 가진다.
- 새 환경에서 clean install, import smoke와 service health check가 재현된다.
- executor, retrieval, actor와 end-to-end 회귀가 자동화돼 있다.
- skill retrieval은 top-5를 기본값으로 사용하고 top-10을 별도 profile로 추적한다.
- 오류가 조용히 fallback되지 않고 분류·기록되며 대표 실패 뒤 복구할 수 있다.
- model, encoder, skill corpus, dependency와 Minecraft fixture revision을 추적할 수 있다.
- Chroma·LangChain·Sentence Transformer 등 논문 기능을 담당하는 외부 구현을 불필요하게 재작성하지 않았다.
- 완료 commit/tag가 향후 `mineskynet-core`의 base로 지정돼 있다.

legacy runtime 대비 성능 개선표는 완료 조건이 아니다.
