#get data from files
#insert it into maps
#assign weights 

import sys
import os
import commands
import subprocess
import operator
from subprocess import Popen, PIPE
from os import path

dir_path = './data/disease_names/'
output_filename = './analysis/' + sys.argv[1]
output_total_disease = './analysis/' + sys.argv[2]
input_filename = './analysis/total_diseases.txt'

#read file names and there content	

root_based_dictionary = {}
disease_set = {}
file_set = {}
diseases = {}
total_disease_set = {}

for fil in os.listdir(dir_path):
	disease_count = 0
	filename = fil[:-4]
	with open(dir_path+fil) as f:
		content = f.readlines()
		disease_dictionary = {}

	for line in content:
		line = line.strip()
		line = line.lower()
		if(line != ''):
			disease_count = disease_count + 1
			if(line in disease_dictionary):
				disease_dictionary[line] = disease_dictionary[line] + 1
			else:
				disease_dictionary[line] = 1
				disease_set[line] = 0
				total_disease_set[line] = 1
				file_set[line] = " "

	diseases[filename] = disease_count
	root_based_dictionary[filename] = disease_dictionary

print "---------------dictionary created--------------"

#assign weights 
weight = {}
weight["vaccine_diseases"] = 34.0/38
weight["diagnose_diseases"] = 10.0/14
weight["died_of_diseases"] = 37.0/69
weight["treatment_diseases"] = 78.0/308.0
weight["diagnoses_diseases"] = 4.0/8
weight["battling_with_diseases"] = 2.0/4
weight["diagnosed_by_diseases_1"] = 3.0/4
weight["symptom_diseases"] = 25.0/31
weight["cure_diseases"] = 13.0/30
weight["diagnosis_diseases"] = 21.0/27
weight["battling_diseases"] = 22.0/87
weight["diagnosed_with_for_diseases"] = 78.0/85
weight["outbreak_diseases"] = 102.0/128
weight["outbreak_of_diseases"] = 3.0/7
weight["hospital_with_diseases"] = 12.0/14
weight["virus_diseases"] = 80.0/146.0
weight["treatment_for_diseases"] = 8.0/25.0

print "---------------weights assigned----------------"

#get total number of diseases (we got from pass1) in the file

# for disease in total_disease_set:
# 	cmd_str = "grep -i -w -c " + "\"" + disease + "\"" + " ./data/headline_text/2014_headline_text.txt"

# 	total_disease_set[disease] = commands.getstatusoutput(cmd_str)[1]
# 	print disease + " - -- " + str(total_disease_set[disease])
# 	output_disease_file.write(disease+"--")
# 	output_disease_file.write(str(total_disease_set[disease]))
# 	output_disease_file.write("\n")

output_disease_file = open(output_total_disease, "w")

with open(input_filename) as f:
    content = f.readlines()

for line in content:
	line = line.strip("\n")
	x = line.split("--")

	if(x[1] != ''):
		x[1] = int(x[1])

	if (isinstance(x[1], (int, long))):
		total_disease_set[x[0]] = int(x[1])
	else:
		total_disease_set[x[0]] = 1

print "---------------diseases extracted----------------"


#frequency analysis begins

disease_in_features = {}

#get disease names in features

for disease in total_disease_set:
	disease_in_features[disease] = 0
	for root in root_based_dictionary:
		if(disease in root_based_dictionary[root]):
			disease_in_features[disease] = disease_in_features[disease] + root_based_dictionary[root][disease]


output_file = open(output_filename, "w")

#calculate probability

for disease in disease_set:
	for root in root_based_dictionary:
		if(disease in root_based_dictionary[root]):
			if(total_disease_set[disease] >= 1):

				if(total_disease_set[disease] < root_based_dictionary[root][disease]):
					total_disease_set[disease] = root_based_dictionary[root][disease]

				#calculate probability with normalized weights
					
				disease_set[disease] = disease_set[disease] + (weight[root] * ((root_based_dictionary[root][disease]*1.0)/total_disease_set[disease]))
				file_set[disease] = file_set[disease] + root + ", "

sorted_disease_set = sorted(disease_set.items(), key=operator.itemgetter(1), reverse = True)

#print sorted_disease_set

print "---------------frequency analysis done--------------"

for key,value in sorted_disease_set:
	output_file.write(key + "--")
	output_file.write(file_set[key])
	output_file.write("\n")
