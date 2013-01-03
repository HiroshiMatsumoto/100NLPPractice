#! /usr/bin/env python
#-*- encoding:utf-8 -*-
#(48)の出力を利用して，文字列の出現頻度の順位（高い順）を横軸，その出現頻度を縦軸として，プロットせよ．

inFile = open("048out.txt","r")
outFile = open("050out.csv","w")

Content = inFile.readlines()
Count = 0
for item in Content:
    Count += 1
    outFile.write(str(Count)+','+str((item.split(':'))[1]))
