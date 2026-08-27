# MineSkynet 연구 환경 안내

문서 역할: 처음 온 연구자에게 프로젝트의 목적과 검증된 실행 방법을 안내한다. 연구 판단이나 현재 작업 순서는 이 문서에서 중복 관리하지 않는다.

## 문서 읽는 순서

1. [AGENTS.md](AGENTS.md): 프로젝트 전체의 판단 원칙
2. [MineSkynet_blueprint.md](doc/MineSkynet_blueprint.md): 연구 질문, 제안 구조와 평가 방법
3. [milestone_index.md](doc/milestone_goal/milestone_index.md): 현재 상태와 바로 다음 단계
4. [modernization_milestone.md](doc/milestone_goal/modernization_milestone.md): Odyssey 재현·현대화 완료 조건
5. [research_milestone.md](doc/milestone_goal/research_milestone.md): modernized 기반의 MineSkynet 연구 단계

구현을 확인할 때만 [paper_code_dependency_map.md](doc/paper_code_dependency_map.md)를 보고, 실행 근거가 필요할 때는 [E0 증거](doc/E0_test_evidence_2026-08-20.md)로 내려간다. 누적 작업 보고는 [report_log.md](doc/report_log.md)에 보존하고, 교수님께 제시할 내용은 [labmeeting_temp.md](doc/labmeeting_temp.md)에서 선별·편집한다.

재현 자산은 다음 세 manifest에서 확인한다.

- [primitive 40 mapping](manifest/odyssey_primitive_40.json): 논문의 primitive가 현재 어느 함수·Mineflayer API contract에 대응하는지 기록
- [skill corpus checksum](manifest/odyssey_skill_corpus.sha256): compositional code 183개, description 183개와 runtime `skills.json`의 SHA-256 기록
- [semantic encoder contract](manifest/odyssey_semantic_encoder.json): 자연어를 vector로 바꾸는 checkpoint revision, artifact checksum과 변환 조건 기록

저장소 루트에서 다음 명령으로 형식과 파일 동일성을 확인할 수 있다.

```bash
jq '.counts, (.primitives | length)' research/manifest/odyssey_primitive_40.json
sha256sum --check --quiet research/manifest/odyssey_skill_corpus.sha256
Odyssey/.venv/bin/python Odyssey/scripts/semantic_encoder_fixture.py
```

아래 명령은 각 터미널에서 먼저 저장소 루트로 이동한 뒤 실행한다. 최초 진입 경로를 제외한 저장소 내부 경로는 상대경로로 표기한다.

```bash
cd ~/Documents/MineSkynet
```

## 1. 개요

MineSkynet은 서로 다른 연산 능력을 가진 물리 edge 장치들이 하나의 Minecraft 세계에서 협력하는 이기종 edge-cloud embodied multi-agent 연구다.

```text
                  MineSkynet Cloud-tier Mothership
        ┌──────────────────────────────────────────────┐
        │ Global Orchestrator                          │
        │ Shared State Service                         │
        │ Evaluator & Replanner                        │
        └──────────────────────┬───────────────────────┘
                               │ structured task protocol
                 ┌─────────────┼─────────────┐
                 │             │             │
          Raspberry Pi    GTX 1050 Ti    RTX 3090
          Edge Actor A    Edge Actor B   Edge Actor C
                 │             │             │
                 └─── Shared Minecraft World ───┘
```

최종 구조에서 각 edge node는 Odyssey의 actor와 Mineflayer skill executor 역할만 담당한다. 작업 분해, capability-aware 배정, 공유 상태, 평가와 재계획은 중앙 cloud-tier control plane으로 통합한다. 초기에는 실제 AWS 대신 RTX 3090 장비를 on-premise cloud proxy로 사용한다.

현재 먼저 달성하는 기준은 RTX 3090에서 원본 Odyssey의 기능적 baseline을 재현하는 것이다.

현재 검증된 범위:

- Minecraft 1.19.4 Fabric 서버 기동
- Mineflayer bot 접속과 observation 반환
- raw `mineWoodLog` skill 실행
- 나무 블록 파괴 후 `oak_log` 인벤토리 증가 확인
- MineMA-8B-v3 체크포인트 로드와 `llama3_8b_v3` endpoint 단일 추론
- 로컬 sentence-transformer 로드와 Odyssey skill top-k 검색
- primitive 40개의 논문–source working manifest와 compositional skill corpus 183개의 파일별 checksum

