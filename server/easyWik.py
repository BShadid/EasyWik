#!/usr/bin/env python2.7

# This file is the main driver file and the one that interacts with the wikipedia API endpoints.
# CHANGE 1: This will now be treated as a library

from commonwords import exclude
import requests
import wikipedia
import re
import json
import unicodedata
import string
import sys
import os
import string
import tfidf
import nltk

#GLOBALS

def usage(status=0):
	print '''
	How to use: {} -q search

	-q		The thing you want to learn about
	'''.format(os.path.basename(sys.argv[0]))
	sys.exit(status)

def run_main(query, query2, KEY):
	'''ANSWER = ""
	while (True):
		
		#if len(QUERY) == 0:
		#	query = raw_input("What would you like explained?  ")
		#else:
		#	query = QUERY
		try:
			response = wikipedia.WikipediaPage(query)
			break
		except wikipedia.exceptions.PageError:
			print "That Wikipedia article does not exist, and no valid suggestions could be made."
			return
		except wikipedia.exceptions.DisambiguationError:
			print "Multiple articles matched this name. Try to be more specific."
			print "Here is a list of possibly related articles:"
			print " "
			dummy = wikipedia.WikipediaPage(query) #Automatically breaks the script, no way to capture stderr


	#links_master = [ str(i.encode('ascii','ignore')).lower().split() for i in response.links ]
	#Build the list of links, these are used as 'important keywords' for now

	

	links_master = tfidf.tfidf(query, "masterDic.txt")
#	for i in response.links:
#		x = str(i.encode('ascii','ignore')).lower().split()
#		for j in x:
#			links_master.append(j.translate(None, string.punctuation))
#	for i in query.split(" "):
#		links_master.append(i)

	s = response.content
	#print (s.encode('ascii', 'ignore')).lower()
	section_names = [i.strip() for i in re.findall("==([^=]+)==", s.encode('ascii','ignore'))]
	sections_content = [ i.strip() for i in re.findall("([^=]+)[=]+", s.encode('ascii','ignore'))]
	sections_content.append(("Summary", str(unicodedata.normalize("NFKD",wikipedia.summary(query)).encode('ascii','ignore')).split(". ")))
	#print sections_content[0:4]
	for i in section_names:
		temp = response.section(i)	
		try:
			sections_content.append((i, (str(temp.encode('ascii','ignore')).split(". "))))
		except AttributeError:
			continue

	for i in sections_content:
		sentences = []
		current_words = []
		if i[0] == "See also":
			break
		if len(i[1][0]) > 0:
			#ANSWER += i[0] + ": "
			#ANSWER += " "
			for sentence in i[1]:
				sentence.replace('\n', " ")
				word_list = sentence.replace("\n"," ").split(" ")

				if (set(word_list) & set(links_master)): # Checks for any common element as hash table representations, search is O(1)
					current_words = sentence.strip().replace('\n',' ').split(" ")
				else:
					continue # if it doesn't have a common word with the links set, don't include it in the sentence list

				edited_words = []

				parenths = False
				for k in range(len(current_words)):
					if current_words[k].startswith("("):
						parenths = True

					elif ")" in current_words[k]:
						parenths = False
						continue
						
					if not (parenths):
						current_words[k].translate(None, string.punctuation)
						current_words[k]=exclude(current_words[k], links_master)
						edited_words.append(current_words[k])


				sentences.append(edited_words)

			for j in sentences:
				ANSWER += " ".join(j) + ". "
#					print " ".join(k)
			del sentences[:]

#			print " "
	'''
	#urlify = re.sub(r"\s+", '_', query)
	url = "http://api.summry.com/&SM_API_KEY={}&SM_LENGTH=5&SM_URL=http://en.wikipedia.org/wiki/{}".format(KEY, query2)
	summary_verified = requests.post(url)
	#sv = json.loads(summary_verified.json())
	summary_text = sv['sm_api_content']
	summary_text.replace("Summary:", query)
	
	return summary_text
	

	#q_resp = wikipedia.summary(query)
	#unicodedata.normalize("NFKD",q_resp).encode('ascii','ignore')
	#data_list = q_resp.split(".")
	#sentence_list = [ i.encode('ascii','replace').strip() for i in data_list ]
	#print sentence_list
'''
if __name__=="__main__":
	args = sys.argv[1:]
	while len(args) and args[0].startswith('-') and len(args[0])>1:
		arg = args.pop(0)
		if arg == '-q':
			QUERY = args.pop(0)
		elif arg == '-h':
			usage(0)
		else:
			usage(1)

	if len(args) > 0:
		if not args[0].startswith('-'):
			usage (1)

	run_main()
'''

