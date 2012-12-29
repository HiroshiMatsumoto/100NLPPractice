#! /usr/bin/env python
#-*- coding:utf-8 -*-

from stemming.porter2 import stem
import re
inFile = open("025out.txt","r")
outFile = open("030out.txt", "w")

for Line in inFile:
    Line = Line.strip("\n")
    Words = re.match("^(\w*)\t(\w*)$",Line)
    #NewLine = Words.group(1)+"\t"+Words.group(2)+"\t"+stem(Words.group(2))
    if Words:
        outFile.write(Words.group(1)+"\t"+Words.group(2)+"\t"+stem(Words.group(2))+"\n")

inFile.close()
outFile.close()
