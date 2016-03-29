import pandas as pd 
import numpy as np 
import sys

input_filename = './' + sys.argv[1]
output_filename ="./" + sys.argv[2]

data = pd.read_csv(input_filename)


headlines = data['headline text']
headlines.to_csv(output_filename)
