#! /usr/bin/en python
# -*- coding: utf-8 -*-
#(5) 自然数Nをコマンドライン引数にとり，入力のうち先頭のN行だけ．確認にはheadコマンドを用いよ．
#参考:http://osksn2.hep.sci.osaka-u.ac.jp/~taku/osx/python/readfile.html
#http://docs.python.jp/2.7/tutorial/stdlib.html#tut-command-line-arguments
#アプローチ：
import sys
N = sys.argv #intと仮定：エラーハンドリング未実装
f = open("../43KUMAMO.CSV", "r")
lines = f.readlines()
for n in range(0, N)
    print reqline[N] 
f.close()

