# Odyssey 논문–코드–의존성 대응표

최종 갱신: 2026-08-27
대상 논문: `research/paper/odyssey.pdf`  
코드 기준: `a157205` 및 현재 작업 트리  
대상 profile: `odyssey-modernized`

## 먼저 읽을 요약

- **논문이 요구하는 것:** 자연어 목표를 계획하고 관련 skill을 검색·선택·실행한 뒤 관측 결과로 성공을 판단한다.
- **현재 확인한 것:** 주요 기능의 코드 위치와 dependency 역할, Odyssey 추가 primitive 22개와 compositional skill 183개의 대응을 확인했다.
- **연구자가 결정한 것:** 연산 부담을 고려해 top-5를 기본 retrieval profile로 고정하고 top-10은 별도 profile로 분리한다. 논문에 정확한 checkpoint가 명시되지 않았으므로 공개 코드 설정의 encoder를 modernized 기준으로 사용한다.
- **구현에서 정비할 것:** exact candidate 검증과 optional dependency 격리를 진행한다. retrieval modern profile의 clean-install lock과 corpus/index 재로드 회귀는 완료했다.
- **실행 시점:** 위 조건을 먼저 고정한 뒤 MineMA와 Minecraft server를 연결한다. legacy runtime 비교 실행은 요구하지 않는다.

이 문서의 항목은 다음 네 종류로 읽는다.

| 종류 | 의미 | 예시 |
|---|---|---|
| 논문 기능 | 결과에서 반드시 보존해야 하는 알고리즘 동작 | semantic retrieval, planner–actor–critic |
| 구현 선택 | 논문 기능을 실제 코드로 제공하는 수단 | Chroma, LangChain, HTTP service |
| 재현성 관리 | 같은 조건을 다시 사용했음을 보이는 장치 | checksum, lockfile, manifest |
| 논문–코드 차이 | 논문과 공개 코드의 조건이 달라 선택 근거와 profile을 밝혀야 하는 항목 | 공개 코드 encoder, top-5 기본·top-10 별도 profile |

## 1. 목적과 판정 원칙

이 문서는 Odyssey 현대화를 별도 성능 연구로 만들기 위한 문서가 아니다. 논문에서 필요한 기능이 공개 코드의 어디에 구현돼 있고 어떤 dependency와 model에 기대는지 고정해, 구형 의존성을 바꿀 때 알고리즘 기능을 함께 제거하지 않도록 하는 추적표다.

- `master`는 논문과 원본 구현을 확인하는 source reference다. 구형 runtime을 다시 실행해 성공률이나 latency를 비교하지 않는다.
- 변경의 합격 기준은 지원 가능한 환경의 clean install, 명시적 interface, 기능 회귀와 실패 복구다.
- Sentence Transformer, semantic retrieval, skill corpus와 planner–actor–critic은 보존 대상이다.
- Chroma·LangChain 같은 외부 구현은 구형 API 결합을 해소할 수 있지만, 자체 구현으로 대체하는 것을 기본값으로 삼지 않는다.
- 논문과 코드가 서로 다른 값을 제시하는 항목은 임의로 하나를 정답으로 만들지 않고 profile parameter와 검증 항목으로 남긴다.
- 이 대응표 작성에는 Minecraft server, MineMA backend 또는 legacy runtime을 실행하지 않았다.

## 2. 논문의 실행 흐름

```text
goal + constraints + environment observation
    → planner: task/subgoal과 context 생성
    → Sentence Transformer: context와 skill description embedding
    → vector similarity: candidate skill 검색
    → actor/MineMA: candidate 중 program 선택
    → Mineflayer executor: recursive JavaScript skill 실행
    → observation: inventory/world/chat/error/state delta
    → critic: success/self-validation/reflection
    → 성공, 재시도 또는 replanning
```

논문은 40개 primitive와 183개 compositional skill, 자연어 description, semantic retrieval, recursive prerequisite, planner–actor–critic을 하나의 기능 흐름으로 설명한다. dependency를 격리하더라도 이 연결은 유지해야 한다.

## 3. 기능 대응표

