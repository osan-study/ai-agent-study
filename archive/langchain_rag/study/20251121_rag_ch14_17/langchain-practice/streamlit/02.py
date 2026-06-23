import streamlit as st
from langchain_core.messages.chat import ChatMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# 웹 앱에 체인 생성하기

load_dotenv()  ## 환경 변수 불러오기

st.title("나만의 챗GPT 만들기")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 사이드바 추가 + 초기화 버튼
with st.sidebar:
    clear_btn = st.button("대화 초기화")


def print_messages():
    for chat_message in st.session_state["messages"]:
        st.chat_message(chat_message.role).write(chat_message.content)


def add_message(role, message):
    st.session_state["messages"].append(ChatMessage(role=role, content=message))


def create_chain():  ## 체인 생성
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "당신은 친절한 AI 어시스턴트입니다."),
            ("user", "#Question:\n{question}"),
        ]
    )
    llm = ChatOpenAI(model_name="gpt-4o", temperature=0)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    return chain


# 메시지 초기화
if clear_btn:
    st.session_state["messages"] = []


print_messages()

user_input = st.chat_input("궁금한 내용을 물어보세요!")

if user_input:
    st.chat_message("user").write(user_input)
    chain = create_chain()  #
    response = chain.stream(
        {"question": user_input}
    )  # 응답을 스트리밍 방식으로 출력. question 키 값으로 사용자 입력 내용(user_input)을 받음
    with st.chat_message("assistant"):
        container = st.empty()  # 실시간 응답을 표시하기 위한 빈 공간

        ai_answer = ""
        for token in response:  # AI의 응답을 토큰 단위로 받아 순차적으로 추가
            ai_answer += token
            container.markdown(ai_answer)

        add_message("user", user_input)
        add_message("assistant", ai_answer)  # ai 응답 저장
