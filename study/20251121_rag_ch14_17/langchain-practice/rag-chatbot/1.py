from dotenv import load_dotenv
from langchain_teddynote import logging
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

load_dotenv()
# logging.langsmith("RAG 챗봇")

# 단계 1. 문서 로드(Load Documents)
loader = PyMuPDFLoader(
    "data/SPRI_AI_Brief_2023년12월호_F.pdf"
)  # Document 타입으로 래핑. 기본적으로 페이지 단위로 분할
docs = loader.load()

# 단계 2. 문서 분할(Split Documents)
## 문서에서 같은 맥락이 이어지는 단락의 크기를 가늠해서 그 정도의 글자 수를 청크 크기로 지정하는 것이 좋음
text_spliter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_documents = text_spliter.split_documents(docs)

# 단계 3. 임베딩(Embedding) 생성
embeddings = OpenAIEmbeddings()

# 단계 4. DB 생성(Create DB) 및 저장
vectorstore = FAISS.from_documents(documents=split_documents, embedding=embeddings)

# 단계 5. 리트리버(Retriever) 생성. 문서에 포함되어 있는 정보를 검색하고 생성
retriever = vectorstore.as_retriever()
# retriever.invoke("삼성전자가 자체 개발한 AI의 이름은?")

# 단계 6. 프롬프트 생성 단계
prompt = PromptTemplate.from_template(
    """You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, just say that you don't know. Answer in Korean.
	
	# Context:
	{context}
	
	# Question:
	{question}
	
	# Answer:"""
)

# 단계 7. 언어 모델(LLM 생성)
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# 단계 8. 체인(Chain) 생성
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 체인 실행(Run Chain). 문서에 대한 질의를 입력하고, 답변을 출력
question = "삼성전자가 자체 개발한 AI의 이름은?"
response = chain.invoke(question)
print(response)
