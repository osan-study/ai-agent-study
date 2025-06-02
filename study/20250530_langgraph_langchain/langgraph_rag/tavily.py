from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

from langchain_community.tools.tavily_search import TavilySearchResults

model = ChatOpenAI(model="gpt-4o", temperature=0, streaming=True)

tools = TavilySearchResults(max_result=1)

# RecursiveCharacterTextSplitter
response = tools.invoke({"query": "2025 유로파리그 우승팀은??"})

print(response[0]["title"])
print(response[0]["url"])
print(response[0]["content"])
print(response[0]["score"])

