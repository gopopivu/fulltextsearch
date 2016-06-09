import re
import json
from .htmlparser import delete_marks

class Queries:
  def __init__(self, query):
    self.query = query
    self.index = json.load(open('search_engine/indexes.json'))

  def by_one_word(self, word):
    self.query = delete_marks(self.query)
    if word in self.index:
      return self.index[word].keys()
    return []

  def by_whole_phrase(self):
    self.query = delete_marks(self.query)
    result = []
    words = self.query.lower().split()
    if not words:
      return []
    listOfPositions = [self.by_one_word(word) for word in words]
    setted = set(listOfPositions[0]).intersection(*listOfPositions)
    for filename in setted:
      temp = [self.index[word][filename][:] for word in words]
      for i in range(len(temp)):
        for pos in range(len(temp[i])):
          temp[i][pos] -= i
      if set(temp[0]).intersection(*temp):
        result.append(filename)
    return result



