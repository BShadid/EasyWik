#!/usr/bin/env python2.7

# commonwords.py :: python library for replacing words with more common words
# uses list of 2000 most common words from
#	  http://www.talkenglish.com/vocabulary/top-2000-vocabulary.aspx


commonwords = []

with open("top2000words.txt",'r') as f:
  for word in f.read().split("\n"):
    commonwords.append(word)

def is_common(word):
  if word in commonwords:
    return True
  else:
    return False
