#! /usr/bin/env python
#-*- encoding:utf-8 -*-
#(48) 標準入力から読み込んだ各行の文字列の頻度を求めるプログラムを書き，(47)のプログラムと組み合わせることによって，文章中に出現する各動詞の出現頻度を求めよ．さらに，出現頻度の高い順に動詞を並べよ．
from collections import *#defaultdict
import sys
import re, pprint

# #標準入力(?)
# inputList = list()
# while True:
#     input = sys.stdin.readline()
#     if input != '\n':
#         inputList.append(input.strip('\n'))
#     else:
#         break

#各行文字列の頻度を求める。
def linefrequency(inputList):
    freqInputDict = defaultdict(int)
    for line in inputList:
        freqInputDict[line.decode('utf-8')] += 1
    return freqInputDict

#ref:http://nltk.googlecode.com/svn/trunk/doc/book-jp/ch12.html#id3
def pp(obj):
    pp = pprint.PrettyPrinter(indent=4, width=160)
    str = pp.pformat(obj)
    return re.sub(r"\\u([0-9a-f]{4})", lambda x: unichr(int("0x"+x.group(1),16)), str)

inFile = open("047out.txt","r")#事前に047.pyに-bオプションをつけて出力させておいた
tmpdict = linefrequency(inFile.readlines())
for key, value in sorted(tmpdict.items(), key=lambda t: t[1], reverse=True):
#tmpdict.iteritems():
    key = key.strip('\n')
    tmpdict[key] = value*1.0/len(tmpdict)
    print key.encode('utf-8')+":",tmpdict[key]
#sorted(tmpdict.items(), key=lambda t: t[1], reverse=True))
#print  pp(OrderedDict(sorted(tmpdict.items(), key=lambda t: t[1], reverse=True)))