MineMA actor를 포함한 전체 Odyssey end-to-end 실행은 아직 진행 중이다.

## 2. 초기 설치

사전 조건은 Ubuntu 계열 Linux, Git으로 받은 본 저장소, 그리고 사용자 계정에 설치된 Miniconda/Conda다. 먼저 `conda --version`이 동작하는지 확인한다. Conda가 없다면 Miniconda를 설치한 뒤 새 terminal을 연다.

### 2.1 시스템 도구

Ubuntu 기준으로 Docker, Compose, npm과 기본 도구를 설치한다.

```bash
sudo apt-get update
sudo apt-get install -y docker.io docker-compose-v2 npm curl git
sudo usermod -aG docker "$USER"
```

Docker group 변경은 로그아웃 후 다시 로그인해야 적용된다. 재로그인 후 확인한다.

```bash
groups
docker ps
docker --version
docker compose version
npm --version
```

Docker group은 사실상 root 수준 권한을 제공하므로 신뢰된 연구 장비 사용자에게만 부여한다.

### 2.2 Conda와 Odyssey Python 환경

Odyssey Python 의존성은 system Python이나 Conda `base`에 설치하지 않고 저장소 내부 prefix로 격리한다.

```bash
cd ~/Documents/MineSkynet
conda create --prefix ./Odyssey/.venv python=3.10 pip -y
conda activate ./Odyssey/.venv

cd Odyssey
pip install -e .
```

프롬프트를 짧게 표시하려면 활성화된 환경에서 다음을 한 번 실행한다.

```bash
conda config --env --set env_prompt '(MineSkynet) '
conda deactivate
conda activate ./.venv
```

설치 결과를 확인한다.

```bash
python --version
which python
python -c "import odyssey; print('Odyssey import OK')"
```

예상 Python은 3.10이며 경로는 `Odyssey/.venv/bin/python`이다.

Conda가 Anaconda channel 이용약관 동의를 요구하면 사용자가 직접 다음을 실행한다.

```bash
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
```

### 2.3 Node.js 20과 Mineflayer 의존성

현재 `package-lock.json`은 Mineflayer 4.25.0과 관련 Prismarine dependency를 고정하며 Node.js 20.13.1, npm 10.5.2에서 E0 회귀를 통과했다. Node·Mineflayer·minecraft-data는 protocol/physics 동작이 함께 바뀔 수 있으므로 개별적으로 올리지 않고 lock 전체를 회귀한다.

`nvm`이 없다면 사용자 계정에 설치한다.

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.6/install.sh | bash
source ~/.bashrc
```

프로젝트의 `.nvmrc`를 이용해 Node 버전을 선택하고 로컬 npm 의존성을 설치한다.

```bash
cd ~/Documents/MineSkynet
cd Odyssey
nvm install
nvm use
node --version

cd odyssey/env/mineflayer
npm ci

cd mineflayer-collectblock
npx tsc

cd ..
npm install
```

`node --version`은 `v20.13.1`이어야 한다. npm package는 전역이 아니라 `Odyssey/odyssey/env/mineflayer/node_modules`에 설치된다.

### 2.4 MineMA LLM Backend Python 환경

MineMA를 서비스하는 LLM Backend는 Odyssey 환경과 의존성이 다르므로 별도의 Conda prefix를 사용한다. 기존 환경이 없다면 다음과 같이 만든다.

```bash
cd ~/Documents/MineSkynet
conda create --prefix ./LLM-Backend/.venv python=3.10 pip -y
conda activate ./LLM-Backend/.venv

