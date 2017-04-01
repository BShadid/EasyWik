#!/usr/bin/env python2.7

# commonwords.py :: python library for replacing words with more common words
# uses list of 2000 most common words from
#	  http://www.talkenglish.com/vocabulary/top-2000-vocabulary.aspx

import string

commonwords = []

with open("top2000words.txt",'r') as f:
  for word in f.read().split("\n"):
    commonwords.append(word)

def exclude(word, links):
  if word in commonwords or len(word) < 5 or word[0].isupper():
    return False
  else:
    if word in links:
      return False
    else:
      return True
