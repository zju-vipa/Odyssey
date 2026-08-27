# 7.27 랩미팅

> 문서 역할: [`report_log.md`](./report_log.md)에 누적된 작업 보고와 날짜별 논의를 선별·다듬어 교수님께 보고하기 위한 임시 문서다. 현재 목표와 완료 조건은 [`milestone_index.md`](./milestone_goal/milestone_index.md), 연구 원칙은 [`AGENTS.md`](../AGENTS.md)를 따르며, 아래 과거 표현은 당시 맥락 보존을 위해 임의로 고치지 않는다.
- ODYSSEY: Empowering Minecraft Agents with Open-World Skills
    - 문제 의식 : 많은 마크 에이전트 연구들이 테크트리(다이아 얻기 등)을 따르도록 설계됨. 이는 LLM의 능력을 제한함
    - 핵심 구성요소
        1) 40개의 primitive skill, 183개의 compositional skill로 구성된 스킬 라이브러리
            - primitive skill : Mineflayer JavaScript API를 그대로 조작하는 가장 기본적인 스킬들
                - 32개 operational skill : foundational interface with parameterized input (mine(), craft() 등)
                - 8개 spatial skill : 정밀한 포지셔닝, 방향 탐색(orientation) <- 시각 인풋의 부재 때문에 spatial 필수적
            - compositonal skill : 스킬라이브러리 함수들을 재귀적 방식을 통해 구현 -> 복잡한 태스크를 선행조건 함수들을 달성하는 식으로 분해
            - 효율적인 스킬 검색(retrival)을 위해 각 스킬에 대한 설명을 LLM을 통해 텍스트로 생성한 뒤 sentence transformer를 통해 텍스트 정보를 벡터 표현으로 변환.
            - planner-actor-critic 아키텍처 :
                - planner : 포괄적인 계획 생성. 장기 목표 달성을 위해 세부적인 서브 목표들로 분해. 플래너의 인풋 프롬프트는 다음으로 구성
                    1) 궁극적 목표와 행동 제약(<- 태스크는 현 인벤토리에서 가능할 때만 제안하라 등)
                    2) 에이전트 상태 (에이전트와 환경 사이의 상호작용; 배고픔, 체력 등)
                    3) 에이전트의 달성 (현 인벤토리/ 얻은 장비 등)
                - actor : 서브 골을 달성하기 위해 실행 가능한 스킬을 다음과 같이 탐색
                    1) 맥락 쿼리 : 플래너에 의해 생성된 텍스트 기반 서브 골은 sentence transformer에 의해 벡터로 표현
                    2) 유사도 매칭 : 벡터 유사도(내부적으로 코사인/유클리드 등 모름)을 통해 스킬 설명과 서브골 간 유사도 비교
                    3) 스킬 선택 : top-5 유사 스킬중 가장 높은것 택
                - critic : 경험을 문서화 하는 것이 중요. 초기 실행 에러를 일으킬 수 있는 초기 플랜 불일치를 교정하는 피드백-공지 시스템 구축. -> 예상 결과와 실제 결과를 비교 하므로써. 피드백은 세 타입으로 나뉨
                    1) excution feedback : 스킬 실행에 대한 진행 사항을 포착. 성공 여부+ 실패시 가이드라인
                    2) self validation : 인벤토리 변화를 추적해 간단히 성공 여부 추적
                    3) self reflection : 현재 에이전트와 환경에 상태를 평가하여 실패의 원인을 추론
        2) 마크 위키의 QnA로 파인튜닝한 MineMA : LLaMA 3를 마인크래프트 위키에서 추출한 데이터를 통해 도메인 특화 모델로 만듬
            - 데이터셋 생성 : GPT를 통해 마인크래프트 위키에서 크롤링한 데이터를 QnA 쌍으로 가공
            - 모델 파인튜닝 : LoRA를 써 하위랭크 행렬을 학습시킴
            - 모델 평가 : GPT4를 통해 다지선다 질문(multiple choice question)을 통해 마크에 대한 도메인 특화 모델이 되었는지 평가
        3) 모델 잠재력 벤치마크
            - long term planning task : 여러개의 전투 시나리오; 무기와 장비를 만들고 전투. 싱글타입과 멀티타입 몬스터로 나뉨. -> 기준은 남은 체력과 시간으로 측정. 각 전투후 반복적으로 에이전트 최적화
            - Dynamic-immediate planning task : 즉각적으로 환경 피드백이 있는 경우 동적으로 생성하고 계획을 싱행하는걸 평가. -> 여러 파밍 시나리오; 실시간 환경에서의 평가
            - autonomous exploration task : 다음 목표와 적절한 스킬을 고르는 능력 평가. 자원을 찾고, 활용하고, 예상치 못한 상황에 적응하는 능력.
    - ablation study : 플래너와 스킬 라이브러리가 각각 필수적 요소. 하나라도 빠지면 심각한 성능저하.
    - 한계 : 오픈소스 LLM은 할루시네이션이 쉽다. 이를 방지하기 위해 RAG 도입을 고려중. 현재 텍스트 기반 LLM에 초점을 맞춰, 시각적 요소는 거의 배제되었다.



