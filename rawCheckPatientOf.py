import nltk 
import sys
import preprocess
import filters

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
		if((key.lower()=='of' or key.lower()=='with') and flag ==1):
			idx = i+1
			break

	disease_name=""

	if idx!=-1:
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

		if filters.filterDiseaseSynonyms(disease_name):
			disease_name+= "\n"
			if disease_name!="\n":
				output_file.write(disease_name)

