import streamlit as st
from langchain_core.messages.chat import ChatMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_teddynote.prompts import load_prompt
from langchain import hub
from langchain_teddynote import logging

logging.langsmith("Streamlit 실습")

# 프롬프트 타입 선택 기능 추가하기

load_dotenv()

st.title("나만의 챗GPT 만들기")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

with st.sidebar:
    clear_btn = st.button("대화 초기화")
    selected_prompt = (
        st.selectbox(  # select box 추가. index=-0은 기본값은 첫번재라는 의미.
            "프롬프트를 선택해 주세요", ("기본모드", "SNS 게시글", "요약"), index=0
        )
    )


def print_messages():
    for chat_message in st.session_state["messages"]:
        st.chat_message(chat_message.role).write(chat_message.content)


def add_message(role, message):
    st.session_state["messages"].append(ChatMessage(role=role, content=message))


def create_chain(
    prompt_type,
):  # 프롬프트 타입에 따라 서로 다른 프롬프트 템플릿 적용
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "당신은 친절한 AI 어시스턴트입니다."),
            ("user", "#Question:\n{question}"),
        ]
    )
    if prompt_type == "SNS 게시글":
        prompt = load_prompt("prompts/sns.yaml", encoding="utf-8")  # utf-8
    elif prompt_type == "요약":
        prompt = hub.pull("teddynote/chain-of-density-map-korean")  # langchain hub
        print("prompt", prompt)

    llm = ChatOpenAI(model_name="gpt-4o", temperature=0)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    return chain


if clear_btn:
    st.session_state["messages"] = []


print_messages()

user_input = st.chat_input("궁금한 내용을 물어보세요!")

if user_input:
    st.chat_message("user").write(user_input)
    chain = create_chain(selected_prompt)
    response = chain.stream({"question": user_input})

    with st.chat_message("assistant"):
        container = st.empty()

        ai_answer = ""
        for token in response:
            ai_answer += token
            container.markdown(ai_answer)

        add_message("user", user_input)
        add_message("assistant", ai_answer)
