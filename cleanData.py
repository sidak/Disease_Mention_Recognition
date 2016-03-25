import pandas as pd 
import numpy as np 
import sys

input_filename = './' + sys.argv[1]
output_filename = './' + sys.argv[2]

cols =['s.no', 'headline text', 'timestamp1', 'timestamp2', 'num1' , 'num2', 'num3', 'link', 'num4']

data = pd.read_csv(input_filename, header = None, names = cols)

print "original data\n"
print data.info()

data.drop_duplicates(subset='link', inplace = True)
data.drop_duplicates(subset='headline text', inplace = True)
data.dropna(inplace = True)

print "cleaned data\n"
print data.info()

data.to_csv(output_filename)
