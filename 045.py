#! /usr/bin/env python
#-*- encoding:utf-8 -*-
#(45) 文章中の「ＡのＢ」という表現（ＡとＢは名詞の１形態素）をすべて抜き出せ．

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
        if (36<= node.posid and node.posid <=67):
            if (node.next.surface=='の'):
                if (36<= node.next.next.posid and node.next.next.posid <=67):
                    print node.surface+node.next.surface+node.next.next.surface
                    node = node.next.next
        node = node.next


