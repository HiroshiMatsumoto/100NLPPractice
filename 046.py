#! /usr/bin/env python
#-*- coding:utf-8 -*-
#(46) 文章中のすべての名詞の連接（１形態素以上）を抜き出せ．

from HiroshiLib import OneLineEach
import MeCab
    

inFile = open("JpData.txt","r")
mecab = MeCab.Tagger("-Ochasen")

EachLineList = list()
for line in inFile.readlines():
    EachLineList += OneLineEach(line)

counter=1
output = ""
for line in EachLineList:
    node = mecab.parseToNode(line)
    node = node.next
    while node:
        if (36<= node.posid and node.posid <=67):#Noun
            output += node.surface
            node = node.next
            while True:
                if (36<= node.posid and node.posid <=67):#Noun
                    output += node.surface
                    node = node.next      
                    counter += 1
                else:
                    print counter,
                    print ": "+output
                    output=""
                    counter = 1
                    break
        node = node.next
        


