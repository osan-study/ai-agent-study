# Vector Database Study Project

이 프로젝트는 다양한 벡터 데이터베이스(Vector Database)를 학습하고 실습하기 위한 프로젝트입니다.

## 지원하는 벡터 데이터베이스

- **Chroma**: 오픈소스 임베딩 데이터베이스
- **FAISS**: Facebook AI Similarity Search 라이브러리
- **Pinecone**: 클라우드 기반 벡터 데이터베이스

## 프로젝트 구조

```
├── 09-VectorStore/          # Jupyter 노트북들
│   ├── 01-Chroma.ipynb      # Chroma 실습 노트북
│   ├── 02-FAISS.ipynb       # FAISS 실습 노트북
│   └── 03-Pinecone.ipynb    # Pinecone 실습 노트북
├── vectordb/                # Python 패키지
├── data/                    # 데이터 파일들
└── images/                  # 이미지 리소스
```

## 환경 설정

이 프로젝트는 [uv](https://docs.astral.sh/uv/)를 사용하여 의존성을 관리합니다.

### 1. 의존성 설치

```bash
uv sync
```

### 2. Jupyter 노트북 실행

```bash
uv run jupyter lab
```

### 3. Python 스크립트 실행

```bash
uv run python your_script.py
```

## 주요 의존성

- `chromadb`: Chroma 벡터 데이터베이스
- `faiss-cpu`: FAISS 라이브러리 (CPU 버전)
- `pinecone-client`: Pinecone 클라이언트
- `openai`: OpenAI API 클라이언트
- `langchain`: LangChain 프레임워크
- `sentence-transformers`: 문장 임베딩 모델
- `jupyter`: Jupyter 노트북 환경

## 환경 변수 설정

`.env` 파일을 생성하여 필요한 API 키를 설정하세요:

```env
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_environment
```

## 개발 도구

개발 의존성을 설치하려면:

```bash
uv sync --extra dev
```

포함된 개발 도구:
- `pytest`: 테스트 프레임워크
- `black`: 코드 포매터
- `isort`: Import 정리
- `flake8`: 린터
- `mypy`: 타입 체커
