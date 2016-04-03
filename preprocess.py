import pandas as pd 
import numpy as np 
import sys
import nltk

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