# 7.30 랩미팅
1) 프레임워크 계획 요약
    - 핵심 연구 질문 : 통합 cloud-tier orchestrator가 연산 성능과 local LLM 능력이 서로 다른 Minecraft bot drone들에게 subtask를 적절히 배정하는 구조는 cloud-only, local-only 또는 고정 역할 방식보다 낮은 비용으로 유사하거나 더 높은 협력 task 성공률을 달성할 수 있는가?
        - 핵심 가설
            1. 복잡한 계획만 cloud-tier mothership에 맡기고 실행은 edge drone가 담당하면 cloud-only 방식보다 API 비용을 줄일 수 있다.
            2. agent별 수행 능력을 고려한 task allocation은 agent 차이를 무시한 균등·무작위 배정보다 성공률과 완료 시간을 개선한다.
            3. 병렬화 가능한 subtask를 여러 drone에 배정하면 강한 단일 agent보다 전체 task 완료 시간이 감소한다.
            4. planning, communication, state synchronization 비용을 모두 포함한 뒤에도 일정 조건에서는 edge-cloud 협력의 이득이 남는다.
    - 보유 자원/장비 및 역할
        - (빌리저 에이전트 논문 설명)
        - (오케스트레이터-엣지 프레임워크 구조도)
            - Raspberry Pi: raspberry pi 4b (4gb ram)
            - GTX 1050 Ti 컴퓨터: vram 4gb; cpu/ram 차후 확인
            - RTX 3090 컴퓨터: VRAM 24GB, 현재 주 개발 장비
            - 외부 cloud LLM API: 고난도 계획과 재계획에 제한적으로 사용 (3090에 통합 고려중; vram, ram 용량 넉넉)
    - drone(기존 오딧세이 actor) 대안 LLM모델
        - 기존 llama 3 8b를 기반으로 파인튜닝한 MineMA는 저사양 노드에 올릴 수 없으므로 gemma 3 1B 모델을 기반으로 LoRA를 통해 파인튜닝한다 (훈련 데이터셋은 허깅페이스에 공유됨)
        - 극한으로 양자화 걸면 양자화 수준 INT4, 컨텍스트 윈도우 8k 기준 vram 1.84gb. (axpml 사진)
    - 네트워킹 방법
        - tailscale을 통해 번거로운 포트포워딩/공인IP 또는 같은 공유기 내 연결 강제 문제 우회
        - 일종의 VPN. 설치후 작동시 타 라우터/공유기 환경 내에서도 잘 동작
        - 당연히 진지한 기여로 포장X.
2) 현재 진행상황 요약
    1) 자바 버전 이슈와 nvm 이슈 해결
    2) mineflyer을 통해 cli 환경으로 나무 1개 채굴 테스트 성공
    3) 오딧세이 actor 재현을 위해 MineMA 다운로드 진행중
3) 추후 계획
    - mineMA까지 포함된 온전한 상태에서 나무 채굴 테스트, 작업대 제작 테스트 확인
    - drone 모델로 llama3/mineMA가 아닌 gemma 3 1b로 교체 가능한지 여부; 교체후 똑같이 나무-작업대 테스트

# 8.6 랩미팅

1) 현재 진행상황
- 프로젝트에서 의존성 이슈가 너무 많아 보수 코드를 계속 짜는 것 보다 차라리 의존성 최신화 -> 이후 최신화된 버전 기준으로 보수 코드 패치 방향으로 결정
    - 단, 조금 진행하다가 LoRA를 먼저 해보고 싶다는 생각에 연구 순서상으론 약간 다음인 파인튜닝 먼저 진행
