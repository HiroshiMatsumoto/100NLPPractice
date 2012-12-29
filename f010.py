#! /usr/bin/env python
# -*- coding: utf-8 -*-
#Input: Input must be in this style: \w*\t\w*\n
#Output: This returns dictionary type {word:'hoge', frequency:987}
import re
import csv

def RankList(file):
    FileContents = open(file, "r")
    dictFreqWords = {}   
    for line in FileContents:
        MatchedWords = re.match("^(.*)\t(.*)$",line)
        Word = MatchedWords.group(2)
        if dictFreqWords.has_key(Word):
            dictFreqWords[Word] += 1
        else:
            if not re.match("^[a-zA-Z0-9 -/:-@\[-\`\{-\~]+$",Word):
                dictFreqWords[Word] = 0
            else:
                dictFreqWords[Word.decode('utf-8')] = 0
    FileContents.close()
    return dictFreqWords

if __name__ == '__main__':
    print "RankList(file) returns a list of words"
