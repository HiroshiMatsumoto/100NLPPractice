#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re

def Ngram(Content, N):
    FreqNgramList = {}
    for line in Content:
        for i in range(len(line)):
            if i+N < len(line):
                word = line[i:i+N]#line[i:i+N] iからi+N-1までの文字列
                if FreqNgramList.has_key(word):
                    FreqNgramList[word]+=1
                else:
                    FreqNgramList[word]=0
    return FreqNgramList

N = 2
Content = open("025out.txt","r")
FreqBigramList = Ngram(Content, N)
Content.close()
for key, value in sorted(FreqBigramList.items(), key=lambda x:x[1]):
    print r"%s:%d" % (key, value)
