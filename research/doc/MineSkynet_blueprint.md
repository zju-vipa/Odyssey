# MineSkynet 연구 블루프린트

최종 갱신: 2026-08-20
문서 역할: MineSkynet이 무엇을 연구하고, 어떤 시스템과 비교 실험으로 가설을 검증하는지 설명한다.

설치 명령은 [`research/README.md`](../README.md), 현재 순서는 [`milestone_index.md`](./milestone_goal/milestone_index.md), Odyssey 구현 근거는 [`paper_code_dependency_map.md`](./paper_code_dependency_map.md)를 따른다.

## 1. 한 문장 정의

MineSkynet은 성능이 서로 다른 물리 edge 장치의 Minecraft bot들을 중앙 coordinator가 능력에 맞게 배정·감독할 때, 단일 강한 agent나 단순 배정보다 유리해지는 조건을 찾는 연구다.

세 edge node는 한 모델의 연산을 나누는 worker가 아니다. 각 node는 공유 Minecraft 세계에서 독립된 avatar 하나를 제어하는 agent다.

## 2. 연구 질문과 가설

### 연구 질문

> 장치와 모델의 능력이 서로 다른 Minecraft agent들을 중앙 cloud-tier coordinator가 배정·감독하면, 성공률·완료 시간·비용·에너지 측면에서 어떤 task와 조건에서 이점 또는 손해가 발생하는가?

### 검증할 가설

1. agent별 성공률과 비용을 반영한 배정은 차이를 무시한 무작위·균등 배정보다 안정적이다.
2. 서로 독립적인 subtask는 여러 agent가 병렬 수행할 때 단일 agent보다 빨라질 수 있다.
3. 약한 local actor와 강한 cloud planner의 역할 분리는 모든 판단을 cloud에서 수행하는 방식보다 비용을 줄일 수 있다.
4. 통신·동기화·재시도 비용이 커지면 위 이점은 사라질 수 있다.

목표는 MineSkynet이 항상 우월하다고 주장하는 것이 아니다. 이득이 생기는 조건과 실패하는 조건을 함께 설명하는 것이 연구 결과다.

## 3. 연구 기반: Odyssey를 어떻게 사용하는가

### 논문 개념

Odyssey는 자연어 목표를 계획하고, 기존 skill을 의미 검색해 선택·실행한 뒤 관측 결과로 성공 여부를 판단한다. MineSkynet은 이 단일-agent 기능을 안정적인 연구 기반으로 사용한 뒤 여러 물리 agent의 배정 문제를 추가한다.

### 브랜치와 profile 역할

| 이름 | 연구에서의 역할 |
|---|---|
| `odyssey-legacy` / `master` | 논문·원본 코드·prompt·asset의 의미를 확인하는 source reference |
| `odyssey-modernized` | 동일한 논문 기능을 지원 가능한 dependency에서 실행하는 단일-agent baseline |
| `voyager-lifelong` | curriculum, code 생성·수정·검증과 능동 skill 축적을 보존하는 별도 baseline |
| `odyssey-full` | Odyssey에 Voyager식 능동 skill lifecycle을 결합한 확장 profile |
| `mineskynet-core` | modernized baseline에서 분기해 다중 agent 배정 가설을 검증하는 제안 시스템 |

modernization은 연구 기여가 아니라 안전한 실험 기반을 만드는 작업이다. legacy runtime과 속도를 경쟁시키지 않으며, 변경 후 논문 기능이 유지되는지를 현재 환경의 회귀로 확인한다.

### 보존하는 기능

- 40개 primitive와 183개 compositional skill
- 자연어 description과 Sentence Transformer 기반 semantic retrieval
- recursive prerequisite 실행
- MineMA actor의 candidate 선택
- planner–actor–critic, 실행 feedback과 재계획
- 논문의 task·prompt·성공 조건

Voyager의 능동 skill 생성·수정은 기본 Odyssey 재현과 섞지 않지만 삭제하지도 않는다. 별도 profile에서 재현해 MineSkynet scheduler 효과와 skill library 성장 효과를 분리한다.

## 4. 제안 시스템

### 한눈에 보는 구조

