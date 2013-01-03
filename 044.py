#! /usr/bin/env python
#-*- encoding:utf-8 -*-
#(44)サ変名詞をすべて抜き出せ．
from HiroshiLib import OneLineEach
import MeCab

inFile = open("JpData.txt","r")
mecab = MeCab.Tagger("-Ochasen")

EachLineList = list()
for line in inFile.readlines():
    EachLineList += OneLineEach(line)

for line in EachLineList:
    node = mecab.parseToNode(line)
    node = node.next
    while node:
        if (36<= node.posid and node.posid <=67):#名詞
            SplitFeature = node.next.feature.split(",")            
            if(SplitFeature[6]=='する'):#原形:する
                print node.surface+node.next.surface
                node = node.next
        node = node.next



