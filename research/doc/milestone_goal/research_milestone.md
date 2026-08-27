# MineSkynet 연구 마일스톤

최종 갱신: 2026-08-20

## 출발 조건

MineSkynet 구현은 완료·검증된 `odyssey-modernized` commit에서 분기한다. `master`의 구형 runtime은 연구 비교군이 아니라 원본 기능을 확인하는 source reference다. 실제 연구 baseline과 MineSkynet은 모두 같은 modernized dependency·executor 기반을 사용해 인프라 차이가 가설 검증을 교란하지 않게 한다. 하드웨어 조사와 benchmark 설계는 병렬로 준비할 수 있지만, `mineskynet-core` 결과 측정은 base commit이 고정된 뒤 시작한다.

## 연구 질문

> capability가 서로 다른 물리 edge 장치의 Minecraft actor들을 중앙 cloud-tier coordinator가 배정·감독하는 구조는 single-strong, cloud-only, edge-only와 고정·무작위 배정보다 어떤 task와 조건에서 성공률·완료 시간·비용의 이점을 갖는가?

연구 목표는 분산 구조가 항상 우월함을 보이는 것이 아니다. 통신·동기화·재시도와 orchestration overhead를 포함한 뒤에도 이점이 남는 조건과 그렇지 않은 조건을 찾는다.

## 연구 단계

### 연구 기반 고정 `[ ]`

MineSkynet의 효과만 비교할 수 있도록 모든 실험이 같은 modernized Odyssey와 task 조건에서 출발하게 한다.

- [ ] `odyssey-modernized` 완료 commit/tag와 재현 명령을 base로 지정
- [ ] modernized 단일-agent Odyssey와 MineSkynet 분산 기능의 변경 경계 표 작성
- [ ] 공통 task protocol, skill interface와 state/trace schema 확정
- [ ] task suite, world fixture, 반복 횟수와 통계 방법 사전 정의

완료 증거: 동일한 단일 actor task에서 modernized base와 `mineskynet-core`의 분산 기능 비활성 조건이 동등해야 한다.

### 세 물리 actor 연결 `[ ]`

세 장치가 공유 세계에서 서로의 bot 상태를 침범하지 않고 독립 agent로 행동하는지 확인한다.

- [ ] RTX 3090, GTX 1050 Ti, Raspberry Pi의 hardware/OS/runtime 기록
- [ ] Tailscale 연결, 시간 동기화와 actor별 독립 endpoint
- [ ] 각 장치가 별도 Mineflayer avatar와 read-only registry를 제어
- [ ] bot 세 개 동시 접속, 독립 실행, disconnect/reconnect 회귀

완료 증거: 한 actor의 reset·실패·재접속이 다른 actor의 bot과 상태를 덮어쓰지 않는다.

### Atomic capability 측정 `[ ]`

각 장치가 어떤 단순 task를 얼마나 안정적이고 빠르게 수행하는지 측정해 배정의 근거를 만든다.

- [ ] 공통 atomic task를 장치·모델·precision 조합별 반복 실행
- [ ] 성공률, 평균/P95 latency, RAM/VRAM, 에너지·온도 기록
- [ ] timeout, retry와 network 비용을 포함한 capability profile 생성
- [ ] QA accuracy가 아니라 실제 skill 선택과 Minecraft 결과를 사용

완료 증거: scheduler가 사용할 `P(success)`, latency, energy와 failure profile이 재현 가능하게 존재한다.

### Cloud-tier coordinator와 shared state `[ ]`

중앙 coordinator가 공동 목표를 나누고 여러 agent의 관측을 하나의 상태로 관리하며 실패를 다시 배정할 수 있는지 확인한다.

- [ ] structured subtask와 dependency DAG
- [ ] authoritative inventory/world/task state와 version 관리
- [ ] heartbeat, capability와 execution trace 수집
- [ ] deterministic validation, retry/reassign과 필요한 경우의 reflection/replan
- [ ] planner/API 호출 latency와 비용 기록

완료 증거: coordinator가 두 개 이상의 actor에 의존 task를 배정하고 관측된 상태를 근거로 완료·실패·재계획을 결정한다.

### Capability-aware allocation `[ ]`

측정된 agent 능력을 사용한 배정이 무작위·고정 역할보다 실제로 유리한 조건이 있는지 검증한다.

- [ ] capability, 이동, item handoff, 통신과 실패 비용을 반영한 정책
- [ ] uniform, random, fixed-role과 single-strong baseline
- [ ] cloud-only와 edge-only baseline
- [ ] timeout, network degradation과 actor failure 시 재할당
- [ ] decision trace와 counterfactual 비교

완료 증거: 같은 task graph와 fixture에서 정책별 결과를 반복 비교하고, 어느 조건에서 제안 정책이 유효하거나 무효한지 설명할 수 있다.

### 통합 평가와 논문 `[ ]`

성공률뿐 아니라 통신·재시도·에너지·비용을 포함해 제안 구조의 이득과 손해를 논문 주장에 연결한다.

- [ ] cooperative task suite를 난이도와 dependency 구조별로 구성
- [ ] 성공률, makespan, API 비용, local energy와 memory
- [ ] 통신, 동기화, retry와 orchestration overhead 분해
- [ ] network delay/loss와 node failure stress test
- [ ] confidence interval, effect size와 실패 사례 분석
- [ ] 주장–실험–ablation–원시 로그 연결
- [ ] 설치, lockfile, model revision, fixture와 공개 범위 정리

완료 증거: 제3자가 허용된 자산으로 핵심 표를 재현할 수 있고, 긍정·부정 결과 모두 연구 질문과 연결된다.

## 비교 기준

최소 비교군은 다음과 같다.

- modernized runtime의 Odyssey 단일-agent 기능 baseline
- 동일 runtime과 task를 사용하는 single strong actor
- cloud-only coordinator/actor
- edge-only actors
- uniform, random, fixed-role allocation
- capability-aware MineSkynet

구형 dependency로 실행한 `odyssey-legacy`는 필수 비교군이 아니다. 모든 핵심 비교군은 같은 modernized Minecraft·executor·dependency 기반을 사용한다. `voyager-lifelong`과 `odyssey-full`은 능동 skill lifecycle이 연구 결과에 미치는 영향을 볼 때 별도 축으로 비교하며, dynamic registry write를 기본 MineSkynet scheduler 효과와 섞지 않는다.

## 핵심 지표와 해석

- task success와 partial completion
- makespan과 평균/P95 subtask latency
- cloud/API 비용과 local energy
- peak RAM/VRAM과 장치 온도
- network traffic, synchronization과 handoff 비용
- retry, reassign, timeout과 actor failure rate
- planner·retrieval·inference·execution·verification별 시간 분해

MineSkynet의 이득은 coordination overhead를 제외한 수치로 주장하지 않는다. 성능 향상이 없거나 single strong actor가 더 나은 조건도 정식 결과로 기록한다.

## 연구 완료 조건

- 동일 modernized 기반의 단일-agent Odyssey와 MineSkynet 분산 기능 효과가 분리돼 있다.
- 각 핵심 가설에 직접 대응하는 baseline과 ablation이 있다.
- 이기종 배정의 이득과 손해가 task 및 system condition별로 설명된다.
- 결과가 commit, 환경, fixture, model revision과 원시 로그까지 추적 가능하다.
- 코드·문서·실험 package가 공개 가능한 범위에서 독립 재현 가능하다.
