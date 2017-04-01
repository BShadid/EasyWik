#!/usr/bin/env python2.7

import math                         # so we can do math

"""
def tf(term, document):             # term frequency for term in document
    count = 0                       # how many times term appears in document
    for word in document.split():   # for every word in the document
        if word is term:            # every time a match is found
            count+= 1               # add one to count

    return 1 + log(count)           # return the frequency

"""
def idf(term, collection):          # inverse document frequency for term

    n = collection["TOTDOCS"]        # total number of documents
    if term in collection:
        return math.log(1 + int(n)/int(collection[term]))
    else:
        return math.log(1 + int(n))

"""    for document in collection:     # for every document in the collection
        words = set(document.split())   # set of words in the document 
        if term in words:           # if the term is in the document
            count+= 1               # add one to the count of documents
            continue                # stop checking that document
"""


def tfidf (document, filename):
    n = 2
    ranking = {}
    collection = tfidf_load(filename)
    for word, count in document.items():
        ranking[word] = ((1 + math.log(int(count))) * idf(word, collection))

    print ranking

    output = []
    for rank, word in enumerate(sorted(ranking, key=ranking.get, reverse=True)):
        print rank, word
        if rank >= n:
            break
        print "appended ", word
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
            print "added ", entries[i][0], entries[i][1]

    return output
