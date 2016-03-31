import pandas as pd 
import numpy as np 
import sys

input_filename = './' + sys.argv[1]
output_filename ="./" + sys.argv[2]

data = pd.read_csv(input_filename)


headlines = data['headline text']

output_file = open(output_filename, "w")

for hline in headlines:
	output_file.write(hline)
	output_file.write("\n")