- 허깅페이스에서 데이터셋과 gemma 3 1b 다운로드
- json 포맷에서 NaN은 읽히지 않아 전처리 필요. 또한 중복 데이터들이 있어 preprocessing.ipynb 생성
- 전처리용 가상환경/커널 세팅; 학습 전용 콘다환경 세팅
- train_row를 달리하며 128, 128 과적합(train_row=128,eval_row=128), 1k, 10k로 달리하며 파인튜닝 수행
    - '제작대에 필요한 나무 판자 수는?' (정답 4개)에 대해 과적합, 1k는 통과; 나머지 128과 10k는 실패함
    - 단일 질문 테스트이므로 확정할 순 없지만, 학습 규모에 따라 일관되게 성능향상은 가지지 않는 것으로 보임
    - 다만 오딧세이의 mineMA 활용이 실제로 작업을 수행하는 actor 뿐만이 아닌, planner, reflector 등 여러 부분에서 쓰인다는 점. 그리고 현재 프로젝트 구상안은 actor 노드에겐 고도의 추론과 계획보단 매우 파편화된 subgoal에 대해 적절한 skill 선택을 주력으로 한다는 점에서 아쉬운 추론성능이 발목을 잡을지는 미지수.
        - 따라서 도메인 특화 모델을 actor용 1b 기반, 도메인 지식/추론용으론 더 크고 똑똑한 모델 이런식으로 병행하는게 필요해보임
        - 오딧세이의 in-context적 요소 또한 actor에게 기대하기보단 planner의 task allocation의 품질을 적응 시키는 방식으로 기대중
{
  "run_profile": "memorize_128",
  "prompt": "In Minecraft, how many wooden planks are required to craft a crafting table?",
  "expected_factual_answer": "4 wooden planks",
  "base_answer": "You need **6** wooden planks to craft a crafting table in Minecraft. \n\n(1 wood plank x 6 = 6 planks)",
  "adapter_answer": "The crafting table requires 4 wooden planks to craft it in Minecraft.",
  "reload_inference_peak_vram_gib": 1.976
}

{
  "run_profile": "pilot_1k",
  "prompt": "In Minecraft, how many wooden planks are required to craft a crafting table?",
  "expected_factual_answer": "4 wooden planks",
  "base_answer": "You need **6** wooden planks to craft a crafting table in Minecraft. \n\n(1 wood plank x 6 = 6 planks)",
  "adapter_answer": "To craft a crafting table in Minecraft, you need 4 wooden planks.",
  "reload_inference_peak_vram_gib": 2.028
}
2) 다음 계획
- INT4로 배포 후 BF16과의 출력정확도, 지연, peak vram을 비교
- 오딧세이 actor adapter의 엔드포인트 설정
- 현 작업 완료시 다시 의존성 현대화 작업 진행
3) 피드백


# 8.20 랩미팅
1) 환경 재현 관련 이슈들
    - 추가적인 실험이나 구현 전에 일단 환경 세팅부터 최우선적으로 하는 방식을 선택. 좀 게으른 방식이긴 하지만 추론수준을 최고로 당기고 프로젝트를 탐색시킨 다음 보고서를 작성 -> 작성된 보고서에서 의존성들을 세가지 클래스로 나눔. 나누는 기준은 오딧세이 실험 재현에 필요한 최소기능인가? 따라서 브랜치 상으로 다음으로 관리
        1) odyssey-modernization : 의존성 이슈가 많은 구형 오딧세이에 대해 의존성이 취약한 부분은 대체/삭제/업데이트/보강. 목표는 구형 코드의 기능 재현하면서 의존성 이슈로부터 튼튼하게
        2) mineskynet-core : 1) 이 완료된 후 이 위에 추가적인 제안을 더 붙일것 (다중에이전트 등)
        3) odyssey-legacy : 구형 오딧세이. 브랜치상 master에서 관리
    - 챗봇이 목표를 과도해석하거나 프로젝트 본질에 맞지 않는 경우를 제한하기 위해 일종의 하네스? 구조 도입. 도입 계기는 오딧세이 현대화중, 현대화 작업 자체가 너무 과도하게 분석의 대상이 되고, 세부 목표가 과도하게 세분화되며 늘어지는 경향을 포착. 또한 챗봇과 작성한 문서에 대한 소비자를 다음과 같이 나눴을 때 (1) 1차 연구자 (저, 연구를 수행하는 당사자). (2) 2차 연구자 (교수님/동료 학연생 같이 피드백/코워커) (3) 프로젝트를 모르는 제 3자 로 나눴을 때 (2),(3)은 고사하고 (1)도 챗봇의 분석이나 문서를 따라가지 못한다고 파악. PROMPT.md에 반영
        - 경험적으로는 해당 하네스 도입 이후 논문-구현 간 일대일 대응이 훨씬 명료하고 챗봇도 실제 구현이나 너무 기술적으로 빠져들지 않고 논문에서의 언어를 사용하여 정보를 받는 입장에서 훨씬 간결하다고 느낌.
