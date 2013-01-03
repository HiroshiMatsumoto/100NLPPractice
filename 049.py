#!/usr/bin/env python
#-*- coding:utf-8 -*-
#(49) (48)の出力を利用して，文字列の頻度を横軸，その文字列の異なり数（種類数）を縦軸として，ヒストグラムをプロットせよ．なお，プロットにはgnuplotやmatplotlibを用い，グラフを画像ファイルとして保存せよ．
import MeCab
import re, pprint
from collections import *

def pp(obj):
    pp = pprint.PrettyPrinter(indent=4, width=160)
    str = pp.pformat(obj)
    return re.sub(r"\\u([0-9a-f]{4})", lambda x: unichr(int("0x"+x.group(1),16)), str)

fpInFile = open("048out.txt","r")
fpOutFile = open("049out.csv","w")
listContent = fpInFile.readlines()

mecab = MeCab.Tagger("-Ochasen")

#動詞のキー値に{基本形,頻度}をバリュー値とした辞書
dictWord = dict()
dictWordItem = dict()
for strLine in listContent:
    listItems = strLine.split(":")
    item = mecab.parse(listItems[0]).split('\t')
    dictWordItem['base'] = item[2].decode('utf-8')
    dictWordItem['freq'] = listItems[1]
    dictWord[item[0].decode('utf-8')] = dictWordItem
    dictWordItem = {}
#print pp(dictWord)

#同じ基本形の動詞のカウント
dictSameBaseWordCount = defaultdict(int)
for word in dictWord:
    dictSameBaseWordCount[dictWord[word]['base']] += 1
#print pp(sorted(dictSameBaseWordCount.items(), key=lambda t:t[1], reverse=True))

outputline=""
for word in dictWord:
    outputline += str(dictWord[word]['freq'].strip('\n'))+','
    key = dictWord[word]['base']
    if key in dictSameBaseWordCount:
        outputline+=str(dictSameBaseWordCount[key])+'\n'
    fpOutFile.write(outputline)
    outputline=""

fpInFile.close()
fpOutFile.close()
