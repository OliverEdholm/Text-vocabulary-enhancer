# imports
import configs
from utils import load_word2vec_model

import os

import logging

# setup
logging.basicConfig(level=logging.DEBUG)


# functions
def convert_to_sims(model):
	logging.debug('converting model to sims')
	model.init_sims(replace=True)

	return model


def save_model(sims_model):
	logging.debug('saving sims model')

	dir_name = os.path.dirname(configs.SIMS_FILE_PATH)
	os.makedirs(dir_name)

	sims_model.save(configs.SIMS_FILE_PATH)


def main():
	logging.debug('running main')

	model = load_word2vec_model()

	sims_model = convert_to_sims(model)

	save_model(sims_model)


if __name__ == '__main__':
	main()

