# !/usr/bin/env python
# -*- coding: utf-8 -*-

# (6) 自然数Nをコマンドライン引数にとり，入力のうち末尾のN行だけ．確認にはtailコマンドを用いよ

# アプローチ：

import sys 

N = int(sys.argv[1]) # $python 006.py 1 のようにファイル名の次に数値が来ると仮定
#if(isinstance(N, int)):#http://www.gossamer-threads.com/lists/python/python/97153
#    print "it is an int"
#    print N
#else:
#    print "it is not an int"
#    print N


f = open("43KUMAMO.CSV","r")
lines = f.readlines()
for num in range(0, N): #(5)
#for num in range(N, len(lines)):#(6)
    print lines[num]
f.close()
