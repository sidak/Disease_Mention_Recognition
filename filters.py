import pandas as pd 
import numpy as np 
import sys
import nltk

disease_syns =[
	"disease ",
	"diseases ",
	"infection ",
	"infections ",
	"illness ",
	"ilnesses ",
	"injury ",
	"injuries ",
	"bruise ",
	"bruises "
]
def filterDiseaseSynonyms(str):
	lower_str = str.lower()
	isPresent = 0
	for syn in disease_syns:
		if(lower_str==syn):
			print "lower_str is "
			print lower_str
			isPresent = 1
			break

	if(isPresent == 1):
		return False 
	else: 
		return True	