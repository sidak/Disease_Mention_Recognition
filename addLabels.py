import pandas as pd 
import numpy as np 
import sys

input_filename = './' + sys.argv[1]
disease_filename = "./" + sys.argv[2]


data = pd.read_csv(input_filename)

diseases = [disease.rstrip('\n') for disease in open(disease_filename, "r")]
diseases = set(diseases)

def diseases_in_string(str):
    return diseases.intersection(str.split())

label =[]

for frame in data.head(1000)['headline text']:
	headline = frame.lower()
	print headline
	headline_diseases = diseases_in_string(headline)
	if len(headline_diseases) > 0 :
		label.append(1)
		print "headline containing diseases is "
		print headline
		print "diseases are "
		print headline_diseases
		print "\n"
	else:
		label.append(0)

print diseases

