#get data from files
#insert it into maps
#assign weights 

import sys
import os
import operator
from os import path

dir_path = './data/disease_names/'
output_filename = './analysis/' + sys.argv[1]
#read file names and there content	

root_based_dictionary = {}
disease_set = {}
file_set = {}
diseases = {}

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
				file_set[line] = " "

	diseases[filename] = disease_count
	root_based_dictionary[filename] = disease_dictionary

print "---------------dictionary created--------------"

#assign weights 
weight = {}
weight["Vaccine_diseases"] = 34.0/38
weight["diagnose_diseases"] = 10.0/14
weight["Diedof_Diseases"] = 37.0/70
weight["Treatment_Diseases"] = 50.0/233.0
weight["final_diagnoses_diseases"] = 4.0/8
weight["BattlingWith_diseases"] = 2.0/5
weight["outbreak_of_disease"] = 3.0/14
weight["diagnosed_by_diseases_1"] = 3.0/4
weight["Symptoms_Diseases"] = 25.0/31
weight["cure_diseases"] = 0.0
weight["final_diagnosis_diseases"] = 21.0/27
weight["Battling_diseases"] = 12.0/59
weight["diagnosed_with_for_diseases"] = 78.0/85
weight["outbreak_diseases"] = 92.0/150
weight["hospital_with_diseases"] = 12.0/14


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
			disease_set[disease] = disease_set[disease] + weight[root]*1000 + root_based_dictionary[root][disease]
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