2) 실제 완료 항목
    ### 논문–코드–dependency 대응 `[~]`

    논문이 설명한 각 기능이 현재 어느 코드와 model에 의해 수행되는지 연결해, dependency를 바꿔도 연구 기능을 잃지 않게 한다.

    - [x] 논문의 각 기능을 source file, dependency, model과 input/output에 연결
    - [~] task, prompt, primitive 40 manifest, 183 skill corpus와 checkpoint 출처·hash 고정
    - [x] dependency를 core, executor, retrieval, model, combat, training으로 1차 분류
    - [ ] 각 profile의 지원 버전, lockfile과 clean-install 절차 작성
    - [~] license, 보안 경고, deprecated API와 유지보수 상태 기록
    - [x] branch 역할과 범위 기반 tag 정책 확정

    세부 근거와 미해결 조건은 [`paper_code_dependency_map.md`](../paper_code_dependency_map.md)에 기록했다. primitive 40개의 논문–source working manifest와 compositional code·description 183쌍의 checksum을 고정했다. Voyager 상속 primitive 18개의 runtime interface fixture, source상 contract 위험의 수정·검증, encoder revision·전처리, retrieval 결과와 clean-install lock은 후속 검증으로 남았다.

    ### Minecraft 실행 계층 `[x]`

    actor가 선택한 JavaScript skill이 실제 Minecraft 상태를 바꾸고, 오류가 나도 다음 실행을 계속할 수 있는지 확인한다.

    - [x] Mineflayer bridge health/version과 request-local bot lifecycle
    - [x] finite position guard와 failure 뒤 bridge 생존
    - [x] `/pause` 없이 mod-free server에서 나무와 작업대 각각 10/10
    - [x] inventory delta, latency, dependency와 Minecraft log 자동 저장
    - [x] bridge·pause bundle·bot lifecycle의 결합 문제와 변경 이유 문서화
    - [x] `a157205`를 `odyssey-modernized-executor-1.19.4` annotated tag로 로컬·원격에 고정

    원본 bridge의 재실행이나 legacy 대비 latency 표는 요구하지 않는다. 현재 실행 계층이 clean install, 정상 행동과 대표 failure recovery를 반복 통과한 것으로 이 범위를 완료한다.
3) 다음 목표 (modernization_milestone.md에 세부사항)
    - 논문–코드–dependency 대응, Skill library와 semantic retrieval 작업 완료
    - 나머지 취약한/불안정한 과제들을 순차적으로 개선.
    - 피드백
        - 기능 전부 재현 & 현대화는 아닐수도 있다 → 일부 까다로운게 있을 수 잇다.
            - 스킬은 많음 → 마크에서 캐고 조합; 작동이 되면 다 되지 않나?
            - 일부가 안될수도 있다.
            - 너무 다양한 태스크 → 판이 너무 커진다. 적당한 태스크 잡는걸 목표 (예를들어 다이아 얻기 까지)
            - 목표를 줬을 때 스킬이 다 있고 적절한 스킬을 조합해서 해결할 수 있나? → 난이도가 (농장만들기나 집만들기처럼 적절한 중간목표)
            - 가벼운 모델은 실패/무거운 모델은 성공할만한
            - 오뎃세이에서 할만한거 전부 최신화하려면 시간이 걸릴수밖에
        - 챗봇 : 챗봇이랑 같이 작업할때 챗봇의 방향이 옳은 방향으로 복잡해지는가? 필수적인가? 내가 컨트롤 가능한 수준인가?
            - 스코프를 적절하게 만들고 계속 쪼지 않는이상 필요이상으로 복잡; 뭘 남기고 뭘 버리는지의 판단도 항상 인간이랑 일치하지 않을수도
            - 선별/축약/요약/판단의 영역이 더 중요해진다
        - 연구주제 : 방향이 헷갈리면 상위 주제가 무엇인지 상기해라; (적절하게 더 작은 목표로 작게 쳐 내거나)
            - 기준 : 남들하던거/권위에 기대긴 함 → 단, 희소하거나 하는게 더 컨트리뷰션 있을수도 (따라하는게 나쁘진 않지만 훌륭한 연구자 → 독창적)

