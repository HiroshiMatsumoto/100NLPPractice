#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
import marshal

inFile = open("inflection.table.txt","r")
outFile = open("031out.txt","w")

dictInflection = dict()
for Line in inFile:
    splitLine = Line.split("|")
    DefinitionBySpeechPart = dict()
    DefinitionBySpeechPart[splitLine[1]] = dict(conjugation = splitLine[3], base = splitLine[6])
    #print DefinitionBySpeechPart
    if not dictInflection.has_key(splitLine[0]):
        dictInflection[splitLine[0]] = DefinitionBySpeechPart
    else:
        dictInflection[splitLine[0]].update(DefinitionBySpeechPart)        
    #break
#print dictInflection
inFile.close()

while True:
    print "Type in a word (just enter to quit):",
    input = sys.stdin.readline()
    if input=="\n":
        break
    else:
        input = input.strip("\n")
        if dictInflection.has_key(input):
            print dictInflection.get(input),
        else:
            print "Not found:"+input,
    print "\n",
