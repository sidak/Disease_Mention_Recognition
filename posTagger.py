import pandas as pd 
import numpy as np 
import sys
import nltk

input_filename = './' + sys.argv[1]
pos_tagged_filename = "./" + sys.argv[2]

data = pd.read_csv(input_filename)

pos_tagged_file = open(pos_tagged_filename, "w")

for frame in data['headline text']:
	words = nltk.word_tokenize(frame)
	pos = nltk.pos_tag(words)
	for (key, val) in pos:
		pos_tagged_file.write("(%s, %s) " % (key, val))
		
	pos_tagged_file.write("\n")
