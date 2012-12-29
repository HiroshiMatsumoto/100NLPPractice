# !/usr/bin/env python
# -*- coding: utf-8 -*-

#(8) 各行を２コラム目の辞書順にソートしたもの（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題は結果が合わなくてもよい）．

import csv

file = open("43KUMAMO.CSV")
l = csv.reader(file)#http://docs.python.jp/2/library/csv.html
for row in file:
    print csv

