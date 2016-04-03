import sys
import nltk

disease_syns =[
	"disease",
	"diseases",
	"infection",
	"infections",
	"illness",
	"ilnesses",
	"injury",
	"injuries",
	"bruise",
	"bruises",
	"virus",
	"fever"
]

natural_disasters=[
	"hurricane",
	"tsunami",
	"tornado",
	"earthquake",
	"flood",
	"wildfire",
	"drought",
	"avalanche",
	"landslide"
]
def filterDiseaseSynonyms(str):
	
	lower_str = (str.lower()).strip()
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

def filterNaturalDisasters(str):
	
	lower_str = (str.lower()).strip()
	isPresent = 0
	for syn in natural_disasters:
		if(lower_str==syn):
			print "lower_str is "
			print lower_str
			isPresent = 1
			break

	if(isPresent == 1):
		return False 
	else: 
		return True	
