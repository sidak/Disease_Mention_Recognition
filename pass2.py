#get data from files
#insert it into maps
#assign weights 

import sys
import os
import operator
from os import path

dir_path = './analysis/pass1_output/'
output_filename = './analysis/' + sys.argv[1]
#read file names and there content	

root_based_dictionary = {}
disease_set = {}

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
				disease_set[line] = 0

	root_based_dictionary[filename] = disease_dictionary

print "---------------dictionary created--------------"

#assign weights 
weight = {}
#equal weights for now
print "---------------weights assigned---------------"

#frequency analysis begins

for disease in disease_set:
	for root in root_based_dictionary:
		if(disease in root_based_dictionary[root]):
			disease_set[disease] = disease_set[disease] + root_based_dictionary[root][disease] + 10

sorted_disease_set = sorted(disease_set.items(), key=operator.itemgetter(1), reverse = True)
# print sorted_disease_set

print "---------------frequency analysis done--------------"

output_file = open(output_filename, "w")

for key,value in sorted_disease_set:
	output_file.write(key)
	output_file.write("\n")

