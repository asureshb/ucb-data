#!/usr/local/bin/python

#
#  PyParagraph/main.py is to calculate and display text metrics
#  Syntax: python PyParagraph/main.py <text_file_path>
#

#import all required modules here
import re
import sys

def textAnalytics(text_file):
    with open(text_file, 'r') as fd:
        text = fd.read()

    sentences  = re.split(r' *[\.\?!][\'"\)\]]* +', text)
    words = re.findall(r'\w+', text)

    print("Number of sentences: " + str(len(sentences)))
    print("Number of words: " + str(len(words)))

    # calculate average letter count
    char_count = 0
    for w in words:
        char_count += len(w)
    print("Average letter count: %s" % str(char_count / len(words)))

    # calculate average length of sentence
    sentence_count = 0
    for s in sentences:
        sentence_count += len(s)
    print("Average sentence length: %s" % str(sentence_count / len(sentences)))

if __name__ == '__main__':
    textAnalytics(sys.argv[1])