```text
공동 목표
   ↓
Global Orchestrator ── task 분해·agent 배정
   ↓                         ↑
Shared State Service ── 상태·inventory·진행 기록
   ↓                         ↑
Evaluator & Replanner ── 검증·재시도·재배정
   ↓
Edge Actor A / B / C ── 각자 skill 선택·Minecraft 실행
   ↓
공유 Minecraft world
```

### Global Orchestrator

논문 언어로는 장기 목표를 실행 가능한 subgoal로 바꾸는 planner에 해당한다. MineSkynet에서는 여기에 각 agent의 능력과 위치를 고려한 배정 기능을 추가한다.

- 공동 목표를 dependency가 있는 subtask로 분해한다.
- task별 예상 성공률, 시간, 이동·handoff 비용을 바탕으로 agent를 선택한다.
- 실행 중 상태가 바뀌면 남은 계획을 갱신한다.
- 배정 이유와 사용한 capability 값을 trace로 남긴다.

### Shared State Service

논문 언어로는 planner와 critic이 참고하는 environment state와 achievement history에 해당한다. 여러 agent가 서로 다른 상태를 보고하므로 하나의 권위 있는 기록으로 통합한다.

- agent 위치·inventory·현재 task와 heartbeat
- task dependency·담당 agent·진행 상태
- world observation과 item handoff
- model·skill·실행 결과의 revision과 timestamp

actor가 보고한 `SUCCESS`만으로 상태를 확정하지 않는다. inventory나 world-state 변화로 교차 검증한다.

### Evaluator & Replanner

논문 언어로는 critic, self-validation과 reflection에 해당한다. 실행 결과를 확인하고 같은 actor의 재시도, 다른 actor로의 재배정 또는 전체 재계획을 선택한다.

- 실행 오류와 task 실패를 구분한다.
- deterministic state check를 우선하고 필요한 경우에만 model critique를 사용한다.
- retry·reassign·replan의 이유와 비용을 기록한다.
- 반복 실패가 공유 상태를 오염시키지 않도록 task commit을 통제한다.

### Edge Actor Runtime

논문 언어로는 검색된 candidate 중 skill을 선택하고 Mineflayer로 실행하는 actor에 해당한다. edge actor는 허용된 skill 안에서만 행동하며 전역 계획을 임의로 바꾸지 않는다.

- 구조화된 atomic goal과 candidate skill을 받는다.
- 자신의 model 또는 rule로 정확한 skill ID를 선택한다.
- Mineflayer executor에 실행을 요청한다.
- observation, latency, resource usage와 오류를 반환한다.
- 확신이 낮거나 반복 실패하면 coordinator에 escalation한다.

## 5. 이기종 장치의 의미

현재 대상은 Raspberry Pi 4B 4GB, GTX 1050 Ti 장비와 RTX 3090 24GB 장비다. 정확한 역할은 미리 고정하지 않고 동일 atomic task의 측정 결과로 결정한다.

| 장치 유형 | 초기 예상 역할 | 연구에서 확인할 점 |
|---|---|---|
| Raspberry Pi | rule-based 또는 매우 제한된 actor | 약한 장치도 이동·운반 같은 task에 기여할 수 있는가 |
| GTX 1050 Ti | 소형·양자화 actor | 중간 난도 skill 선택과 비용 사이의 균형 |
| RTX 3090 | 강한 actor와 on-premise cloud proxy | planning·재계획 비용과 single-strong baseline |

local model은 자유 JavaScript 생성자가 아니라, 검색된 소수 skill 중 하나를 고르는 bounded actor부터 평가한다. 장기 계획, 전역 배정과 복잡한 code repair는 cloud-tier 또는 별도 Full Skill profile의 책임이다.

## 6. 공통 계약

### Task 계약

자연어 목표가 agent마다 다르게 해석되지 않도록 실행 task는 최소 다음 정보를 가진다.

```text
task_id, goal, dependencies, allowed_skills,
required/expected state, timeout, assigned_actor, revision
```

### 결과 계약

성공 메시지가 아니라 관측 증거로 task를 판정하기 위해 결과는 최소 다음 정보를 가진다.

```text
attempt_id, actor/model/skill revision,
before/after observation, status, failure_class,
latency, retry count, resource usage
```

