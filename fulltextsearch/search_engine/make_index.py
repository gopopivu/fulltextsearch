import re
import json


class MakeIndex:
	def __init__(self, filenames):
		self.filenames = filenames

	def process_file(self):
		files_and_words = {}
		for filename in self.filenames:
			files_and_words[filename] = open(filename).read().split()
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
		for filename in self.filenames:
			total_dict[filename] = self.make_positions(files_and_words[filename])
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
		self.indexes = json.load(open('indexes.json'))
		self.new_indexes = self.make_indexes()
		self.merge_indexes()
		json.dump(open('indexes.json'), self.indexes)

	def merge_indexes(self):
		for word in self.new_indexes:
			if word in self.indexes:
				self.indexes[word].update(self.new_indexes[word])
			else:
				self.indexes[word] = self.new_indexes[word]


