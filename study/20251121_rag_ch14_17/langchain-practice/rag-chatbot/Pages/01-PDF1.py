import streamlit as st
from langchain_core.messages import ChatMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_teddynote.prompts import load_prompt
from dotenv import load_dotenv
import glob
import os
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_community.vectorstores import FAISS
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

st.title("PDF 기반 QA")

if not os.path.exists(".cache"):
    os.mkdir(".cache")

if not os.path.exists(".cache/files"):
    os.mkdir(".cache/files")

if not os.path.exists(".cache/embeddings"):
    os.mkdir(".cache/embeddings")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "chain" not in st.session_state:
    st.session_state["chain"] = None

with st.sidebar:
    clear_btn = st.button("대화 초기화")
    uploaded_file = st.file_uploader(
        "파일 업로드", type=["pdf"]
    )  # 업로더 UI 작성. 파일 유형은 pdf로 지정


def print_messages():
    for chat_message in st.session_state["messages"]:
        st.chat_message(chat_message.role).write(chat_message.content)


def add_message(role, message):
    st.session_state["messages"].append(ChatMessage(role=role, content=message))


@st.cache_resource(show_spinner="업로드한 파일을 처리 중입니다...")
def embed_file(file):
    file_content = file.read()
    file_path = f"./.cache/files/{file.name}"
    with open(file_path, "wb") as f:
        f.write(file_content)

    # 단계 1: 문서 로드(Load Documents)
    loader = PDFPlumberLoader(file_path)
    docs = loader.load()

    # 단계 2: 문서 분할(Split Documents)
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    split_documents = text_splitter.split_documents(docs)

    # 단계 3: 임베딩(Embedding) 생성
    embeddings = OpenAIEmbeddings()

    # 단계 4: DB 생성(Create DB) 및 저장
    # 벡터스토어를 생성합니다.
    vectorstore = FAISS.from_documents(documents=split_documents, embedding=embeddings)

    # 단계 5: 검색기(Retriever) 생성
    # 문서에 포함되어 있는 정보를 검색하고 생성합니다.
    retriever = vectorstore.as_retriever()
    return retriever


def create_chain(retriever):
    # 단계 6: 프롬프트 생성(Create Prompt)
    prompt = PromptTemplate.from_template(
        """You are an assistant for question-answering tasks. 
	Use the following pieces of retrieved context to answer the question. 
	If you don't know the answer, just say that you don't know. 
	Answer in Korean.

	#Context: 
	{context}

	#Question:
	{question}

	#Answer:"""
    )

    # 단계 7: 언어 모델(LLM) 생성
    llm = ChatOpenAI(model_name="gpt-4o", temperature=0)

    # 단계 8: 체인(chain) 생성
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return chain


if uploaded_file:
    retriever = embed_file(uploaded_file)
    chain = create_chain(retriever)
    st.session_state["chain"] = chain

if clear_btn:
    st.session_state["messages"] = []

print_messages()

user_input = st.chat_input("궁금한 내용을 물어보세요!")

# wraning_msg = st.empty()

if user_input:
    chain = st.session_state["chain"]
    if chain is not None:
        st.chat_message("user").write(user_input)
        response = chain.stream(user_input)

        with st.chat_message("assistant"):
            container = st.empty()
            ai_answer = ""
            for token in response:
                ai_answer += token
                container.markdown(ai_answer)

        add_message("user", user_input)
        add_message("assistant", ai_answer)

    # else:
    #     wraning_msg.error("파일을 업로드해 주세요.")
