from utils.visualize_graph import visualize_graph
from typing import TypedDict, Annotated
from langgraph.graph import  StateGraph, START, END

class SampleState(TypedDict):
  text: Annotated[str, 'question 텍스트']


work_flow = StateGraph(SampleState)

# 노드 - 작업단위
def question_setup(state) -> SampleState  :
  return { "text": state['text'] + " question_setup!! "}

# 노드 추가
work_flow.add_node("question", question_setup)

# 엣지 등록


# work_flow.set_entry_point("question")
# work_flow.set_finish_point("question")
work_flow.add_edge(START, "question")
work_flow.add_edge("question", END)

#  그래프를 실행가능한 형태로 컴파일,
# 해당 과정에서 구조거 검증되고 최적화됨.
app = work_flow.compile()

# invoke에 적힌 매개변수를 초기상태로 설정.
result = app.invoke({"text": "Hello World"})
print(result)


visualize_graph(app, __file__)