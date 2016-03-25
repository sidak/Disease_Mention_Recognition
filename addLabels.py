import pandas as pd 
import numpy as np 
import sys

input_filename = './' + sys.argv[1]
disease_filename = "./" + sys.argv[2]
label_filename = "./" + sys.argv[3]
disease_headlines_filename ="./" + sys.argv[4]

data = pd.read_csv(input_filename)

diseases = [disease.rstrip('\n') for disease in open(disease_filename, "r")]
diseases = set(diseases)

def diseases_in_string(str):
    return diseases.intersection(str.split())

label =[]

imp_headlines =[]

num = 0

for frame in data['headline text']:
	headline = frame.lower()
	print "headline is : " + headline

	headline_diseases = diseases_in_string(headline)
	print "headline diseases is : "
	print headline_diseases
	
	if len(headline_diseases) > 0 :
		label.append(1)
		print "headline containing diseases is "
		print headline
		print "diseases are "
		print headline_diseases
		print "\n"
		num+= 1
		imp_headlines.append(frame)
	else:
		label.append(0)

print label

data['label'] = label
data.to_csv(label_filename)

disease_headlines_file = open(disease_headlines_filename, "w")
for item in imp_headlines:
	disease_headlines_file.write("%s\n" % item)

print "the number of headlines with diseases is "
print num