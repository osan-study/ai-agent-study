import os
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader

# 환경 변수 로드
load_dotenv()

# OpenAI API 키 확인
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY가 설정되지 않았습니다.")

def create_chroma_db():
    """Chroma 벡터스토어 생성 및 문서 저장"""
    
    # 1. 문서 로드 (예시)
    # loader = TextLoader("your_document.txt")
    # documents = loader.load()
    
    # 임시 문서 데이터 (실제로는 위의 loader 사용)
    from langchain.schema import Document
    documents = [
        Document(page_content="RAG는 Retrieval-Augmented Generation의 줄임말입니다.", metadata={"source": "doc1"}),
        Document(page_content="벡터스토어는 임베딩된 벡터를 저장하는 데이터베이스입니다.", metadata={"source": "doc2"}),
        Document(page_content="LangChain은 LLM 애플리케이션 개발을 위한 프레임워크입니다.", metadata={"source": "doc3"})
    ]
    
    # 2. 텍스트 분할
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        separators=["\n\n", "\n", " ", ""]
    )
    split_documents = text_splitter.split_documents(documents)
    
    # 3. 임베딩 모델 초기화
    embeddings = OpenAIEmbeddings(
        model="text-embedding-ada-002"  # 또는 "text-embedding-3-small"
    )
    
    # 4. Chroma DB 생성 (메모리 기반)
    db_memory = Chroma.from_documents(
        documents=split_documents,
        embedding=embeddings,
        collection_name="my_db"
    )
    
    # 5. Chroma DB 생성 (디스크 저장)
    db_persistent = Chroma.from_documents(
        documents=split_documents,
        embedding=embeddings,
        collection_name="my_persistent_db",
        persist_directory="./chroma_storage"  # 로컬 저장소
    )
    
    return db_memory, db_persistent

def test_search(db):
    """벡터스토어 검색 테스트"""
    
    # 유사도 검색
    query = "RAG란 무엇인가요?"
    docs = db.similarity_search(query, k=3)
    
    print(f"검색 쿼리: {query}")
    print("=" * 50)
    
    for i, doc in enumerate(docs, 1):
        print(f"{i}. {doc.page_content}")
        print(f"   메타데이터: {doc.metadata}")
        print()
    
    # 점수와 함께 검색
    docs_with_scores = db.similarity_search_with_score(query, k=3)
    print("점수와 함께 검색 결과:")
    print("=" * 50)
    
    for doc, score in docs_with_scores:
        print(f"점수: {score:.4f}")
        print(f"내용: {doc.page_content}")
        print(f"메타데이터: {doc.metadata}")
        print()

def add_documents_to_existing_db():
    """기존 DB에 문서 추가"""
    
    # 기존 DB 로드
    embeddings = OpenAIEmbeddings()
    db = Chroma(
        collection_name="my_persistent_db",
        embedding_function=embeddings,
        persist_directory="./chroma_storage"
    )
    
    # 새 문서 추가
    new_documents = [
        Document(
            page_content="Chroma는 AI 네이티브 오픈소스 임베딩 데이터베이스입니다.",
            metadata={"source": "new_doc1"}
        )
    ]
    
    db.add_documents(new_documents)
    
    return db

def advanced_chroma_usage():
    """고급 Chroma 사용법"""
    
    embeddings = OpenAIEmbeddings()
    
    # 커스텀 설정으로 DB 생성
    db = Chroma(
        collection_name="advanced_db",
        embedding_function=embeddings,
        persist_directory="./advanced_chroma",
        collection_metadata={"hnsw:space": "cosine"}  # 코사인 유사도 사용
    )
    
    # 메타데이터 필터링과 함께 검색
    query = "벡터스토어"
    docs = db.similarity_search(
        query,
        k=3,
        filter={"source": "doc2"}  # 특정 소스만 검색
    )
    
    # 검색기로 변환
    retriever = db.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "k": 5,
            "score_threshold": 0.8  # 유사도 임계값
        }
    )
    
    return db, retriever

if __name__ == "__main__":
    try:
        # 1. 기본 Chroma DB 생성
        print("Chroma DB 생성 중...")
        db_memory, db_persistent = create_chroma_db()
        print("✓ DB 생성 완료")
        
        # 2. 검색 테스트
        print("\n검색 테스트:")
        test_search(db_memory)
        
        # 3. 문서 추가 테스트
        print("기존 DB에 문서 추가...")
        updated_db = add_documents_to_existing_db()
        print("✓ 문서 추가 완료")
        
        # 4. 고급 사용법
        print("\n고급 사용법 테스트:")
        advanced_db, retriever = advanced_chroma_usage()
        
        print("모든 테스트 완료!")
        
    except Exception as e:
        print(f"오류 발생: {e}")