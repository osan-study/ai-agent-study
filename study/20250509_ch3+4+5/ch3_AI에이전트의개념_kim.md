# 3. AI 에이전트의 개념

## *AI 에이전트란?*

- 사람의 개입 없이 스스로 작업을 수행하고 의사 결정을 내리는 프로그램입니다.
    
    사람의 반복 작업 또는 복잡한 문제 해결을 돕기 위해 설계되었습니다.
    

- 기능 및 장점
    1. 자동화: 반복적이거나 단순한 작업을 자동으로 수행.
    2. 효율성: 시간과 비용 절감 가능.
    3. 자율성: 상황별로 스스로 판단하여 작업 수행. 계획 수립 - 작업 실행 - 결과 평가까지 모두 자율적으로 실행됨.

## *AI 에이전트를 활용한 실제 비즈니스*

- Lemonade Insurance
    - 소개: AI 기반 보험회사
    - 보험 가입을 위한 브로커를 없애고 AI 에이전트로 대체함.
        
        Lemonade에는 세 명의 AI 에이전트가 존재함.
        
        - Maya - 보험 가입 담당. 보험 가입 시에 1,700개의 데이터 포인트를 수집.
        - Jim - 보험금 심사 담당. 피보험자가 청구한 보험금의 지급 가능여부를 빠르게 판단하여 지급.
        - Cooper - 사내 업무 담당. 직원에게 필요한 문서를 찾아주거나, 자연재해 발생 시, 해당 지역의 신규 보험 가입을 중단
        
        [https://youtu.be/flSLI2JmWVE?feature=shared&t=6](https://youtu.be/flSLI2JmWVE?feature=shared&t=6)
        

- Blue River Technology
    - 소개: AI 기반 농업기술개발
    - See & Spray 시스템을 개발하여 제초제 사용량을 혁신적으로 줄임.
        - 카메라로 수집한 정보를 AI가 판단하여, 작물과 잡초를 구분
        - 식별된 잡초에는 필요한 영역에만 정밀하게 제초제를 분사
        
        [https://youtu.be/L0nGUSPDnUU?feature=shared&t=28](https://youtu.be/L0nGUSPDnUU?feature=shared&t=28)
        

- Betterment
    - 소개: AI 로보어드바이저를 통한 자산 관리
    - AI를 활용한 포트폴리오 자동 리밸런싱 시스템
    - 사용자의 투자 목표, 성향(공격적/보수적), 자산 규모를 입력하면 AI 가 적절한 포트폴리오 구성
        
        
        [https://youtu.be/ikNghIrvnJs?feature=shared](https://youtu.be/ikNghIrvnJs?feature=shared)
        

## *LLM vs RAG vs AI 에이전트*

- 책에서는 LLM과 RAG와 AI 에이전트를 구분하여 표현하는 것 같습니다. 그러나 여기에 대해서 제가 알아본 바로는 포함 관계가 있는 것으로 보이는데 어떠신가요?
    - LLM: 대규모 텍스트 데이터로 사전 학습된 AI 모델
    - RAG: LLM + 웹 검색의 결합
    - AI 에이전트: LLM + 작업수행의 결합 (단, 웹 검색이 필요한 경우 RAG도 결합됨)

- 따라서 이메일 작성이라는 예를 들어 본다면,
    - LLM: 이메일 내용을 작성
    - RAG: 웹의 최신 정보를 포함하여 이메일 내용을 작성
    - AI 에이전트: 작성된 이메일을 전송까지 실행. 또한 이메일 응답에 대한 모니터링과 후속 처리까지 가능.