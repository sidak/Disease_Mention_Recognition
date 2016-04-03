import sys
import nltk
import re
from preprocess import *
from filters import *

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

def filter_dname_virus(disease_name):
	if 'like' in disease_name:
		disease_name = re.sub('- *like *$', '', disease_name)
	output_file.write(disease_name)
 
with open(input_filename) as f:
    content = f.readlines()

output_file = open(output_filename, "w")


for hline in content:
	words = nltk.word_tokenize(lowercaseAndAbbreviate(hline))
	pos = nltk.pos_tag(words)
	
	flag =0 
	idx = -1
	for i, (key, val) in enumerate(pos):
		if(key.lower()=='virus' or key.lower()=='viruses'):
			idx = i
			break
		

	disease_name=""
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

		disease_name = reverse(disease_name)	
		if filters.filterDiseaseSynonyms(disease_name):
			disease_name+= "\n"
			filter_dname_symptoms(disease_name)
	
		
