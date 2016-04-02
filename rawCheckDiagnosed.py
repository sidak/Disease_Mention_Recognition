import pandas as pd 
import numpy as np 
import sys
import nltk

input_filename = './' + sys.argv[1]
output_filename = "./" + sys.argv[2]

with open(input_filename) as f:
    content = f.readlines()

def isUpper(char):
	if(char>='A' and char<='Z'):
		return True
	else: 
		return False

def lowercaseAndAbbreviate(str):
	lowercase = str.lower()
	prevCap = 0
	startCapIdx = -1
	
	if(isUpper(str[0])):
		prevCap = 1
		startCapIdx = 0
	
	i= 1

	while(i<len(str)):
		if(prevCap == 0 and isUpper(str[i])):
			prevCap = 1
			startCapIdx = i
		elif(prevCap == 1 and (not isUpper(str[i]))):
			if((i-startCapIdx)>1):
				abbvn = str[startCapIdx:i]
				lowercase = lowercase.replace(abbvn.lower(), abbvn)
			elif((str[i]>='a' and str[i]<='z') or (str[i]>='0' and str[i]<='9')):
				j = i 
				while(j<len(str) and str[j]!=' ' and str[j]!='.' and str[j]!=',' and str[j]!='?' and str[j]!=':' and str[j]!=';'):
					j+=1
				word = str[startCapIdx:j]
				word = word.lower()
				words = nltk.word_tokenize(word)
				tags = nltk.pos_tag(words)
				(key, val) = tags[0]
				if(val == 'NN' or val == 'NNP'):
					abbvn = str[startCapIdx:i]
					lowercase = lowercase.replace(word, str[startCapIdx:j])

			prevCap = 0 

		i+=1

	return lowercase

def get_disease_name_diagnoses(pos):
	idx = -1
	direc = 'o'
	flag = 0 
	for i, (key, val) in enumerate(pos):
		if(key.lower()=='diagnosed' or key.lower()=='misdiagnosed'):
			if(val == 'VBN'):
				direc = 'r'
				idx = i + 1 
			else:
				direc = 'l'
				idx = i - 1 
			flag = 1
		elif(flag == 1):
			if(key.lower()=='by'):
				direc = 'l'
				idx = i-2
			break	

	disease_name=""

	if idx!=-1:
		if direc == 'r':
			pos1 = pos[idx:]
			flag1 = 0
			for i, (key, val) in enumerate(pos1):
				if val == 'DT' and not flag1:
					continue

				elif val == 'NN' or val == 'NNP' or val == 'NNS'or val == 'NNPS'or val == 'CD' :
					flag1 = 1;
					if i==0:
						disease_name+= key+" "
					elif i>0 and (pos1[i-1][1] == 'NN' or pos1[i-1][1] == 'NNP'or pos1[i-1][1] == 'NNS' or pos1[i-1][1] == 'NNPS ' or pos1[i-1][1] == 'CD' or pos1[i-1][1] == 'JJ'):
						disease_name+= key+" "	

				elif val == 'JJ' and not flag1:
					disease_name+= key+" "

				else:
					break

		else:
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

		disease_name+= "\n"
	
	return disease_name	

output_file = open(output_filename, "w")

for hline in content:
	if('diagnosed' in hline.lower() or 'misdiagnosed' in hline.lower()):
		words = nltk.word_tokenize(lowercaseAndAbbreviate(hline))
		#words = nltk.word_tokenize(hline)

		pos = nltk.pos_tag(words)
		disease_name = get_disease_name_diagnoses(pos)
		if(disease_name!="\n"):
			output_file.write(disease_name)
