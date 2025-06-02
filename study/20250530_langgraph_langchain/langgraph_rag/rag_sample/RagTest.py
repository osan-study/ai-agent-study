from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

pdf_filepath = 'sample2.pdf'
loader = PyPDFLoader(pdf_filepath)
pages = loader.load()

# print(pages[0].page_content)
#
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50, length_function=len)
docs = text_splitter.split_documents(pages)
texts = text_splitter.split_text(pages[0].page_content)


recursive_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", ".", " "],  # 우선순위
    chunk_size=500,
    chunk_overlap=200
)

docs1 = recursive_splitter.split_documents(pages)
texts1 = recursive_splitter.split_text(pages[0].page_content)

split = loader.load_and_split(text_splitter=recursive_splitter)

print(texts1)

# print(len(texts))
# print(texts[0])

embeddings = OpenAIEmbeddings()

#  FaceBook AI Similarity Search
vectorstore = FAISS.from_documents(split, embeddings)

# 저장하기
vectorstore.save_local(folder_path="./rag-test", index_name='rag-test')

# 4. 질의 응답 체인 생성
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)



print("-----")

# # 5. 질문 테스트
# query = "휴대폰 인증 관련 API 알려줘 "
# result = qa_chain.invoke(query)
# print(result["result"])