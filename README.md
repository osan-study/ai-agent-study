

---

# 모임 소개

[오산 개발자 모임](https://kimozex.notion.site/37518824cbc1491eb753d23cc51ceb6d?v=0e4d1e0a97b0435a92a0d0c5470a13c5%20)  
[카톡방](https://open.kakao.com/o/gsIAzZPe)  
[깃허브](https://github.com/osan-study)

AI 스터디 \- 랭체인 & 랭그래프로 AI 에이전트 개발하기  
[깃허브](https://github.com/osan-study/ai-agent-study)

---

# 스터디 자료

책소개 :  
[테디노트의 랭체인을 활용한 RAG 비법노트(기본편)](https://product.kyobobook.co.kr/detail/S000216574552)   
[책 예제코드](https://github.com/teddylee777/langchain-kr) 

[테디노트의 랭체인을 활용한 RAG 비법노트(심화편)](https://product.kyobobook.co.kr/detail/S000216796093)   


참고자료 :  

[테디노트의 랭체인 노트](https://wikidocs.net/book/14314) 

[랭체인 아카데미](https://academy.langchain.com/) 

---

# 스터디 참가자

신재익, 나명진, 이정희, 김, 주디, 정 , 윤일준, 최성진

---

# 스터디 방식

매주 금요일 오후 9시-11시 온라인 모임

책 내용 + 개인 프로젝트 발표

---

# 스터디 일정

## 2025.08.22

기본편 CH 1,2,3,4 : 김  ( + 최신기술 UV 를 이용한 환경 구성 추가 + await, async 등 비동기 호출 발표 )  


## 2025.08.29

기본편 CH 5 프롬프트,6 출력파서 : 이정희 ( + misty, 랭체인 허브 등에서 프롬프트 샘플 발표 + 랭스미스 연동 핸즈온  )  

## 2025.09.05

기본편 CH 7 모델 : 나명진 (hugging face, Ollama 제외)  

기본편 CH 8 메모리 : 정세일 
[발표자료](https://www.markslides.ai/publications/RAG%EB%B9%84%EB%B2%95%EB%85%B8%ED%8A%B8-8%EC%9E%A5-%EB%A9%94%EB%AA%A8%EB%A6%AC-Zu1gvlfLetJnveg42cQX5)  

기본편 CH 9 문서로더 , 10 텍스트 분할 : 신재익  

## 2025.09.12

기본편 CH 11 임베딩 : 최성진 + LLM 원리  


## 2025.09.19

기본편 CH 12 벡터스토어 : 추숙 + 벡터 DB + DB에 대한 이해


## 2025.09.26

기본편 CH 13 리트리버 : 윤일준

## 추후 일정 조절

기본편 CH 14-17 또는 개인 프로젝트 발표

책 심화편 발표

심화편 CH 1 리랭크  

심화편 CH 2 RAG 파이프라인

심화편 CH 3 사전에 정의된 체인

심화편 CH 4 LECL 고급문법으로 Runnable 활용

심화편 CH 5 RAGAS로 답변 평가하기 

심화편 CH 6 LangSmith API를 활용한 프롬프트 최적화 

심화편 CH 7 도구와 툴킷 

심화편 CH 8 에이전트 주요기능  

심화편 CH 9 에이전트 활용  

심화편 CH 10 Streamlit을 이용한 서비스 배포 실습

심화편 CH 11 LangServe. 


## 2025.09.19

## 2025.09.26





---

# 기본편 책 목차

PART 01 처음 만나는 LangChain

CHAPTER 01 RAG 이해하기
01 RAG를 사용해야 하는 이유
02 RAG의 기막힌 능력
03 LangChain을 이용한 RAG 시스템 구축

CHAPTER 02 환경 설정
01 윈도우에서 환경 설치
02 MacOS에서 환경 설치
03 OpenAI API 키 발급 및 설정하기
04 LangSmith 키 발급 및 설정하기

CHAPTER 03 LLM 기본 용어
01 Jupyter Notebook 사용법
02 토큰, 토큰 계산기, 모델별 토큰 비용
03 모델의 입출력과 컨텍스트 윈도우

CHAPTER 04 LangChain 시작하기
01 ChatOpenAI 주요 매개변수와 출력
02 LangSmith로 GPT 추론 내용 추적하기
03 멀티모달 모델로 이미지를 인식하여 답변 출력하기
04 프롬프트 템플릿 활용하기
05 LCEL로 체인 생성하기
06 출력 파서를 체인에 연결하기
07 batch() 함수로 일괄 처리하기
08 비동기 호출 방법
09 Runnable로 병렬 체인 구성하기
10 값을 전달해 주는 RunnablePassthrough
11 병렬로 Runnable을 실행하는 RunnableParallel
12 함수를 실행하는 RunnableLambda와 itemgetter

PART 02 프롬프트와 출력 파서

CHAPTER 05 프롬프트
01 프롬프트 템플릿 만들기
02 부분 변수 활용하기
03 YAML 파일로부터 프롬프트 템플릿 로드하기
04 ChatPromptTemplate
05 MessagesPlaceholder
06 퓨샷 프롬프트
07 예제 선택기
08 FewShotChatMessagePromptTemplate
09 목적에 맞는 예제 선택기
10 LangChain Hub에서 프롬프트 공유하기

CHAPTER 06 출력 파서
01 PydanticOutputParser
02 with_structured_output() 바인딩
03 LangSmith에서 출력 파서의 흐름 확인하기
04 쉼표로 구분된 리스트 출력 파서
05 구조화된 출력 파서
06 JSON 형식 출력 파서
07 Pandas 데이터프레임 출력 파서
08 날짜 형식 출력 파서
09 열거형 출력 파서

PART 03 모델과 메모리

CHAPTER 07 모델
01 RAG에서 LLM의 역할과 모델의 종류
02 다양한 LLM 활용 방법과 API 키 가져오기
03 LLM 답변 캐싱하기
04 직렬화와 역직렬화로 모델 저장 및 로드하기
05 GPT 모델의 토큰 사용량 확인하기
06 Google Generative AI 모델
07 Hugging Face Inference API 활용하기
08 Dedicated Inference Endpoint로 원격 호스팅하기
09 Hugging Face 로컬 모델 다운로드 받아 추론하기
10 Ollama 설치 및 Modelfile 설정하기
11 Ollama 모델 생성하고 ChatOllama 활용하기
12 GPT4All로 로컬 모델 실행하기

CHAPTER 08 메모리
01 대화 버퍼 메모리
02 대화 버퍼 윈도우 메모리
03 대화 토큰 버퍼 메모리
04 대화 엔티티 메모리
05 대화 지식 그래프 메모리
06 대화 요약 메모리
07 벡터 스토어 검색 메모리
08 LCEL 체인에 메모리 추가하기
09 SQLite에 대화 내용 저장하기
10 휘발성 메모리로 일반 변수에 대화 내용 저장하기

PART 04 데이터 로드와 텍스트 분할

CHAPTER 09 문서 로더
01 문서 로더의 구조 이해하기
02 PDF 로더
03 HWP 로더
04 CSV 로더와 데이터프레임 로더
05 WebBaseLoader
06 DirectoryLoader
07 UpstageDocumentParseLoader
08 LlamaParse

CHAPTER 10 텍스트 분할
01 문자 단위로 분할하기
02 문자 단위로 재귀적으로 분할하기
03 토큰 단위로 분할하기
04 의미 단위로 분할하기
05 코드 분할하기
06 마크다운 헤더로 분할하기
07 HTML 헤더로 분할하기
08 JSON 단위로 분할하기

PART 05 벡터 스토어와 리트리버

CHAPTER 11 임베딩
01 OpenAIEmbeddings
02 CacheBackedEmbeddings
03 HuggingFaceEmbeddings
04 UpstageEmbeddings
05 OllamaEmbeddings

CHAPTER 12 벡터 스토어
01 Chroma
02 FAISS
03 Pinecone

CHAPTER 13 리트리버
01 벡터 스토어 기반 리트리버
02 문서 압축기
03 양방향 리트리버
04 긴 문맥 재정렬
05 부모 문서 리트리버
06 다중 쿼리 생성 리트리버
07 다중 벡터 스토어 리트리버
08 셀프 쿼리 리트리버
09 시간 가중 벡터 스토어 리트리버

PART 06 LangChain 실습

CHAPTER 14 Streamlit으로 ChatGPT 웹 앱 제작하기
01 기본적인 웹 앱 형태 만들기
02 웹 앱에 체인 생성하기
03 프롬프트 타입 선택 기능 추가하기

CHAPTER 15 이메일 업무 자동화 챗봇
01 이메일 내용으로부터 구조화된 정보 추출하기
02 SerpAPI를 정보 검색에 활용하기
03 구조화된 답변을 다음 체인의 입력으로 추가하기
04 이메일의 주요 정보 및 검색 정보 기반 요약 보고서 챗봇

CHAPTER 16 다양한 모델을 활용한 챗봇
01 별도의 파이썬 파일로 기능 분리하기
02 GPT 대신 Deepseek 모델 사용하기
03 Ollama 모델을 사용한 RAG
04 멀티모달 모델을 활용한 이미지 인식 기반 챗봇

CHAPTER 17 RAG 챗봇
01 PDF 문서 기반 질의응답 RAG 만들기
02 프롬프트를 개선해 주는 프롬프트 메이커
03 페이지 분할 후 파일 업로드 기능 추가하기
04 PDF 기반 QA 챗봇 만들기
05 LangSmith 추적, 다양한 LLM을 RAG에 적용하기
06 프롬프트에 출처 표시하고 표 기능 추가하기

---

# 심화편 책 목차

PART 01 고급 RAG

CHAPTER 01 리랭커로 검색된 문서 순위 조정하기
01 교차 인코더 리랭커
02 Cohere 리랭커
03 Jina 리랭커
04 FlashRank 리랭커

CHAPTER 02 RAG 파이프라인
01 네이버 뉴스 기사 기반 QA 시스템
02 RAPTOR
03 무료 오픈 모델로 구현하는 문서 기반 QA 시스템

CHAPTER 03 사전에 정의된 체인
01 Stuff 요약
02 Map-Reduce 요약
03 Map-Refine 요약
04 Chain of Density(CoD) 요약
05 Clustering-Map-Refine 요약
06 SQL 쿼리 생성기


PART 02 LCEL 고급 문법

CHAPTER 04 LCEL 고급 문법으로 Runnable 활용하기
01 RunnablePassthrough
02 Runnable 구조 검토하기
03 RunnableLambda
04 RunnableBranch와 RunnableLambda를 이용한 라우팅
05 RunnableParallel
06 config로 LLM이나 프롬프트를 동적으로 변경하기
07 @chain 데코레이터로 Runnable 설정하기


PART 03 RAG 평가와 개선

CHAPTER 05 RAGAS로 답변 평가하기
01 합성 테스트 데이터셋 생성하기
02 RAGAS로 평가하기
03 테스트 데이터셋 번역 및 업로드 관리하기

CHAPTER 06 LangSmith API를 활용한 프롬프트 최적화
01 평가용 테스트 데이터셋 구축하기
02 LLM-as-a-judge로 평가하기
03 사용자 정의 평가자 만들기
04 휴리스틱 방식으로 평가하기
05 실험별 비교 분석하기
06 요약 평가자로 전체 수준 평가하기
07 Groundedness 평가자로 할루시네이션 확인하기
08 Pairwise 평가로 실험 비교 분석하기
09 반복 평가하기
10 온라인 LLM 평가자를 활용한 평가 자동화하기
11 RAGAS를 활용해 RAG 평가하기


PART 04 에이전트

CHAPTER 07 도구와 툴킷
01 LangChain에서 제공하는 도구
02 사용자 정의 도구 만들기

CHAPTER 08 에이전트 주요 기능
01 LLM에 도구 바인딩하기
02 에이전트와 AgentExecutor 생성하기
03 에이전트의 중간 단계 스트리밍 출력하기
04 이전 대화 내용을 기억하는 에이전트 만들기
05 다양한 LLM을 활용해 에이전트 생성하기
06 iter() 함수로 단계별 출력하고 확인하기

CHAPTER 09 에이전트 활용
01 Agentic RAG
02 CSV, 엑셀 데이터 분석 에이전트
03 파일 관리 업무 자동화 에이전트
04 보고서 작성 업무 자동화 에이전트
05 CSV 파일 기반 데이터 분석 에이전트

PART 05 서비스 배포

CHAPTER 10 Streamlit을 이용한 서비스 배포 실습
01 배포를 위한 config 설정하기
02 배포를 위한 GitHub와 기타 설정 파일 준비하기
03 배포 및 동작 테스트하기
04 서비스 수정 및 변경 사항 확인하기

CHAPTER 11 LangServe
01 LangServe로 모델을 서빙하기
02 NGROK을 활용해서 모델을 외부에 공개하기

