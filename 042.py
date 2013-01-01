#! /usr/bin/env python
#-*- encoding: utf-8 -*-
#文章中に出現するすべての動詞を抜き出せ．

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
        #SplitFeature = node.feature.split(",") #debug
        if (31 <= node.posid and node.posid <=33):#posidによるフィルタ
            print node.surface#+": "+SplitFeature[0] 
        node = node.next
