#! /usr/bin/en python
# -*- coding: utf-8 -*-
#(3) 各行の１列目だけを抜き出したものをcol1.txtに，２列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ
#アプローチ：for文とsplit関数の利用、書き出しにwrite関数
f = open("../43KUMAMO.CSV", "r")
wfF = open("col1.txt","w");
wfS = open("col2.txt","w");
for line in f.readlines():
    line = line.split(",")
    FirCol = line[0]
    SecCol = line[1]
    print u"1列目: %s" % FirCol,
    print u"2列目: %s" % SecCol
    wfF.write(FirCol+"\n")
    wfS.write(SecCol+"\n")
f.close()
wfF.close()
wfS.close()
