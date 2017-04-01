#!/usr/bin/env python2.7

# commonwords.py :: python library for replacing words with more common words
# uses list of 2000 most common words from
#	  http://www.talkenglish.com/vocabulary/top-2000-vocabulary.aspx

import string
from PyDictionary import PyDictionary
import requests

commonwords = []

with open("top2000words.txt",'r') as f:
  for word in f.read().split("\n"):
    commonwords.append(word)

def exclude(word, links):
	#dictionary=PyDictionary(word)
	tempword = [word.translate(None, string.punctuation)]
	#tempset.update(tempword)
	if set(tempword) & set(commonwords) or len(tempword) <= 4 or tempword[0].isupper():
		#print set(tempword)
		#print set(commonwords)
		#raw_input(" ")
		return word
	else:
		if tempset & set(links):
			return word
		else:
			try:
				output = str(((requests.get("http://pydictionary-geekpradd.rhcloud.com/api/synonym/{}".format(tempword))).json())[0])
				if word.endswith("'s"):
					output += "'s"
				elif word.endswith("s'"):
					output += "s'"
				return output
			except KeyError:
				return word
