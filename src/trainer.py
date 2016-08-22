import os

def main_trainer(number_of_iteration):
	command_str = "carmel --train-cascade -HJ -! " + number_of_iteration + " train.data train.fsa train.fst"
	os.system(command_str)

	command_str = "carmel --project-right --project-identity-fsa -HJ train.fsa.trained > train.fsa.trained.noe "
	os.system(command_str)

	command_str = "awk 'NF>0' train.data > train.data.noe"
	os.system(command_str)

	command_str = "cat train.data.noe | carmel -qbsriWIEk 1 train.fsa.trained.noe train.fst.trained > results.txt"
	os.system(command_str)
