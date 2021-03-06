# imports
import configs
from utils import load_pkl_file
from utils import SimsModel

import sys
import logging
from itertools import chain
from six.moves import cPickle as pickle
from collections import Counter
from operator import itemgetter
from random import choice

from nltk.tag import pos_tag
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.corpus import wordnet as wn
	
# setup
logging.basicConfig(level=logging.DEBUG)


# classes:
class Frequencies(object):
	def __init__(self):
		self.frequencies = self.get_frequencies()

	def get_frequencies(self):
		logging.debug('loading frequencies')
		return load_pkl_file(configs.FREQUENCIES_FILE_PATH)

	def get_frequency(self, word):
		return self.frequencies[word]


# functions
def get_synonyms(word):
	logging.debug('getting synonyms of word: {}'.format(word))
	synsets = wn.synsets(word)

	synonyms = [word.lemma_names() for word in synsets]
	synonyms = chain.from_iterable(synonyms)
	synonyms = list(set(synonyms))
	synonyms = [synonym.lower()
				for synonym in synonyms
				if synonym != word]

	return synonyms


def filter_frequencies(words, max_word_frequency, frequencies):
	logging.debug('filtering frequencies')
	word_frequencies = [(word, frequencies.get_frequency(word))
						for word in words]

	filtered_words = []
	filtered_words.extend([word
						   for word, freq in word_frequencies
						   if freq <= max_word_frequency])

	return filtered_words


def filter_similarities(main_word, synonyms, min_similarity, model):
	logging.debug('filtering similarities')
	return [word
			for word in synonyms
			if model.get_similarity(main_word, word) >= min_similarity]


def convert_tag(tag):
	return tag[0]


def filter_pos_tags(main_word, synonyms, main_pos_tag=None):
	logging.debug('filtering pos tags')
	def get_word_pos_tag(word):
		return convert_tag(pos_tag([word])[0][1])

	if main_pos_tag is None:
		main_pos_tag = get_word_pos_tag(main_word)

	return [word
			for word in synonyms
			if get_word_pos_tag(word) == main_pos_tag]


def get_advanced_words(word, frequencies, sims_model, word_tag=None):
	logging.debug('getting advanced words from: {}'.format(word))
	syns = get_synonyms(word)
	syns = filter_similarities(word, syns, configs.MIN_WORD2VEC_SIMILARITY,
							   sims_model)
	syns = filter_frequencies(syns, configs.MAX_WORD_FREQUENCY, frequencies)
	syns = filter_pos_tags(word, syns, main_pos_tag=word_tag)

	return syns


def tag_text(text):
	logging.debug('pos tagging text')
	return [(word, convert_tag(tag)) for word, tag in pos_tag(word_tokenize(text))]


def is_accepted(word, tag):
	return True


def transform_sentence(sentence, frequencies, sims_model):
	logging.debug('transforming sentence')	
	tagged = tag_text(sentence)

	new_sentence = ''
	for word, tag in tagged:
		if is_accepted(word, tag):
			advanced_words = get_advanced_words(word.lower(), frequencies, sims_model, word_tag=tag)
		else:
			advanced_words = None

		if advanced_words:
			new_word = choice(advanced_words)
			if word[0].isupper():
				new_word = new_word.title()
		else:
			new_word = word

		if word not in '?!.,':
			new_sentence += ' '

		new_sentence += new_word

	new_sentence = new_sentence[1:]

	return new_sentence


def main():
	logging.debug('running main')
	frequencies = Frequencies()
	sims_model = SimsModel() 

	sentence = sys.argv[1]

	transformed = transform_sentence(sentence, frequencies, sims_model)
	print(transformed)


if __name__ == '__main__':
	main()