cd LLM-Backend
pip install -r requirements.txt
```

GPU용 PyTorch가 정상 설치됐는지 확인한다.

```bash
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))"
```

`torch.cuda.is_available()`은 `True`여야 한다. Odyssey용 `Odyssey/.venv`와 Backend용 `LLM-Backend/.venv`에 서로의 requirements를 섞어 설치하지 않는다.

MineMA 체크포인트를 받은 뒤 `LLM-Backend/conf/config.json`을 다음 형태로 설정한다.

```json
{
  "CUDA_VISIBLE_DEVICES": "0",
  "models": {
    "llama3_8b_v3": "./models/MineMA-8B/MineMA-3-8b-v3"
  },
  "port": 9999
}
```

`models`의 key는 Odyssey가 요청하는 endpoint 이름과 동일한 `llama3_8b_v3`이어야 한다.

## 3. Docker와 Mineflayer 서버 설정

### 3.1 기본 mod-free executor와 optional legacy pause bundle

현재 modernized executor의 기본 조건은 다음과 같다.

- Minecraft 1.19.4
- Java 17
- Fabric Loader 0.15.11
- 외부 mod JAR 없음

이 조건에서 `/health`, `/start`, `/step`만 사용한 finite-position, 원목 채집과 작업대 제작 회귀를 통과했다. 따라서 `Odyssey/runtime/minecraft/mods`는 비어 있어도 된다.

기존 Python `VoyagerEnv`의 `/pause` 경로를 조사할 때만 다음 legacy bundle이 필요하다.

- Fabric API 0.87.2+1.19.4
- Multiplayer Server Pause 1.3.1
- iChunUtil 1.0.2
- CompleteConfig 2.3.1

optional JAR을 둘 디렉터리는 다음과 같다.

```bash
mkdir -p ./Odyssey/runtime/minecraft/mods
```

legacy pause 경로에서만 확인할 파일:

```text
Odyssey/runtime/minecraft/mods/
├── fabric-api-0.87.2+1.19.4.jar
├── MultiplayerServerPause-1.19.4-Fabric-1.3.1.jar
├── iChunUtil-1.19.4-Fabric-1.0.2.jar
└── completeconfig-2.3.1.jar
```

이 JAR들은 저장소에서 재배포하지 않으므로 필요할 때 각 mod의 공식 배포처에서 정확한 Minecraft 1.19.4 호환 버전을 받아야 한다. `runtime/`은 Minecraft world와 다운로드된 JAR을 포함하므로 Git에 커밋하지 않는다. `bridge.py`의 modernized 기본 경로는 pause adapter를 비활성화하며, `legacy_pause_adapter=True`를 명시한 과거 호환 profile에서만 `/pause`를 호출한다.

### 3.2 터미널 1: Minecraft 서버 실행

```bash
cd ~/Documents/MineSkynet
cd Odyssey
cp .env.example .env
# .env의 ODYSSEY_RCON_PASSWORD를 긴 임의 문자열로 교체한다.
docker compose up -d
docker compose ps
docker compose logs -f mc
```

modernized server의 `ops.json`은 비어 있어 실행 bot에 OP 권한을 주지 않는다. RCON port도 host에 publish하지 않으며, 비밀번호는 Git에서 제외된 `Odyssey/.env`를 통해 Minecraft container에만 전달한다. `gamemode`, `summon`, player 초기화와 같은 관리자 작업은 연구자·서버 호스트가 아래 RCON harness로 실행한다.

```bash
cd ~/Documents/MineSkynet
python3 Odyssey/scripts/host_admin_rcon.py prepare-player \
  --player bot --gamemode survival
python3 Odyssey/scripts/host_admin_rcon.py summon-near-player \
  --player bot --entity minecraft:cow