| 논문 기능 | 보존할 contract | 공개 코드 | 주 dependency/model | 현재 판정 |
|---|---|---|---|---|
| Minecraft environment와 observation | 실행 전후 inventory, status, voxel, entity, chest, chat와 error를 구조화 event로 반환 | `odyssey/env/bridge.py`, `odyssey/env/mineflayer/index.js`, `lib/observation/*` | Mineflayer, minecraft-data, Express, requests | executor 회귀 완료. `/pause`는 명시적 legacy adapter로 격리했고 modernized 기본은 no-op |
| Primitive skill | compositional skill이 호출할 안정된 저수준 동작 제공 | `skill_library/skill/primitive`, `odyssey/control_primitives`, `control_primitives_context/mineflayer.js` | Mineflayer, pathfinder, tool, collectblock | [40개 working manifest](../manifest/odyssey_primitive_40.json) 작성. 정책 fixture 6/6 통과, 나머지 명백 오류와 runtime 검증은 남음 |
| Compositional skill | 이름, code, description을 가진 재사용 skill이며 다른 skill을 재귀 호출 가능 | `skill_library/skill/compositional`, `skill/skills.json` | JavaScript executor와 primitive corpus | 183 code·description·JSON entry 동기화와 파일별 checksum 완료 |
| Skill description | 전체 program code에서 자연어 설명을 얻고 retrieval corpus로 사용 | `skill_library/skill/description`, `SkillManager.generate_skill_description` | 논문상 LLM; 현재 저장 corpus | 고정 corpus는 존재. 생성 경로는 비활성·불완전 |
| Semantic skill retrieval | 자연어 context와 descriptions를 같은 encoder로 embedding하고 유사도 순으로 candidate 반환 | `agents/skill.py: SkillManager.retrieve_skills`, `odyssey/retrieval_embedding.py` | Sentence Transformers → LangChain embedding adapter → Chroma | L2·top-5 기본·top-10 별도 profile 고정. 183개 fresh index와 별도 프로세스 reload에서 후보 순서·score 동일성 통과 |
| Planner QA retrieval | subgoal context를 만들기 위한 별도 QA cache 검색 | `agents/planner.py: PlannerAgent`, `curriculum/vectordb` | Sentence Transformers, Chroma, planner/MineMA endpoint | skill retrieval과 다른 DB임. eager initialization과 분리 필요 |
| Planner | goal, constraints, observation, completed/failed task를 받아 combat·farming·explore task를 제안·분해 | `agents/planner.py`, `Odyssey.learn`, `Odyssey.inference` | MineMA planner/QA model, LangChain message types | 기능은 존재. 세 mode별 입력·출력 fixture 필요 |
| Actor | task/context/feedback와 candidate를 받아 candidate의 정확한 program name을 반환 | `agents/actor.py`, `Odyssey.step` | MineMA actor endpoint, LangChain messages, Babel parser | unknown name을 첫 candidate로 바꾸는 silent fallback 수정 필요 |
| Skill executor | 선택된 code와 prerequisite programs를 동일 request에서 실행하고 event를 반환 | `Odyssey.step`, Mineflayer `/step`, `lib/skillLoader.js` | Python `javascript`, Babel, Node bridge | raw executor 회귀 완료. Babel package 선언 누락 확인 |
| Critic과 self-validation | execution feedback, inventory 변화와 관측 상태로 success/critique를 반환 | `agents/critic.py`, `Odyssey.step` | MineMA critic endpoint, observation schema | 일반 LLM critic과 일부 hard-coded subgoal 판정이 혼재 |
| Multi-round combat feedback | 전투 결과를 다음 round planner/actor 입력으로 연결 | `Odyssey.inference`, `agents/comment.py` | planner/actor/comment model, combat test environment | 현재 comment 경로 일부가 규칙 기반이며 논문 prompt와 대조 필요 |
| MineMA service | system/user message를 model endpoint에 보내 text 응답과 model revision을 반환 | `agents/llama.py`, `LLM-Backend` | FastAPI, transformers, torch, accelerate, bitsandbytes | 별도 환경은 적절함. timeout/status/schema와 revision trace 보강 필요 |
| Recorder와 benchmark | task별 success와 tick/time/iteration 및 평가 지표를 원시 기록과 연결 | `utils/record_utils.py`, `Odyssey.learn/inference`, `significance_test.py` | Python runtime | 대표 논문 task의 판정·반복 protocol 미고정 |
| 능동 skill 추가·수정 | 생성→실행→검증→description/embedding→versioned commit | `SkillManager.add_new_skill`, Voyager 계보 | LLM, Sentence Transformers, Chroma | 단계별 Odyssey baseline에서는 제외. `voyager-lifelong`/`odyssey-full`에서 보존 |

