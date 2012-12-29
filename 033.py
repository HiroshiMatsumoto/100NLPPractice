#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
import marshal

inFile = open("030out.txt","r")
outFile = open("033out.txt","w")

dictData = open("032out.txt","r")
Dict = marshal.load(dictData)

#use the same code from 032.py
for input in inFile:
    input = input.strip("\n")
    item = re.match("^(.*?)\t(.*?)\t(.*?)$", input)
    word = item.group(2)
    if Dict.has_key(word):
        Word = Dict[word]
        print word,":"
        for Def in Word:
            print "\t["+Def+"]:"
            for Spec in Dict[word][Def]:
                print "\t ",
                print Spec.ljust(11),
                print ":",
                print Dict[word][Def][Spec]
            #print Dict.get(input),
        print "\n",