python3 Odyssey/scripts/host_admin_rcon.py command "time set day"
```

`command` 하위 명령은 임의 server command를 실행할 수 있으므로 agent나 생성 코드에 노출하지 않고 서버 호스트만 사용한다. 실행 bot이 수행하는 skill code는 `/`로 시작하는 chat을 거부하며, 서버의 비-OP 설정이 최종 권한 경계다.

성공하면 로그에 다음 형태가 나타난다.

```text
Done (...)! For help, type "help"
```

`docker compose logs -f mc` 화면은 `Ctrl+C`로 빠져나와도 서버가 계속 실행된다.

서버를 중지하거나 다시 시작하려면 다음을 사용한다.

```bash
cd ~/Documents/MineSkynet
cd Odyssey
docker compose stop mc
docker compose start mc
```

`docker compose down`은 container를 제거하므로 필요한 경우에만 사용한다. Minecraft world는 `Odyssey/runtime/minecraft/data`에 보존된다.

### 3.3 터미널 2: Mineflayer bridge 실행

새 터미널을 열어 Node 20을 선택한 뒤 bridge를 실행한다.

```bash
cd ~/Documents/MineSkynet
cd Odyssey/odyssey/env/mineflayer
source ~/.nvm/nvm.sh
nvm use 20.13.1
node --version
node index.js 3000
```

이 터미널은 Mineflayer bridge가 동작하는 동안 계속 열어 둔다.

### 3.4 터미널 3: MineMA LLM Backend 실행

새 터미널에서 Backend 전용 Conda 환경을 활성화하고 포그라운드로 실행한다. 이 방식은 model load, HTTP 요청 및 오류 로그를 터미널에서 바로 확인할 수 있다.

```bash
cd ~/Documents/MineSkynet
cd LLM-Backend
conda activate ./.venv
HF_HOME=./.cache/huggingface python main.py
```

MineMA-8B-v3 가중치를 RTX 3090에 올리는 동안 잠시 기다린다. 다음 로그가 나타나야 9999 포트에서 요청을 받을 준비가 된 것이다.

```text
Uvicorn running on http://0.0.0.0:9999
```

Backend 터미널은 테스트가 끝날 때까지 열어 둔다. 다른 터미널에서 상태를 확인한다.

```bash
curl --fail http://127.0.0.1:9999/ping
nvidia-smi
```

정상 응답:

```json
{"data":"pong!"}
```

MineMA 단일 추론까지 확인하려면 다음을 실행한다.

```bash
curl --fail -X POST http://127.0.0.1:9999/llama3_8b_v3 \
  -H 'Content-Type: application/json' \
  -d '{
    "system_prompt": "You are a Minecraft expert. Answer with only the item name.",
    "user_prompt": "Which tool is required to mine stone?"
  }'
```

응답의 `status`가 `0`이고 `data`가 비어 있지 않으면 정상이다. 현재 환경에서 확인한 응답 예시는 다음과 같다.

```json
{"status":0,"data":"Pickaxe"}
```

테스트 종료 후 이 터미널에서 `Ctrl+C`를 누르면 Backend가 종료되고 MineMA가 사용하던 VRAM이 해제된다. 종료 여부는 `nvidia-smi`로 확인한다.

### 3.5 터미널 4: bot 접속과 서비스 상태 확인

다른 터미널에서 Mineflayer bridge의 `/start` endpoint를 호출한다.

먼저 세 서비스가 준비됐는지 확인한다.

```bash
cd ~/Documents/MineSkynet
cd Odyssey
docker compose ps
curl --fail http://127.0.0.1:9999/ping
```

```bash
curl -X POST http://127.0.0.1:3000/start \
  -H 'Content-Type: application/json' \
  -d '{
    "host": "127.0.0.1",
    "port": 25565,
    "username": "bot",
    "waitTicks": 20,
    "reset": "soft"
  }'
```

Minecraft 로그에서 다음을 확인한다.

```text
bot joined the game
```

### 3.6 raw 나무 채굴 smoke test

bot 접속이 유지되는 상태에서 터미널 4에 다음을 실행한다.

```bash
cd ~/Documents/MineSkynet
cd Odyssey
conda activate ./.venv
python scripts/smoke_test_mine_wood.py
```

성공 예시:

```text
{
  "logs": {"oak_log": 1},
  "inventory": {"oak_log": 1}
}
PASS: mineWoodLog collected at least one wood log
```

단순히 `Wood log mined.`가 출력되는 것만으로는 충분하지 않다. 성공 기준은 실제 `*_log` 인벤토리 수량 증가다.

### 3.7 Primitive runtime online fixture

`goto`와 `getAnimal`의 실제 Minecraft 행동을 확인한다. 이 fixture에는 Minecraft server와 Mineflayer bridge만 필요하며 MineMA backend는 필요하지 않다. 먼저 3.2, 3.3, 3.5 절에 따라 server·bridge·bot을 준비한다.

서버를 사용하기 전에 `Vec3`, air/water 배치, armor 순서, 단일 drop 책임, non-OP profile과 seed 42의 선행 정책을 offline에서 확인할 수 있다.

```bash
cd ~/Documents/MineSkynet
node Odyssey/scripts/primitive_policy_offline.js
```

장애물이 없는 방향으로 6블록 이동하고 최종 위치가 목표 반경 2블록 안인지 확인한다.

```bash
cd ~/Documents/MineSkynet
python3 Odyssey/scripts/primitive_runtime_online.py goto --dx 6
```

`getAnimal`은 fixture 준비 명령과 primitive 실행을 분리한다. 아래 예시는 기존 cow를 정리하고 bot 근처에 cow 한 마리와 wheat를 준비한 뒤, 현재 위치에서 x축으로 8블록 떨어진 목표까지 유인한다.

```bash
cd ~/Documents/MineSkynet
python3 Odyssey/scripts/host_admin_rcon.py command \
  "execute at bot run kill @e[type=minecraft:cow,distance=..32]"