## 4. 확인된 corpus 상태

연구 목적은 모든 재현 실험이 논문과 같은 skill 집합을 사용하고, 코드나 description 변화로 검색 결과가 조용히 달라지지 않게 하는 것이다. 현재 작업 트리의 정적 집계는 다음과 같다.

| 자산 | 수량 | 확인 결과 |
|---|---:|---|
| `skill/primitive/*.js` | 22 | 논문에서 Odyssey가 추가했다고 명시한 14 operational + 8 spatial과 이름까지 일치 |
| `odyssey/control_primitives/*.js` | 11 | Voyager control과 Odyssey 실행 helper가 섞인 파일 수이며 primitive 수와 일대일 대응하지 않음 |
| `skill/compositional/*.js` | 183 | `skills.json` key와 전부 일치하고 file별 SHA-256 기록 |
| `skill/skills.json` | 183 | E0에서 검증한 `craftCraftingTable.js`와 내장 code 불일치 1건을 동기화한 뒤 code·description 전체 일치 확인 |
| `skill/description/*.txt` | 184 | compositional 183개와 전부 대응. code가 없는 `killOnePlayer.txt`는 기본 corpus에서 제외 |

현재 고정 가능한 checksum:

```text
skill/skills.json                         sha256 0be22fdc338d4db199c75d60ad6455ec67e9b1240bda56834014d886e0c87802
conf/config.json                          sha256 504cea1fc2489aff6e38f9c1000aabbc704bfe8c3ed5224778a9e9bf4d7113f5
requirements.txt                          sha256 45f8947cf4bb08525d94d1ceb1504d105c579d15afdcd05b45f839f5bf818ecc
mineflayer/package-lock.json              sha256 5555e896e0c5d19c635965bc9338b0cd60a248092bc9c8ff65a6c678943a6b7c
manifest/odyssey_primitive_40.json         sha256 446f462bb61e3799d3e7e6d9a3537113503f9911b33e9e6da6e47a86b0af33ea
manifest/odyssey_skill_corpus.sha256       sha256 31a4c1e3f7672a7a422628ddb9701b485286b25bb3edd67e403aeb9eaab73861
manifest/odyssey_semantic_encoder.json     sha256 c393693544bee8b799e8f1e576174cc3b2f9a1c3fb0ac83535748fec00677b1c
log/semantic_retrieval_smoke_2026-08-27.json sha256 b39d4838001a9da4bb1bda8a5fdc7b0a1921496cb66d767669296234e87704a5
log/semantic_retrieval_profiles_2026-08-27.json sha256 ee6e732eb797d6f09c211978d5b4a3df158ce6b30b83dd2cf3272d8bf5585e6f
log/retrieval_wrapper_migration_2026-08-27.json sha256 64559023994c0344e8425de93600679c4a33574513f9cdf1d893656b770465bb
Odyssey/requirements-retrieval-modern.lock.txt sha256 3fd810577c7f2bb40116bca05fa2b4f2a0bc481c7c0f713b046fbc94a463dbb2
```

`odyssey_skill_corpus.sha256`에는 compositional code 183개, 대응 description 183개와 실제 runtime bundle인 `skills.json` 1개가 들어 있다. 저장소 루트에서 `sha256sum --check --quiet research/manifest/odyssey_skill_corpus.sha256`로 367개 항목을 한 번에 확인한다.

### 4.1 Primitive 40개 working map

Odyssey 부록 C.1은 `Voyager의 operational 18 + Odyssey가 추가한 operational 14 + spatial 8 = 40`으로 정의한다. 공개 파일과 이름을 대조하면 Odyssey가 추가한 22개는 완전히 대응한다.

