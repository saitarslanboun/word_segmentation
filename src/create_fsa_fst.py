#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys, os

from textblob import TextBlob

def generate_word_list():
	#file_name = os.getcwd() + "/" + file_name[:-4] + ".data"
	with open("train.data") as f:
                words = f.read().split()

        return list(set(words))

def generate_fsa(number_of_cluster):
	#fsa_file_name = os.getcwd() + "/" + file_name[:-4] + ".fsa"
        text_file = open("train.fsa", "w")

        text_file.write("c0\n")

        dquote = '"'

	#line_str = "(0 (0 *e* " + dquote + "dot" + dquote + "))\n(0 (0 *e* " + dquote + "quuestion" + dquote + "))\n"
	#line_str = line_str + "(0 (0 *e* " + dquote + "exclamation" + dquote + "))\n(0 (0 *e* " + dquote + "tdot" + dquote + "))\n"
	#line_str = "(c0 (c0 *e* " + dquote + "end" + dquote + "))\n"

	#text_file.write(line_str)

        for c in range(number_of_cluster):
                for d in range(number_of_cluster):
			state1 = "c" + str(c)
			state2 = "c" + str(d)
			equals = dquote + state2 + dquote
                        line_str = "(" + state1 + " (" + state2 + " *e* " + equals + "))\n"
                        text_file.write(line_str)

        text_file.close()

def generate_fst(words, number_of_cluster):
	#fst_file_name = os.getcwd() + "/" + file_name[:-4] + ".fst"
	text_file = open("train.fst", "w")
	text_file.write("c0\n")
	dquote = '"'

	for e in range(number_of_cluster):
		for f in range(len(words)):
			label = "c" + str(e)
			line_str = "(c0 (c0 " + dquote + label + dquote + " " + words[f] + "))\n"
			text_file.write(line_str)
	text_file.close()

def main_create_fsa_fst(number_of_cluster):
	words = generate_word_list()
	generate_fsa(number_of_cluster)
	generate_fst(words, number_of_cluster)


