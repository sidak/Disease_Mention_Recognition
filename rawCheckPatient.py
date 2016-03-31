

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
	
	idx = -1
	for i, (key, val) in enumerate(pos):
		if(key.lower() == 'patients' or key.lower() == 'patient'):
			idx = i
			break

	disease_name=""

	if idx!=-1:
		pos1 = pos[:idx]
		flag1 = 0
		if(pos1[idx-1] == 'NN' or pos1[idx-1] == 'NNP' pos1[idx-1] == 'NNS' pos1[idx-1] == 'NNPS')
 
		disease_name+= "\n"
		output_file.write(disease_name)

