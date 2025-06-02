from langchain.schema import BaseRetriever
from typing import List

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from pydantic import PrivateAttr


class ThresholdRetriever(BaseRetriever):
  _vectorstore: FAISS = PrivateAttr()
  _threshold: float = PrivateAttr()
  _k: int = PrivateAttr()

  def __init__(self, vectorstore, threshold=0.7, k=5):
    super().__init__()
    self._vectorstore = vectorstore
    self._threshold = threshold
    self._k = k

  def get_relevant_documents(self, query: str) -> List[Document]:
    results = self.vectorstore.similarity_search_with_score(query, k=self.k)
    return [doc for doc, score in results if score <= self.threshold]