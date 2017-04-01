#!/usr/bin/env python2.7

# This file is the main driver file and the one that interacts with the wikipedia API endpoints.

from commonwords import exclude
import wikipedia
import re
import json
import unicodedata
import string

# print wikipedia.summary("Treap")


def prep(query):
	response = wikipedia.WikipediaPage(query)
	links_master = [ str(i.encode('ascii','ignore')) for i in response.links ]
	s = response.content
	section_names = [i.strip() for i in re.findall("==([^=]+)==", s.encode('ascii','ignore'))]
	sections_content = []

	for i in section_names:
		temp = response.section(i)
		sections_content.append((i, (str(temp.encode('ascii','ignore')).split("."))))

#	for i in sections_content:
#		print i[0] + ": "
#		print " "
#		for j in i[1]:
#			print j
#			
#		print " "


	#s.encode('ascii','ignore')

	#print s
	#print " "

	#q_resp = wikipedia.summary(query)
	#unicodedata.normalize("NFKD",q_resp).encode('ascii','ignore')
	#data_list = q_resp.split(".")
	#sentence_list = [ i.encode('ascii','replace').strip() for i in data_list ]
	#print sentence_list

if __name__=="__main__":
	query = raw_input("What would you like to search?  ")

prep(query)

#for i in q_response.content:
	#print i

# replacement_json = requests.get(https://wordsapiv1.p.mashape.com/words/ /frequency