| 분류 | 논문 수 | 현재 source 대응 |
|---|---:|---|
| Odyssey operational | 14 | `plantSeeds`, `feedAnimals`, `killAnimal`, `killMonsters`, `cookFood`, `eatFood`, `equipArmor`, `equipSword`, `equipPickaxe`, `equipAxe`, `equipHoe`, `equipShovel`, `getLogsCount`, `getPlanksCount` |
| Odyssey spatial | 8 | `findSuitablePosition`, `checkAdjacentBlock`, `checkBlockAbove`, `checkBlocksAround`, `checkNearbyBlock`, `checkNoAdjacentBlock`, `goto`, `getAnimal` |

Voyager 부록 A.4와 현재 `control_primitives_context`를 함께 보면 상속된 18개의 재현 대상 interface는 다음 working map으로 설명할 수 있다.

- Voyager custom control 8개: `exploreUntil`, `mineBlock`, `craftItem`, `placeItem`, `smeltItem`, `killMob`, `getItemFromChest`, `depositItemIntoChest`
- 직접 실행하는 Mineflayer interface 10개: `bot.pathfinder.goto`, `bot.blockAt`, `bot.equip`, `bot.consume`, `bot.fish`, `bot.sleep`, `bot.activateBlock`, `bot.lookAt`, `bot.activateItem`, `bot.useOn`
- `Goal*` constructor와 `bot.isABed` 같은 predicate/helper는 위 interface가 사용하는 지원 API로 별도 추적한다.

이 18개 목록은 Odyssey 부록이 상속분을 다시 열거하지 않기 때문에 Voyager 부록과 공개 prompt context를 결합한 working map이다. 따라서 현재 파일 11개를 더해 수를 맞추지 않고, 각 interface가 modernized Mineflayer에서 호출 가능한지를 회귀 fixture로 확인해야 최종 고정된다.

전체 40개 항목의 논문 contract, source path, 주 호출 API와 정적 판정은 [`odyssey_primitive_40.json`](../manifest/odyssey_primitive_40.json)에 고정했다. 실제 함수 파일은 syntax 검사를 통과했다. `control_primitives_context/mineflayer.js`는 top-level `await` 예시를 포함한 prompt fragment이므로 실행 파일이 아니라 외부 API 선언 근거로만 취급한다. `goto`의 위치 오타·종료 조건과 `getAnimal`의 대입 조건·동물 유인 불일치는 수정했으며 offline fixture 14/14을 통과했다. `getAnimal(cow)`은 목표 유인, `goto`는 block-grid 거리 1.414와 `onError` 없음으로 2026-08-27 Minecraft online fixture를 각각 통과했다. 이후 연구자가 정한 `Vec3`, air/water 배치, 공개 armor 재료 순서, 단일 drop 책임, server-host OP 경계와 탐색 seed 42를 policy fixture 6/6으로 고정했고, 실제 server에서 non-OP·host RCON·agent command 거부·survival 유지도 확인했다. 나머지 명백 오류와 마지막 Pathfinder goal 판단은 남아 있다.

## 5. 재현 contract 초안

논문 기능이 package나 service 경계를 넘어가도 같은 입력이 같은 의미의 출력으로 이어지도록 최소 입출력을 고정한다.

### 5.1 Retrieval

입력은 자연어 `query`, corpus revision, encoder revision, distance metric과 `k`다. 출력은 순서가 보존된 candidate 목록이며 각 항목은 `skill_id`, `description`, `score`, `code_revision`을 가진다.

반드시 기록할 값:

- `skills.json` checksum
- Sentence Transformer model ID, local revision/checksum과 normalization 설정
- Chroma 및 adapter version, collection 이름, distance metric과 persist path
- query 원문, `k`, candidate 이름과 score

현재 `conf/config.json`은 `paraphrase-multilingual-MiniLM-L12-v2` 경로를 사용한다. 논문에서 정확한 checkpoint를 특정한 근거는 확인되지 않았으므로, 이 값을 논문 확정값이 아닌 공개 코드 설정의 modernized 재현 기준으로 사용한다. 검색 k는 연산 부담을 고려해 top-5를 기본값으로 고정하고 top-10은 별도 retrieval profile에서만 사용한다.

