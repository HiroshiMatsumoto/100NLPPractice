#! /usr/bin/env python
#-*- encoding:utf-8 -*-

import re
import sys
import marshal

inFile = open("030out.txt","r")

dictData = open("032out.txt","r")
Dict = marshal.load(dictData)

wordCount = {}

for input in inFile:
    item = re.match("^(.*?)\t(.*?)\t(.*?)$", input.strip("\n"))
    word = item.group(2)
    if Dict.has_key(word): #もしデータが辞書にあって
        if word in wordCount: #すでに登場単語リストに登録されていて
#           if wordCount[word] == 3:#登場単語が３回なら 
#                print word+":",wordCount[word] #出力
            wordCount[word] += 1
        else:
            wordCount[word] = 1

for item in wordCount:
    if wordCount[item] >= 3:
        print item+":",wordCount[item]


