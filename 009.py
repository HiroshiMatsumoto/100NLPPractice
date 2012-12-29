#! /usr/bin/env python
# -*- encoding: utf-8 -*-
#(9) 各行を２コラム目，１コラム目の優先順位で辞書の逆順ソートしたもの（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題は結果が合わなくてもよい）．
#アプローチ:sorted関数の利用(key値の使用)
#参考:
#みんなのPython 柴田淳
#http://docs.python.jp/2/howto/sorting.html

import csv
file = open("43KUMAMO.CSV","r")
contents = csv.reader(file)
NewList = []
for line in contents:
    #print line[3],
    #print line[4], 
    #print line[5], 
    #print line[6], 
    #print line[7], 
    #print line[8]
    NewList.insert(len(NewList), [line[4], line[5], line[7], line[8]])

NewList.sort(key=lambda x:(x[1],x[0]), reverse=True)

for line in NewList:
    print line[0],
    print line[1],
    print line[2],
    print line[3]

file.close()