python3 Odyssey/scripts/host_admin_rcon.py command "give bot minecraft:wheat 1"
python3 Odyssey/scripts/host_admin_rcon.py summon-near-player \
  --player bot --entity minecraft:cow

python3 Odyssey/scripts/primitive_runtime_online.py get-animal --type cow --dx 8
```

통과 기준은 `GoalNear`와 동일하게 좌표를 내림한 block-grid에서 `goto`의 bot–target 거리가 2블록 이하이고, `getAnimal`은 같은 bot–target 조건과 cow–bot 실수 거리 4블록 이하를 만족하면서 `onError`가 없는 것이다. 따라서 block-grid 기준을 만족하면 bot 중심과 실수 target 사이의 출력 거리(`bot_distance_to_target`)는 2를 조금 넘을 수 있으며, 실제 판정값은 `bot_block_distance_to_target`이다. 지형 때문에 경로가 막히면 실패를 성공으로 바꾸지 말고, 열린 방향에 맞춰 `--dx`, `--dy`, `--dz`만 조정해 다시 실행한다. 실행이 끝나면 필요에 따라 다음 명령으로 cow를 정리한다.

```bash
cd ~/Documents/MineSkynet
python3 Odyssey/scripts/host_admin_rcon.py command \
  "execute at bot run kill @e[type=minecraft:cow,distance=..32]"
```

### 3.8 Semantic encoder contract fixture

자연어 subgoal과 skill description이 동일한 공개 코드 checkpoint와 전처리 조건으로 384차원 vector가 되는지 확인한다. Minecraft server, Mineflayer bridge와 MineMA backend는 필요하지 않다.

다음 정적 검사는 checkpoint revision, canonical model·tokenizer artifact checksum, max sequence length와 pooling 설정을 확인하며 model inference는 수행하지 않는다.

```bash
cd ~/Documents/MineSkynet
Odyssey/.venv/bin/python Odyssey/scripts/semantic_encoder_fixture.py
```

정적 검사가 통과한 뒤 다음 명령으로 CPU에서 실제 embedding shape, 유한값, 반복 오차와 newline 전처리를 확인한다. 이 실행은 local checkpoint만 사용하며 검색 순위나 retrieval 품질까지 검증하지 않는다.

```bash
cd ~/Documents/MineSkynet
Odyssey/.venv/bin/python Odyssey/scripts/semantic_encoder_fixture.py --run-model --device cpu
```

성공하면 마지막 줄에 `PASS: semantic encoder contract fixture`가 출력된다. 전체 JSON 출력은 runtime manifest의 관찰값과 지원 dependency 조합을 확정하는 근거로 사용한다.

다음 smoke는 같은 encoder로 183개 skill description을 indexing하고 영어·한국어 known query의 top-5 candidate와 L2 score를 출력한다.

```bash
cd ~/Documents/MineSkynet
Odyssey/.venv/bin/python Odyssey/scripts/semantic_retrieval_smoke.py
```

2026-08-27 CPU 실행에서는 183개가 모두 index에 들어갔고 네 query의 기대 skill이 모두 rank 1로 반환돼 recall@5 `4/4`를 기록했다. 원시 candidate와 score는 [실행 로그](log/semantic_retrieval_smoke_2026-08-27.json)에 남겼다.

다음 정식 fixture는 top-5를 기본 profile, top-10을 별도 profile로 실행한다. fresh index를 만든 뒤 별도 프로세스에서 저장 index를 다시 열어, candidate 순서와 L2 score가 유지되는지도 함께 검사한다.

```bash
cd ~/Documents/MineSkynet
Odyssey/.venv/bin/python Odyssey/scripts/semantic_retrieval_fixture.py
```

2026-08-27 CPU 실행에서 두 profile 모두 네 query의 기대 skill을 포함해 recall@5·recall@10 `4/4`를 기록했다. fresh index와 reload의 모든 후보 순서가 같았고 최대 score 차이는 `0.0`이었다. top-10 전체 후보와 score, reload 비교 결과는 [profile 실행 로그](log/semantic_retrieval_profiles_2026-08-27.json)에 고정했다.

### 3.9 Modern retrieval wrapper profile

기존 검증 환경을 변경하지 않고 `langchain-huggingface`·`langchain-chroma` 조합을 확인하려면 비어 있는 Python 3.10 환경을 사용한다. 아래 경로가 이미 존재한다면 덮어쓰지 말고 다른 빈 임시 경로를 선택한다.

```bash
cd ~/Documents/MineSkynet
Odyssey/.venv/bin/python -m venv /tmp/odyssey-retrieval-modern
/tmp/odyssey-retrieval-modern/bin/python -m pip install --upgrade pip
/tmp/odyssey-retrieval-modern/bin/python -m pip install \
  --index-url https://download.pytorch.org/whl/cpu \
  torch==2.13.0