[`odyssey_semantic_encoder.json`](../manifest/odyssey_semantic_encoder.json)은 공개 checkpoint revision `e8f8c211226b894fcb81acc59f3b34ba3efd5f42`, PyTorch safetensors runtime에 필요한 11개 canonical artifact, 384차원·길이 128·attention-mask mean pooling·대소문자 유지·normalization 없음·float32 조건을 기록한다. LangChain adapter가 document와 query 모두에서 newline을 ASCII space로 치환하는 동작도 입력 contract로 고정했다. CPU encoder fixture는 `(3, 384)` 출력과 반복 오차 `0.0`으로 통과했다. 이어 183개 description을 L2 index에 넣은 [top-5 smoke](../log/semantic_retrieval_smoke_2026-08-27.json)에서 영어 3개·한국어 1개 query의 기대 skill이 모두 rank 1로 반환됐다. [profile fixture](../log/semantic_retrieval_profiles_2026-08-27.json)는 top-5를 기본값, top-10을 별도 profile로 실행해 두 profile 모두 known-query recall `4/4`를 기록했고, fresh index와 별도 프로세스 reload 사이의 모든 후보 순서가 같고 최대 score 차이가 `0.0`임을 확인했다.

### 5.2 Actor selection

입력은 `task`, `context`, 최신 observation/critique와 retrieval candidate 집합이다. 출력 program은 candidate의 정확한 ID와 일치해야 한다. 이름이 없거나 parser가 실패하면 첫 candidate를 실행하지 않고 구조화 오류를 반환해야 한다.

### 5.3 Executor와 observation

executor 입력은 선택된 code, prerequisite programs, bot/session 식별자와 timeout이다. 출력은 다음 event sequence를 보존한다.

```text
[[event_type, {
  status: {health, food, position, equipment, entities, inventoryUsed, elapsedTime, ...},
  inventory: {...},
  voxels: [...],
  blockRecords: [...],
  nearbyChests: {...},
  onChat: ...,
  onError: ...,
  onSave: ...
}], ...]
```

HTTP timeout, non-2xx, disconnected bot, JavaScript evaluation error와 critic verification failure는 서로 다른 오류로 기록한다.

### 5.4 Critic

입력은 task/context, 실행 전후 observation과 execution error다. 출력은 최소 `success: bool`, `critique`, `evidence`를 가진다. inventory 기반 deterministic check와 LLM self-reflection은 같은 값으로 숨기지 말고 verifier 종류를 기록한다.

### 5.5 Model service

요청에는 model endpoint, system/user message와 decoding profile이 포함돼야 한다. 응답과 trace에는 model ID/revision, precision, decoding parameter, latency와 parse 결과를 남긴다. Odyssey controller는 timeout, non-2xx와 응답 schema 오류를 명시적으로 처리한다.

## 6. Dependency 경계

한 기능의 구형 package가 다른 논문 기능까지 실행 불가능하게 만들지 않도록 설치·실행 환경을 역할별로 나눈다.

| Profile | 필수 기능 | 주 dependency | 조치 방향 |
|---|---|---|---|
| `executor` | Minecraft 연결, skill 실행, observation | Node 20.13.1, Mineflayer 4.25.0, minecraft-data, pathfinder, tool, collectblock, Express; Python requests/psutil | 현재 lock과 E0 회귀 유지. `/pause` 없는 경로를 기본화 |
| `controller-core` | planner/actor/critic orchestration, message/schema 처리 | Python, requests, coloredlogs | retrieval·launcher·provider SDK의 eager import 제거 |
| `retrieval` | description embedding, index persist/reload, top-k | sentence-transformers, Chroma, LangChain adapter | 신뢰받는 구현 유지. 지원 조합 고정 후 corpus 회귀 |
| `model-service` | MineMA inference endpoint | 별도 `LLM-Backend`의 torch/transformers/FastAPI stack | controller와 환경 분리 유지, model revision trace 추가 |
| `launcher` optional | 로컬 Minecraft client 실행 | minecraft-launcher-lib | headless/server 연구 core에서 lazy import |
| `provider` optional | 외부 hosted model | dashscope 등 | provider별 extra와 lazy import |
| `combat` optional | test environment와 multi-round combat | test mod/command와 combat fixture | 일반 executor와 분리 |
| `training` | MineMA fine-tuning | 별도 학습 requirements | runtime과 lock 공유 금지 |

## 7. Python requirement 감사

