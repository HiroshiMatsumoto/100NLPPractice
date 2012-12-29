#! /usr/bin/env python
#-*- encoding: utf-8 -*-
import re
import sys
import marshal

inFile = open("030out.txt","r")
outFile = open("034out.txt","w")

dictData = open("032out.txt","r")
Dict = marshal.load(dictData)

for input in inFile:
    item = re.match("^(.*?)\t(.*?)\t(.*?)$", input.strip("\n"))
    word = item.group(2)
    if not Dict.has_key(word):
        outFile.write(word+"\n")


