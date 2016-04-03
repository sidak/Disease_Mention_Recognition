

import pandas as pd 
import numpy as np 
import sys
import nltk
import filters
import preprocess

input_filename = './' + sys.argv[1]
output_filename = "./" + sys.argv[2]

with open(input_filename) as f:
    content = f.readlines()

output_file = open(output_filename, "w")


for hline in content:
	words = nltk.word_tokenize(preprocess.lowercaseAndAbbreviate(hline))
	pos = nltk.pos_tag(words)
	
	flag =0 
	idx = -1
	for i, (key, val) in enumerate(pos):
		if(key.lower() == 'patients' or key.lower() == 'patient'):
			flag =1 
		if((key.lower()!='of' and key.lower()!='with' and key.lower()!= 'suffering') and flag ==1):
			idx = i
			break

	disease_name=""

	# 2-gram
	if idx!=-1:
		seenAdj = 0
		seenNoun = 0
		while(idx>=0):
			(key, val) = pos[idx]
			
			if(val == 'JJ' and seenNoun == 1):
				seenAdj = 1
				disease_name= key+" " + disease_name
			elif((val == 'NN' or val == 'NNP') and seenAdj == 0):
				seenNoun = 1
				disease_name= key+" " + disease_name
			else:
				break
			idx -=1	

		if filters.filterDiseaseSynonyms(disease_name):
			disease_name+= "\n"
			if disease_name!="\n":
				output_file.write(disease_name)