논문 기능에 필요한 package와 특정 실행 방식에만 필요한 package를 구분해, 무거움을 이유로 기능을 삭제하거나 선택 기능을 core에 강제하지 않게 한다. 이 표는 제거 결정이 아니라 현재 source의 직접 사용 여부를 기준으로 한 1차 분류다.

| Dependency | 코드상 역할 | 1차 분류 |
|---|---|---|
| `langchain`, `langchain_community` | legacy message type, embedding adapter, Chroma wrapper | 기준 tag에서 보존. modern profile은 `langchain-core` message와 공식 partner wrapper로 분리 |
| `langchain-huggingface`, `langchain-chroma` | modern embedding·Chroma adapter | clean-install과 기능 회귀를 통과한 기본 retrieval profile |
| legacy `chromadb==0.3.29` / modern `1.3.5` | skill/QA vector persistence와 search | 새 index 생성·reload 통과. 구 index migration 대신 고정 corpus에서 재생성 |
| `sentence-transformers` | description/query encoder | 논문 핵심 기능. checkpoint 고정 필요 |
| `javascript` | Python에서 Babel module 호출 | actor/raw-skill parser 경로. 대체 또는 격리 전 기능 회귀 필요 |
| `requests` | Mineflayer와 MineMA HTTP client | controller core 필수 |
| `gymnasium` | `VoyagerEnv` base/type | 현재 bridge 직접 의존. 필요 최소 범위 재검토 가능 |
| `psutil` | Node/client subprocess monitor | executor process 관리에 필요 |
| `minecraft_launcher_lib` | GUI client launcher | optional이지만 `bridge.py` import 시 현재 eager load |
| `dashscope` | hosted model provider | optional이지만 `llama.py`에서 현재 eager load |
| `coloredlogs` | logging | controller core 직접 사용 |
| `setuptools` | build/install | build dependency. requirements 중 중복 1회 제거 후보 |
| `tqdm`, `openai`, `chardet`, `cchardet`, `tiktoken` | Odyssey Python source에서 직접 사용을 확인하지 못함 | 미사용 후보. entrypoint와 packaging 전체 확인 뒤 결정 |
| `flufl.lock` | `file_utils.py` 특정 함수 내부 import | requirements에 없음. 해당 기능 optional화 또는 extra 선언 필요 |
| `@babel/core`, `@babel/generator` | actor와 raw-skill code parse/generation | Python 경로에서 require하지만 Node manifest에 없음. 누락 dependency |

기존 설치 환경의 `pip check`는 성공했지만 LangChain 0.2 계열, Chroma 0.3.29와 맞지 않는 PostHog 7.27.0 때문에 deprecated/telemetry warning이 발생했다. Modern profile은 Python 3.10 빈 환경 두 개에서 exact lock 설치와 `pip check`, encoder·index 생성·reload·검색을 통과했고 경고도 제거됐다. Legacy 대비 L2 score 최대 차이 `7.62939453125e-06`은 stochastic하지 않지만 후보 순서와 recall에 영향을 주지 않아 dependency 내부 수치 구현 차이로 기록했다.

## 8. 논문–코드 차이와 미해결 항목

논문·부록·공개 코드의 조건이 다른 항목은 연구자 결정을 먼저 기록하고, 구현자는 그 결정을 profile과 fixture로 고정한다.

### 연구자 결정 완료

1. **Retrieval k:** 본문 2.2는 top-5, 부록 C.3과 autonomous exploration 설명은 top-10이다. 연산 부담을 줄이기 위해 top-5를 기본 profile로 고정하고, top-10은 별도 profile로 보존한다.
2. **Encoder checkpoint:** 공개 config의 multilingual MiniLM을 modernized 재현 기준으로 사용한다. 이는 논문이 명시한 checkpoint가 아니라 공개 코드가 선택한 checkpoint다.
3. **Primitive 선행 정책:** 기존 caller의 `Vec3`, 공개 코드의 air/water 배치와 armor 순서를 유지한다. `killMob`이 drop 책임을 단독 소유하고, 실행 bot은 non-OP로 두며 관리자 작업은 server-host RCON으로 격리한다. 탐색은 episode seed 42의 재현 가능한 의사난수를 사용한다. Pathfinder goal은 다른 문제를 모두 처리한 뒤 판단한다.

