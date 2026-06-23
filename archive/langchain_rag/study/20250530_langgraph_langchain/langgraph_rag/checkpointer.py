

from utils.visualize_graph import visualize_graph
from utils.file_memory_saver import FileMemorySaver
from typing import TypedDict, Annotated, Literal
from langgraph.graph import  StateGraph, START, END


class SampleState(TypedDict):
  text: Annotated[str, 'question 텍스트']
  count : Annotated[int, 'counter']
  status: Annotated[str, '카운트 상태']

key = "checkpointer"

work_flow = StateGraph(SampleState)

def question_setup(state) -> SampleState  :
  return { "text": state['text'] + " question_setup!! "}

def secondState(state) -> SampleState :
  return SampleState(count=state['count'] + 1)

def conditionalEdgeState(state) -> Literal['resolve', 'reject'] :

  if(int(state['count']) > 5) :
    return 'reject'

  return 'resolve'

def rejectPrintNode(state: SampleState) -> SampleState :
  return { 'status': 'reject'}

def resolvePrintNode(state: SampleState) -> SampleState :
  return { 'status': 'resolve'}

work_flow.add_node("question", question_setup)
work_flow.add_node("counter", secondState)

work_flow.add_node("reject_print_node", rejectPrintNode)
work_flow.add_node("resolve_print_node", resolvePrintNode)

work_flow.add_edge(START, "question")
work_flow.add_edge("question", "counter")
work_flow.add_edge("counter", END )
work_flow.add_conditional_edges("counter", conditionalEdgeState, {
  'reject' : 'reject_print_node',
  'resolve': 'resolve_print_node'
})

app = work_flow.compile()

file_memory_saver = FileMemorySaver()
load = file_memory_saver.load(key="checkpointer")
if(load is None) :
  result = app.invoke({"text": "Hello World", "count": 1})
else :
  result = app.invoke(load)

print(result)
file_memory_saver.save(key = "checkpointer", value=result)



visualize_graph(app, __file__)