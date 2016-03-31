import pandas as pd 
import numpy as np 
import sys
import nltk

input_filename = './' + sys.argv[1]
output_filename = "./" + sys.argv[2]

with open(input_filename) as f:
    content = f.readlines()

output_file = open(output_filename, "w")


for hline in content:
	words = nltk.word_tokenize(hline)
	pos = nltk.pos_tag(words)
	

	flag =0 
	idx = -1
	for i, (key, val) in enumerate(pos):
		if(key.lower() == 'cure' or key.lower() == 'cured'):
			flag =1 
		if((key.lower()!= 'of' and key.lower()!= 'for') and flag ==1):
			idx = i
			break

	disease_name=""

	# 2-gram
	if idx!=-1:
		pos1 = pos[:idx]
		flag1 = 0
		if(pos1[idx-1] == 'NN' or pos1[idx-1] == 'NNP' or pos1[idx-1] == 'NNS' or pos1[idx-1] == 'NNPS')
			if(pos1[idx-2] == 'NN' or pos1[idx-2] == 'NNP' or pos1[idx-2] == 'NNS' or pos1[idx-2] == 'NNPS')
				disease_name+= key+" "
			disease_name+= key
			disease_name+= "\n"
			output_file.write(disease_name)
