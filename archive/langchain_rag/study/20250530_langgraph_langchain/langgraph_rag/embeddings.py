# from langchain.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import OpenAIEmbeddings
# from openai import embeddings
from dotenv import load_dotenv
import chromadb
from numpy import dot
from numpy.linalg import norm
import numpy as np

load_dotenv()
# a == vector, b == embedding_text
def cosine_similarity(a, b):
    return dot(a, b) / (norm(a) * norm(b))


embeddings = OpenAIEmbeddings()

text = "안녕하세요 텍스트 임베딩 테스트입니다."
vector = embeddings.embed_query(text);

text2 = "누구세요? 나는 손흥민입니다"
vector2 = embeddings.embed_query(text2);
print(vector)



client = chromadb.Client(
    chromadb.config.Settings(
        persist_directory="./chroma_store"  # 로컬 저장 경로
    )
)

collection = client.get_or_create_collection("my_collection")

# 길이는 항상 같아야함
collection.add(
    documents=[text, text2],        # 원본 텍스트
    embeddings=[vector, vector2],     # 임베딩 벡터
    ids=["sample1", "sample2"],            # 고유 ID
    metadatas=[{"type": "어떻게 보는걸까 "}, {"type": "손흥민"}]  # 선택적 메타데이터
)

# 쿼리용 임베딩 생성 (검색할 문장도 임베딩으로 변환)
query_vector = embeddings.embed_query("안녕")


result = collection.query(query_embeddings=[query_vector] , n_results=3)

print(f"text - {text}: 유사도 - {cosine_similarity(np.array(vector), np.array(query_vector))}")
print(f"text2 - {text2}: 유사도 - {cosine_similarity(np.array(vector2), np.array(query_vector))}")
print("문서 내용:", result["documents"])
print("문서 ID:", result["ids"])
print("메타데이터:", result["metadatas"])

# 벡터간 거리 기반 유사 문서를 찾는다. 가까운 순으로 반환함.
