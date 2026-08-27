# MineSkynet 마일스톤 인덱스

최종 갱신: 2026-08-27

## 방향

이 프로젝트의 우선 목표는 작은 대체 시스템을 순서대로 완성하는 것이 아니다.

> 원본 논문의 핵심 기능을 보존하면서, 구형 의존성에 묶이지 않는 안전하고 반복 가능한 실행환경에서 Odyssey를 재현한다.

현대화는 별도의 연구 주제가 아니라 MineSkynet 가설을 검증하기 위한 신뢰 가능한 기반을 만드는 일이다. 완료 여부는 다음 세 가지로 판단한다.

1. 논문의 기능과 공개 코드·model·skill·prompt 사이의 대응 관계
2. 지원 가능한 dependency lock과 격리된 실행 profile의 clean install 결과
3. modernized 환경에서 핵심 기능, 오류 처리와 복구 경로의 반복 회귀 결과

구형 runtime을 다시 실행해 modernized와 속도·성공률을 비교하는 것은 필수 조건이 아니다. 교체 이유는 source code, dependency 지원 상태, 기존 오류 기록과 현재 회귀로 설명하면 충분하다.

## 브랜치와 책임

| 브랜치 | 역할 | 원칙 |
|---|---|---|
| `master` | `odyssey-legacy` | 원본 코드와 논문 기능을 확인하는 참조점. 구형 runtime 성능을 다시 측정하기 위한 실험군은 아니다. |
| `experiment/odyssey-modernized` | `odyssey-modernized` | 논문 기능을 지원 가능한 의존성과 명시적 service/profile 경계에서 안정적으로 실행하는 연구 기반이다. |
| `mineskynet-core` | MineSkynet 연구 구현 | 검증 완료된 modernized commit을 base로 만든다. 분산 실행과 연구 기여는 여기서 추가한다. |

`experiment/e1-stub`의 하네스·문서 변경은 `234238d`에서 modernized에 병합됐다. stub controller는 독립 연구 목표가 아니라 service boundary, parser, 오류 분류를 검사할 필요가 있을 때만 사용하는 test harness다.

## 문서 구성

- 판단 원칙: [`AGENTS.md`](../../AGENTS.md)
- 연구 질문과 제안 구조: [`MineSkynet_blueprint.md`](../MineSkynet_blueprint.md)
- [Odyssey 재현과 현대화 마일스톤](./modernization_milestone.md): 논문 기능을 안전한 환경에서 실행하기 위한 현재 작업
- [MineSkynet 연구 마일스톤](./research_milestone.md): modernized Odyssey 이후의 이기종 edge-cloud 실험
- [논문–코드–의존성 대응표](../paper_code_dependency_map.md): 구현 판단이 필요할 때 내려가 보는 기술 근거
- 실행 환경과 명령: [`research/README.md`](../../README.md)
- 과거 진단·실행 증거와 현재 작업 보고: [`report_log.md`](../report_log.md)

처음 읽는 사람은 원칙 → 블루프린트 → 이 인덱스 순서만 보면 된다. 구현 세부사항과 원시 증거는 판단 근거가 필요할 때만 내려가 읽는다. 과거 E0~E4는 진단 이름이며, 현재 작업 순서와 완료 판단은 이 인덱스와 두 마일스톤 문서만 기준으로 한다.

## 현재 상태

- [x] modernized 실행 계층에서 Minecraft 1.19.4, Mineflayer bridge, `mineWoodLog`, `craftCraftingTable`의 hard-reset 회귀를 각각 10/10 통과했다.
- [x] `/pause` 없이 mod-free server에서 정상·failure-path 회귀와 실행 증거 저장을 확인했다.
- [x] E0 변경은 `a157205` (`E0 finished`)에 커밋됐다.
- [x] `a157205`를 `odyssey-modernized-executor-1.19.4` annotated tag로 로컬·원격에 고정했다. 이 tag는 실행 계층 baseline이며 Odyssey 전체 재현 완료를 뜻하지 않는다.
- [x] `234238d`에서 E1 하네스, 문서 재편과 retrieval 정책을 `experiment/odyssey-modernized`에 병합했다.
- [x] 논문 기능을 공개 코드, model/service와 dependency profile에 1차 대응하고 contract 및 불일치를 문서화했다.
- [~] primitive 40개의 논문–source working manifest를 작성했다. Odyssey 추가 22개는 source와 대응하지만 Voyager 상속 18개의 runtime fixture와 확인된 contract 위험 수정은 남았다.
- [x] compositional code·JSON entry·description 183개를 동기화하고 파일별 checksum을 고정했다. code가 없는 `killOnePlayer.txt`는 기본 corpus에서 제외했다.
- [x] 공개 코드 Sentence Transformer의 revision·변환 조건과 CPU 출력을 고정했다. 183개 corpus의 기본 top-5와 별도 top-10은 known-query recall `4/4`를 기록했고, fresh index와 별도 프로세스 reload의 후보 순서·score가 일치했다.
- [ ] MineMA actor, recursive prerequisite, planner–actor–critic을 포함한 Odyssey end-to-end baseline은 아직 재현되지 않았다.
- [ ] 논문 핵심 기능 전체를 실행하는 `odyssey-modernized` 완료 commit과 clean-install 회귀는 아직 없다.
- [ ] `mineskynet-core` 브랜치는 modernized 완료 뒤 생성한다.

## 전체 흐름

```text
Odyssey 논문·공개 코드 대응표
    → 구형·optional dependency와 결합 지점 감사
    → 지원 가능한 lockfile과 격리 profile 구성
    → odyssey-modernized에서 논문 기능과 복구 회귀 검증
    → modernized 완료 commit/tag 고정
    → mineskynet-core 분기
    → 이기종 edge-cloud 가설 검증
```

`master`의 구형 환경을 먼저 실행할 필요는 없다. 다만 modernized 변경이 어떤 source/dependency 결합을 해소했는지와 어떤 논문 기능을 보존해야 하는지는 기록한다. 변경 뒤에는 해당 기능과 이전 회귀를 현재 지원 환경에서 확인해 원본 알고리즘을 새로운 동작으로 조용히 바꾸지 않는다.

## 공통 기록 규칙

모든 재현·연구 실행은 commit, branch/profile, dependency lock, model·encoder revision, Minecraft version, world fixture/seed, task, 반복 횟수, 성공 조건, 오류와 원시 로그 경로를 기록한다. 운영 latency는 modernized 환경의 용량 계획과 연구 실험에 기록하되 구형 runtime과의 성능 경쟁 지표로 사용하지 않는다. 성공 메시지가 아니라 inventory 또는 world-state 변화로 실행 성공을 판정한다.
