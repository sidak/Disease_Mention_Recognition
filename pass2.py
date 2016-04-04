#get data from files
#insert it into maps
#assign weights 

import sys
import os
import subprocess
import operator
from os import path

dir_path = './data/disease_names/'
output_filename = './analysis/' + sys.argv[1]
output_total_disease = './analysis/' + sys.argv[2]
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
				total_disease_set[line] = 0
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

output_disease_file = open(output_total_disease, "w")

for disease in total_disease_set:
	cmd_str = "grep -i -w -c " + "\"" + disease + "\"" + " ./data/headline_text/2014_headline_text.txt"
	total_disease_set[disease] = subprocess.call(cmd_str, shell = True)
	print total_disease_set[disease]
	output_disease_file.write(disease+"--")
	if(total_disease_set[disease] == 0):
		output_disease_file.write("0")
	else:
		output_disease_file.write(total_disease_set[disease])
	output_disease_file.write("\n")


for root in root_based_dictionary:
	print "------------------" + root + " starts------------------"
	#weight[root] = len(root_based_dictionary[root])
	#total = total + weight[root]
	print root_based_dictionary[root]
	print diseases[root]

#for root in root_based_dictionary:
#	weight[root] = weight[root]/total

#equal weights for now
print "---------------weights assigned----------------"

#frequency analysis begins

for disease in disease_set:
	for root in root_based_dictionary:
		if(disease in root_based_dictionary[root]):
			disease_set[disease] = disease_set[disease] + (weight[root]*1000 * ((root_based_dictionary[root][disease]*1.0)/total_disease_set[disease]))
			file_set[disease] = file_set[disease] + root + ", "

sorted_disease_set = sorted(disease_set.items(), key=operator.itemgetter(1), reverse = True)
print sorted_disease_set

print "---------------frequency analysis done--------------"

output_file = open(output_filename, "w")

for key,value in sorted_disease_set:
	output_file.write(key + "------ ")
	output_file.write(file_set[key])
	output_file.write("\n")

for key in weight:
	print key
	print weight[key]



#

