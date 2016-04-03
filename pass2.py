#get data from files
#insert it into maps
#assign weights 

import sys
import os
from os import path

dir_path = './analysis/pass1_output/'

#read file names and there content	

root_based_dictionary = {}

for fil in os.listdir(dir_path):
	filename = fil[:-4]
	with open(dir_path+fil) as f:
		content = f.readlines()
		disease_dictionary = {}

	for line in content:
		line = line.strip()
		if(line != ''):
			if(line in disease_dictionary):
				disease_dictionary[line] = disease_dictionary[line] + 1
			else:
				disease_dictionary[line] = 1

	root_based_dictionary[filename] = disease_dictionary

print root_based_dictionary