from langgraph.checkpoint.memory import MemorySaver
import json

class FileMemorySaver(MemorySaver):
  def __init__(self, filepath="memory_store.json"):
    self.filepath = filepath
    try:
      with open(self.filepath, "r") as f:
        self.store = json.load(f)
    except FileNotFoundError:
      self.store = {}

  def save(self, key, value, config=None):
    self.store[key] = value
    with open(self.filepath, "w") as f:
      json.dump(self.store, f)

  def load(self, key, config=None):
    return self.store.get(key, None)

  def delete(self, key, config=None):
    if key in self.store:
      del self.store[key]
      with open(self.filepath, "w") as f:
        json.dump(self.store, f)