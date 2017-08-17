# imports
import configs
from utils import load_pkl_file
from utils import save_pkl_file

import logging
from collections import Counter

from nltk.corpus import gutenberg

# setup
logging.basicConfig(level=logging.DEBUG)


# functions
def get_corpus(all_lowercase=True):
	logging.debug('getting corpus')
	if all_lowercase:
		words = (word.lower() for word in gutenberg.words())
	else:
		words = gutenberg.words()

	return words


def get_frequencies(words):
	logging.debug('getting frequencies')
	frequencies = Counter(words)

	return frequencies


def main():
	logging.debug('running main')	
	corpus = get_corpus()
	
	frequencies = get_frequencies(corpus)

	save_pkl_file(frequencies, configs.FREQUENCIES_FILE_PATH)


if __name__ == '__main__':
	main()