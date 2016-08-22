import sys, os

from tokenizer import *
from create_fsa_fst import *
from trainer import *

if __name__ == "__main__":

	# create data file from given txt
	main_tokenizer()

        # create fsa+fst file from data file
	main_create_fsa_fst(int(sys.argv[1]))

	# train and create viterbi
	main_trainer(sys.argv[2])
