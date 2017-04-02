#!/usr/bin/env python2.7

import sys
sys.path.append('./')
import tfidf

import re
import requests

#output = tfidf.tfidf_load("test_load.txt")
#print output

document = {
"kevin":3,
"word":1,
"another":4,
"example":3,
"pepper":2,
"dorito":7,
"sprite":2,
}
#print document
while (1):
        doc = raw_input('enter title: ')
        output = tfidf.tfidf(doc, "masterDic.txt")
        print output