### 남은 구현·검증 항목

1. **Primitive 40개 runtime 검증:** 40개 working manifest는 작성했다. Odyssey 추가 22개의 source상 contract 위험을 먼저 수정하고, Voyager 상속 18개를 포함한 interface별 실행 fixture를 통과해야 runtime manifest로 승격할 수 있다.
2. **Encoder 고정 `[x]`:** 공개 코드 encoder의 revision·checksum과 전처리·normalization을 manifest에 고정하고 CPU runtime fixture를 통과했다.
3. **Retrieval profile 회귀 `[x]`:** L2 기반 기본 top-5와 별도 top-10 모두 known-query recall `4/4`로 통과했고, fresh index와 별도 프로세스 reload의 후보 순서와 score가 일치했다.
4. **Retrieval wrapper migration `[x]`:** 공식 partner wrapper와 최종 lock은 두 clean 환경에서 통과했고 deprecated/telemetry warning도 제거됐다. Legacy–modern 후보 순서와 recall을 보존해 modernized 기본 profile로 승인했다.
5. **Dynamic skill lifecycle:** `Odyssey.learn`의 `add_new_skill` 호출은 주석 처리돼 있고 `generate_skill_description`은 초기화되지 않은 `self.llm`을 참조한다. 고정-library Odyssey baseline과 Voyager/Full profile을 분리한다.
6. **Actor validation:** substring match 뒤 실패 시 첫 skill을 선택하는 현재 동작은 논문의 exact program 선택 contract와 맞지 않는다.
7. **Critic 범위:** 일반 LLM critic 외에 crafting table/pickaxe/diamond만 처리하는 hard-coded subgoal verifier가 있다.
8. **Eager coupling:** `Odyssey` 생성만으로 environment, planner QA vector DB, retrieval DB, launcher/provider import가 함께 초기화된다.
9. **CWD 의존:** skill primitive와 sibling comprehensive library 경로가 `os.getcwd()`에 의존한다.

README의 Mineflayer 버전과 mod bundle 설명은 이번 감사에서 현재 lock 및 mod-free E0 증거에 맞춰 수정했다. Python `VoyagerEnv`의 `/pause`는 modernized 기본 no-op이고 `legacy_pause_adapter=True`를 명시한 과거 호환 profile에서만 사용한다.

## 9. 검증 순서

### 정적 감사 — 이번 단계 완료

- 논문 기능과 주요 Python/Node 진입점 연결
- corpus 파일 수와 compositional/JSON/description 대응 확인
- dependency 직접 사용, optional·누락·미사용 후보 분류
- contract 초안과 논문–코드 불일치 기록

### Offline 검증 — 진행 중

1. **Primitive 기능 고정 `[~]`:** 논문의 primitive 40개가 어느 함수·Mineflayer API에 대응하는지 working manifest를 작성했다. source상 contract 위험 수정과 runtime interface fixture는 남았다.
2. **Skill library 동일성 보장 `[x]`:** 183개 compositional skill과 자연어 description, 동기화된 runtime `skills.json`의 파일별 checksum을 기록하고 검증했다.
3. **Semantic encoder 고정 `[x]`:** 공개 코드 checkpoint의 revision·checksum과 전처리를 고정하고 실제 384차원 출력과 반복 오차 `0.0`을 확인했다.
4. **후보 검색 재현 `[x]`:** 183개 corpus와 네 known query에서 기본 top-5·별도 top-10을 통과했고, index를 별도 프로세스에서 다시 열어도 후보 순서와 score가 유지됐다.
5. **새 환경 설치 재현 `[~]`:** retrieval modern profile은 빈 환경 두 개에서 exact lock 설치·import·index reload를 통과하고 최종 승인됐다. 나머지 profile lock은 미완료다.

### Server 통합 검증 — 위 조건 이후

- MineMA actor가 retrieved candidate만 선택하는지 확인
- recursive prerequisite 실행과 observation/critic feedback 연결
- planner–actor–critic 대표 task와 failure recovery 반복

서버 실행은 위 interface와 dependency profile을 먼저 고정한 뒤 수행한다. legacy runtime 재실행이나 legacy 대비 latency 비교는 이 순서에 포함하지 않는다.
