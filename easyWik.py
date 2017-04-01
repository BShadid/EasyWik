#!/usr/bin/env python2.7

# This file is the main driver file and the one that interacts with the wikipedia API endpoints.

from contextlib import contextmanager
from commonwords import exclude
import wikipedia
import re
import json
import unicodedata
import string
import sys
import os
import string

# print wikipedia.summary("Treap")
'''
@contextmanager
def suppress_error():
	with open("trash.log", "w") as devnull:
		orig_stderr = sys.stderr
		sys.stderr = devnull
		try:
			devnull.write( #ERROR
		finally:
			sys.stderr = orig_stderror'''


def prep():
	while (True):	
		query = raw_input("What would you like to search?  ")
		try:
			response = wikipedia.WikipediaPage(query)
			break
		except wikipedia.exceptions.PageError:
			print "That Wikipedia article does not exist, and no valid suggestions could be made."
		except wikipedia.exceptions.DisambiguationError:
			print "Multiple articles matched this name. Try to be more specific."
			print "Here is a list of possibly related articles:"
			print " "
			dummy = wikipedia.WikipediaPage(query) #Automatically breaks the script, no way to capture stderr


	links_master = [ str(i.encode('ascii','ignore')) for i in response.links ]
	s = response.content
	section_names = [i.strip() for i in re.findall("==([^=]+)==", s.encode('ascii','ignore'))]
	sections_content = []

	sections_content.append(("Summary", str(unicodedata.normalize("NFKD",wikipedia.summary(query)).encode('ascii','ignore')).split(". ")))
	for i in section_names:
		temp = response.section(i)
		try:
			sections_content.append((i, (str(temp.encode('ascii','ignore')).split("."))))
		except AttributeError:
			continue

	for i in sections_content:
		if i[0] == "See also":
			break
		print i[0] + ": "
		print " "
		for j in i[1]:
			print j.strip()
			
		print " "


	#s.encode('ascii','ignore')

	#print s
	#print " "

	#q_resp = wikipedia.summary(query)
	#unicodedata.normalize("NFKD",q_resp).encode('ascii','ignore')
	#data_list = q_resp.split(".")
	#sentence_list = [ i.encode('ascii','replace').strip() for i in data_list ]
	#print sentence_list

if __name__=="__main__":
	prep()