# 8.27 랩미팅
1) 이번주 목표
    - Skill library를 정적으로 정리한 상태에서 실제 재현 가능한 retrieval 입력 계층으로 올리는 것

    1. Primitive runtime 결함 정리
        - `goto`, `getAnimal`의 명백한 구현 오류 수정
        - `feedAnimals`, `cookFood`, `killMonsters`의 contract 위험 확인
        - primitive를 조회·장착·이동·상호작용 등으로 나눠 대표 fixture(고정본) 작성
        - 서버가 필요한 fixture는 실행 명령과 성공 조건을 준비한 뒤 직접 실행

    2. Semantic encoder 조건 고정
        - 공개 코드의 `paraphrase-multilingual-MiniLM-L12-v2` 정확한 revision/checksum 기록
        - max length, pooling, normalization 설정 기록
        - 같은 corpus(말뭉치)를 다시 embedding할 수 있는 manifest(확정본) 작성
            - 같은 입력을 다시 만들 수 있는가?
        - Chroma·LangChain deprecated API 경고 정리
        - retrieval profile의 dependency version/lock 작성

    3. Retrieval fixture 완성
        - top-5를 기본 profile로 구현(의도는 저사양 노드에서 불필요한 연산을 줄이고 추가적인 계산이 유의미하진 않다고 판단)
            - top-10을 별도 profile로 분리
        - 대표 자연어 subgoal 몇 개에 대한 후보와 score 저장
        - index 재생성·재로드 후 후보 순서가 유지되는지 확인
            - 구형/원본 인덱스 사용시 잠재적 문제가 있고 어차피 인코더로서 재현 가능하기 때문에 구형 index 제거
        - 조건과 결과를 고정해 이후 actor 실험의 입력을 통제
        - 빈 환경에서 install → index 생성 → reload → 검색 smoke test 
            - 2. 에서 통과하긴 했지만 설치->임베딩->검색 까지 파이프라인 통과

    4. +@
        - 작업을 하면서도 지속적으로 목표를 상기중. 현재 코드 자체의 디버깅/트러블슈팅 뿐만이 아니라 semantic transfomer의 조건 확정이나 clean install 또한 주관적인 입장이지만 파이프라인을 명시적이고 깔끔하게 한다는 측면에서 개인적으로는 타당하다고 생각
        - 추가로 의미상/기능상으로 세부 목표를 묶어 한 보고 단위를 정하고 report_log.md 로 체계화
        - 현대화 마일스톤 문서상으로도 

2) 다음 목표
    - 논문–코드–dependency 대응 `[~]` : 미완료된 나머지 항목들 보수
    - Actor와 model service `[ ]`
    - Planner–actor–critic end-to-end `[ ]`
    - 능동 skill lifecycle 보존 profile `[ ]`
        - 대략 2-3주, 보수적으론 3-4주면 완전한 현대화 가능.
    - in context RL이 전통적인 뉴럴넷/딥러닝에서의 온라인학습이나 보조 수단(RAG등) 외에도 실시간으로, 혹은 한 세션의 lifecycle 내에서 적응 가능한 시스템으로서 방법론이 가능한가? (넓게보면 보이저-오딧세이-마인스카이넷도 이 질문의 연장선이라고 넓은 관점에서 해석 가능할지도)
        - 구체적으로는 챗봇등에서 과거 대화 내역 -> 감성분석 및 스코어링 -> 적응이 기존 트랜스포머 only보다 더 효율적으로 가능한가?
            - 막연히 드는 생각이지만 어차피 트랜스포머 구조상 모든 입력을 읽고 다음 토큰을 예측하는 것 이기 때문에 의도적이진 않아도 사용자의 의도에 적응한다고는 생각
        - RLHF등과는 별개로 구분
        - 아직 구체화되고 엄밀한 질문은 아니고 추상적으로 러프하게 던지는 질문