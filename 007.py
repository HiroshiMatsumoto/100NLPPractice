# !/usr/bin/env python
# -*- coding: utf-8 -*-

#(7) １コラム目の文字列の異なり数（種類数）．確認にはcut, sort, uniq, wcコマンドを用いよ．
#line[a,b,c,d,e,f]とあったらaがline[0], line[1], line[2],・・・で異なるline要素が何個あるか

#アプローチ:aの内容をリスト

file = open("43KUMAMO.CSV", "r")
NewList = set()
for line in file.readlines():
    item = line.split(",")
    NewList.add(item[0])

print len(NewList)

file.close()
