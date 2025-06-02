from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
import chromadb

load_dotenv()

model = ChatOpenAI(model="gpt-4o", temperature=0, streaming=True)
tools = TavilySearchResults(max_result=1)

# RecursiveCharacterTextSplitter
response = tools.invoke({"query": "2025 유로파리그 우승팀은??"})

contents = response[0]["content"]
# print(response[0]["title"])
# print(response[0]["url"])
# print(response[0]["content"])
# print(response[0]["score"])

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=["\n\n", "\n", ".", " "]
)

client = chromadb.PersistentClient(path="./chroma_store")
collection = client.get_or_create_collection("euro_2025_news")

embedding_model = OpenAIEmbeddings()

for i, doc in enumerate(response):
    content = doc["content"]
    splits = text_splitter.split_text(content)

    embeddings = embedding_model.embed_documents(splits)

    ids = [f"doc_{i}_chunk_{j}" for j in range(len(splits))]
    metadatas = [{"title": doc["title"], "url": doc["url"], "chunk_index": j} for j in range(len(splits))]

    collection.add(
        documents=splits,
        embeddings=embeddings,
        ids=ids,
        metadatas=metadatas
    )

query_vector = embedding_model.embed_query("손흥민")
result = collection.query(query_embeddings=[query_vector] , n_results=3)
print(result)
print("✅ ChromaDB에 저장 완료")


