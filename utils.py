# imports
import configs

import logging
from six.moves import cPickle as pickle

import gensim


# classes
class SimsModel(object):
	def __init__(self):
		self.model = self.load_sims_model()

	def load_sims_model(self):
		logging.debug('loading sims model')
		return gensim.models.KeyedVectors.load(configs.SIMS_FILE_PATH, mmap='r')

	def get_similarity(self, word1, word2):
		try:
			return self.model.similarity(word1, word2)	
		except Exception as e:
			return -float('inf')


# functions
def load_pkl_file(file_path):
	logging.debug('loading pickle file at: {}'.format(file_path))
	with open(file_path, 'rb') as pkl_file:
		return pickle.load(pkl_file)


def save_pkl_file(data, file_path):
	logging.debug('saving pickle file at: {}'.format(file_path))
	with open(file_path, 'wb') as pkl_file:
		pkl_file.flush()
		pickle.dump(data, pkl_file)


def load_word2vec_model():
	logging.debug('loading word2vec model')
	return gensim.models.KeyedVectors.load_word2vec_format(configs.WORD2VEC_MODEL_PATH,
													  	   binary=True)


def main():
	pass


if __name__ == '__main__':
	main()