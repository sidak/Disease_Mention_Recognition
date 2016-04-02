import pandas as pd 
import numpy as np 
import sys
import nltk

input_filename = './' + sys.argv[1]
output_filename = "./" + sys.argv[2]

def reverse(sentence):
    answer = ''
    temp = ''
    for char in sentence:
        if char != ' ':
            temp += char
        else:
            answer = temp + ' ' + answer
            temp = ''
    answer = temp + ' ' + answer
    return answer

 
with open(input_filename) as f:
    content = f.readlines()

output_file = open(output_filename, "w")


for hline in content:
	words = nltk.word_tokenize(hline)
	pos = nltk.pos_tag(words)
	
	flag =0 
	idx = -1
	for i, (key, val) in enumerate(pos):
		if(key.lower()=='symptom' or key.lower()=='symptoms'):
			idx = i
			break
		

	disease_name=""
	if idx!=-1:
			pos2 = pos[:idx]
			pos1 = pos2[::-1]
			flag1 = 0
			for i, (key,val) in enumerate(pos1):
				if val == 'NN' or val == 'NNP' or val == 'NNS'or val == 'NNPS'or val == 'CD' :
					flag1 = 1;
					if i>0 and (pos1[i-1][1] == 'NN' or pos1[i-1][1] == 'NNP'or pos1[i-1][1] == 'NNS' or pos1[i-1][1] == 'NNPS ' or pos1[i-1][1] == 'CD' or pos1[i-1][1] == 'JJ'):
						disease_name+= " "+key	
					elif i==0:
						disease_name+= " "+key
				
				elif val == 'JJ' and not flag1:
					disease_name+= " "+key

				else:
					break

			disease_name = reverse(disease_name)	
			disease_name+= "\n"
			output_file.write(disease_name)
	
		
