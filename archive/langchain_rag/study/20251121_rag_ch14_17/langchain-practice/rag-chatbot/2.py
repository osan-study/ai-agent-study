import streamlit as st
from langchain_core.messages.chat import ChatMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_teddynote.prompts import load_prompt
import glob  # 특정한 문자 규칙을 주면 해당 규칙에 해당하는 파일ㅇ르 가져와서 리스트로 만들어줌

load_dotenv()

st.title("나만의 챗GPT 만들기")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

with st.sidebar:
    clear_btn = st.button("대화 초기화")

    prompt_files = glob.glob("prompts/*.yaml")  # 1.yaml select box 추가
    selected_prompt = st.selectbox("프롬프트를 선택해 주세요", prompt_files, index=0)
    task_input = st.text_input("TASK 입력", "")  # 3.task 입력할 수 있는 UI 요소 추가


def print_messages():
    for chat_message in st.session_state["messages"]:
        st.chat_message(chat_message.role).write(chat_message.content)


def add_message(role, message):
    st.session_state["messages"].append(ChatMessage(role=role, content=message))


def create_chain(prompt_filepath, task=""):
    prompt = load_prompt(prompt_filepath, encoding="utf-8")  # 2. prompt 불러오기
    if task:
        prompt = prompt.partial(task=task)  # 3.

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
    chain = create_chain(selected_prompt, task=task_input)  # 3.task_input 전달
    response = chain.stream({"question": user_input})

    with st.chat_message("assistant"):
        container = st.empty()

        ai_answer = ""
        for token in response:
            ai_answer += token
            container.markdown(ai_answer)

        add_message("user", user_input)
        add_message("assistant", ai_answer)
