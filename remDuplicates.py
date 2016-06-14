#This function returns a new string with duplicate words removed from an old string

from collections import OrderedDict # don't forget the module

def remDuplicates(os):
	string = map(str, os.split())
	output = ""
	for item in list(OrderedDict.fromkeys(string)):
		output+=item+" "
	return output
