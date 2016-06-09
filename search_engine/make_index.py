import re
import json
from search.models import SearchResult

class MakeIndex:
	def __init__(self, results):
		self.results = results
		self.index_path = 'search_engine/indexes.json'

	def process_file(self):
		files_and_words = {}
		for result in self.results:
			files_and_words[result.filename] = result.normalized_html.split()
		return files_and_words

	def make_positions(self, words_dict):
		words_position = {}
		for index, word in enumerate(words_dict):
			if word in words_position:
				words_position[word].append(index)
			else:
				words_position[word] = [index]
		return words_position

	def make_intermediate_indexes(self):
		files_and_words = self.process_file()
		total_dict = {}
		for result in self.results:
			total_dict[result.filename] = self.make_positions(files_and_words[result.filename])
		return total_dict

	def make_indexes(self):
		intermediate_indexes = self.make_intermediate_indexes()
		indexes = {}
		for filename in intermediate_indexes:
			for word in intermediate_indexes[filename]:
				if word in indexes:
					indexes[word][filename] = intermediate_indexes[filename][word]
				else:
					indexes[word] = {filename : intermediate_indexes[filename][word]}
		return indexes

	def save_indexes(self):
		self.indexes = json.load(open(self.index_path))
		self.new_indexes = self.make_indexes()
		self.merge_indexes()
		json.dump(self.indexes, open(self.index_path, 'w'))

	def merge_indexes(self):
		for word in self.new_indexes:
			if word in self.indexes:
				self.indexes[word].update(self.new_indexes[word])
			else:
				self.indexes[word] = self.new_indexes[word]