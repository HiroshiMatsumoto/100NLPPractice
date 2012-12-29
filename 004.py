#! /usr/bin/en python
# -*- coding: utf-8 -*-
#(4) (3)で作ったcol1.txtとcol2.txtを結合し，元のタブ区切りテキストを復元したもの．確認にはpasteコマンドを用いよ．
#アプローチ：for文とsplit関数の利用、書き出しにwrite関数
f = open("../43KUMAMO.CSV", "r")
wfF = open("first_col.col","w");
wfS = open("second_col.col","w");
wfR = open("復元.txt","w");
for line in f.readlines():
    line = line.split(",")
    FirCol = line[0]
    SecCol = line[1]
    wfR.write(FirCol+"\t"+SecCol+"\n")
f.close()
wfF.close()
wfS.close()
wfR.close()

