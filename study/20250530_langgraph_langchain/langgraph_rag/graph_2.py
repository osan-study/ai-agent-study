from utils.visualize_graph import visualize_graph
from typing import TypedDict, Annotated
from langgraph.graph import  StateGraph, START, END

class SampleState(TypedDict):
  text: Annotated[str, 'question 텍스트']
  count : Annotated[int, 'counter']



work_flow = StateGraph(SampleState)

def question_setup(state) -> SampleState  :
  return { "text": state['text'] + " question_setup!! "}

def SecondState(state) -> SampleState :
  return SampleState(count=state['count'] + 1)

work_flow.add_node("question", question_setup)
work_flow.add_node("counter", SecondState)

work_flow.add_edge(START, "question")
work_flow.add_edge("question", "counter")
work_flow.add_edge("counter", END )

app = work_flow.compile()

result = app.invoke({"text": "Hello World", "count": 0})
print(result)

visualize_graph(app, __file__)