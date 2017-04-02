#!/usr/bin/env python2.7

import math                         # so we can do math
import requests
import re

def idf(term, collection):          # inverse document frequency for term

    n = collection["TOTDOCS"]        # total number of documents
    if term in collection:
        return math.log(1 + int(n)/int(collection[term]))
    else:
        return math.log(1 + int(n))



def tfidf (docName, masterFile):
    n = 10
    ranking = {}
    collection = tfidf_load(masterFile)

    docName = docName.replace(" ", "_")
    document = tfidf_wc(docName)

    for word, count in document.items():
        ranking[word] = ((1 + math.log(int(count))) * idf(word, collection))

    output = []
    for rank, word in enumerate(sorted(ranking, key=ranking.get, reverse=True)):
        if rank >= n:
            break
        output.append(word)

    return output

def tfidf_load(filename):
    output = {}
    with open(filename) as f:
        lines = f.readlines()
        entry = [line.rstrip() for line in lines]
        entries = [x.split() for x in entry]
        for i in range(len(entries)):
            output[entries[i][0]] = entries[i][1]

    return output

def tfidf_wc(docName):
    docName = docName.replace("_", "%20")
    reg = '[A-Za-z]+'

    try:
        url = 'https://en.wikipedia.org/w/api.php?action=query&titles={}&prop=revisions&rvprop=content&format=json'.format(docName)
        pass
    except:
        print "error that's not a webpage"

    r = requests.get(url)
    r = r.json()
    r = r['query']
    r = r['pages']
    r = r[r.keys()[0]]
    r = r['revisions']
    r = r[0]
    r = r['*']

    ret = re.findall(reg, r)
    wordCount = {}
    for word in ret:
        word = word.lower()
        wordCount.setdefault(word, 0)
        wordCount[word] += 1

    return wordCount
