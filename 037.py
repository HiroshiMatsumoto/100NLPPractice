#! /usr/bin/env python
#-*- encoding: utf-8 -*-

import re

inFile = open("036out.txt","r")
outFile = open("037out.txt","w")

#frequency calc:
FreqList = dict()
for line in inFile:
    line = line.strip("\n")
    if line in FreqList:
        FreqList[line] += 1
    else:
        FreqList[line] = 1
#ref: http://d.hatena.ne.jp/ir_takt/20110808/1312830911
for k, v in sorted(FreqList.items(), key=lambda x:x[1], reverse=True):
    newline = str(v)+"\t"+k+"\n"
    outFile.write(newline)
    
inFile.close()
outFile.close()