### Capability 계약

scheduler가 막연한 “강한 장치/약한 장치”가 아니라 측정값으로 배정하도록 actor–task 조합별 성공률, 평균·P95 시간, memory/energy와 failure 유형을 기록한다.

## 7. 실험 설계

### 단계 A: 공통 기반 고정

MineSkynet 효과와 인프라 차이를 섞지 않기 위해 단일-agent Odyssey와 모든 비교군은 같은 `odyssey-modernized` executor·dependency·fixture를 사용한다.

### 단계 B: Atomic capability 측정

각 agent가 이동, log·stone 채집, item 운반·handoff, crafting table과 기본 도구 제작을 반복한다. 이 결과로 scheduler가 사용할 capability profile을 만든다.

### 단계 C: Cooperative task

병렬성과 dependency를 함께 포함한 축소 task를 사용한다.

- 여러 agent가 재료를 병렬 수집한 뒤 한 agent가 제작
- 서로 다른 위치의 재료를 chest 또는 담당 agent에게 전달
- 수집 → 운반 → 제작이 이어지는 wood-to-stone task

### 비교군

| 비교군 | 확인하는 질문 |
|---|---|
| Modernized Odyssey single agent | 다중 agent를 쓰지 않을 때의 기능 기준 |
| Single strong actor | 강한 장치 하나가 더 단순하고 빠른가 |
| Cloud-only | 모든 판단을 cloud가 할 때의 성공률과 비용 |
| Edge-only | 중앙 coordination 없이 local actor만으로 가능한가 |
| Random/uniform | 능력을 무시한 배정과 차이가 있는가 |
| Static roles | 사람이 고정한 역할보다 동적 배정이 나은가 |
| Capability-aware MineSkynet | 제안 배정 정책의 실제 이득과 손해 |

### 측정값

- team task success와 partial completion
- 전체 완료 시간과 subtask 평균·P95 latency
- cloud/API 비용과 local memory·energy
- 통신·동기화·item handoff 비용
- retry·timeout·reassign과 actor failure
- planning·retrieval·inference·execution·verification 시간 분해

orchestration overhead를 제외한 결과로 MineSkynet의 이득을 주장하지 않는다.

## 8. 범위와 후속 연구

현재 핵심 연구에는 visual pixel control, LHF, internal MoE 변경, 대규모 full fine-tuning, learned scheduler와 실행 중 임의 JavaScript 전역 배포를 포함하지 않는다. 이 기능들은 다중 agent 배정 효과와 섞이기 때문에 후속 연구 또는 별도 ablation으로 둔다.

능동 skill 학습은 범위에서 삭제한 것이 아니다. `voyager-lifelong`과 `odyssey-full`에서 보존하되, 기본 MineSkynet scheduler 실험에서는 registry를 읽기 전용으로 사용한다.

## 9. 성공과 실패의 해석

다음 결과가 나오면 제안 구조가 유효한 조건이 존재한다고 판단한다.

> Capability-aware 배정이 random/static 배정보다 높은 성공률 또는 짧은 완료 시간을 보이고, cloud-only보다 비용을 줄이며, coordination overhead를 포함한 뒤에도 유의미한 trade-off를 유지한다.

반대로 single strong actor가 항상 낫거나 약한 actor의 재시도 비용이 이득을 지우는 결과도 중요한 결론이다. 연구 논문은 어느 조건에서 각 결과가 나타났는지를 설명해야 한다.

## 10. 문서 경계

- 프로젝트 판단 원칙: [`PROMPT.md`](../PROMPT.md)
- 설치와 실행 명령: [`research/README.md`](../README.md)
- 현재 상태와 다음 순서: [`milestone_index.md`](./milestone_goal/milestone_index.md)
- Odyssey 재현 완료 조건: [`modernization_milestone.md`](./milestone_goal/modernization_milestone.md)
- MineSkynet 실험 단계: [`research_milestone.md`](./milestone_goal/research_milestone.md)
- 논문 기능과 구현 근거: [`paper_code_dependency_map.md`](./paper_code_dependency_map.md)
- 실행 계층 원시 증거: [`E0_test_evidence_2026-08-20.md`](./E0_test_evidence_2026-08-20.md)