/tmp/odyssey-retrieval-modern/bin/python -m pip install \
  -r Odyssey/requirements-retrieval-modern.lock.txt
/tmp/odyssey-retrieval-modern/bin/python -m pip check
```

이 lock은 서로 다른 두 빈 환경에서 재설치한 최종 retrieval lock이다. 설치 뒤 다음 명령으로 encoder와 신규 wrapper 자체의 index 생성·reload·검색 contract를 확인한다.

```bash
/tmp/odyssey-retrieval-modern/bin/python \
  Odyssey/scripts/semantic_encoder_fixture.py \
  --run-model --device cpu --wrapper-profile modern-partner
/tmp/odyssey-retrieval-modern/bin/python \
  Odyssey/scripts/semantic_retrieval_fixture.py \
  --wrapper-profile modern-partner --summary-only
```

2026-08-27에는 서로 다른 빈 환경 두 개에서 설치와 `pip check`를 통과했고, encoder checksum과 top-5·top-10 fresh/reload fixture도 통과했다. deprecated wrapper와 telemetry 경고는 출력되지 않았다. 결과는 [migration 실행 로그](log/retrieval_wrapper_migration_2026-08-27.json)에 기록했다.

다음 비교 명령은 과거 wrapper의 후보·score와 직접 대조한다.

```bash
/tmp/odyssey-retrieval-modern/bin/python \
  Odyssey/scripts/semantic_retrieval_fixture.py \
  --wrapper-profile modern-partner \
  --baseline-evidence research/log/semantic_retrieval_profiles_2026-08-27.json \
  --summary-only
```

후보 순서는 전부 같고 비교 명령은 통과한다. Legacy 대비 L2 score 최대 차이 `7.62939453125e-06`은 stochastic하지 않지만 후보 순서와 recall에 영향을 주지 않는 dependency 내부 수치 구현 차이로 기록한다. Wrapper 간 raw score의 임시 절대 허용값은 병합 기준으로 사용하지 않으며, 동일 modern profile의 fresh/reload score 동일성과 실제 top-k 결과를 회귀 기준으로 사용한다.

## 알려진 주의사항

- 서버의 offline/insecure mode 경고는 로컬 Mineflayer 연구 환경에서는 예상된 메시지다.
- `entity.objectType is deprecated` trace는 현재 기능을 막지 않는 구 Mineflayer 경고다.
- Node.js 22에서 이동 packet 오류가 발생했으므로 Mineflayer 터미널은 Node.js 20.13.1을 사용한다.
- `npm audit fix --force`는 호환 버전을 깨뜨릴 수 있으므로 실행하지 않는다.
- Mineflayer `/step`은 JavaScript를 실행하므로 public internet에 노출하지 않는다.
- MineMA Backend는 현재 bf16으로 약 15.8 GiB VRAM을 사용한다. 테스트 중에는 같은 GPU의 다른 대형 모델 서비스를 함께 띄우지 않는다.
- 포그라운드 서비스 실행 터미널 세 개(Minecraft 로그, Mineflayer, MineMA)를 유지하고, 네 번째 터미널에서 `curl`과 Odyssey 테스트를 실행하면 로그 원인을 구분하기 쉽다.
