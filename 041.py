#! /usr/bin/env python
#-*- coding:utf-8 -*-
#(41) 日本語の文章をMeCabで形態素解析し，その結果を読み込むプログラムを実装せよ．
#ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，１文は形態素（マッピング型）のリストとして表現せよ．
#ref:http://mecab.googlecode.com/svn/trunk/mecab/doc/index.html#parse
#表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
import sys
import re
import MeCab

#文字列chunkを句読点ごとにリストにいれたものをリターンする。
def OneLineEach(chunk):
    retList = list()
    SplitChunk = chunk.split("。")
    for line in SplitChunk:
        if not re.match("[\n\z]",line):
            retList.append(line+"。")
    return retList  

inFile=open("JpData.txt","r")
mecab = MeCab.Tagger("-Ochasen")
"""
% mecab -Oyomi (ヨミ付与)
% mecab -Ochasen (ChaSen互換)
% mecab -Odump (全情報を出力)
"""
EachLineList = list()

#一行ごとにリスト化
for line in inFile.readlines():
    EachLineList+=OneLineEach(line)#リストの結合は+演算子で行える appendメソッドだと要素として追加される。
#確認
#for line in EachLineList:
#    print line

######
#解析
######

listParagraph = list() #全体のマッピング
listLine = list()#一行ごとのマッピング
dictWord = dict()#単語ごとのマッピング

for line in EachLineList:
    #ref:http://blog.unfindable.net/archives/4347
    node = mecab.parseToNode(line)
    node = node.next
    while node:
        SplitFeature = node.feature.split(",")
        #ref:http://mecab.googlecode.com/svn/trunk/mecab/doc/posid.html
        dictWord['surface'] = node.surface.decode('utf-8')
        dictWord['base'] = SplitFeature[6].decode('utf-8')
        dictWord['pos'] = SplitFeature[0].decode('utf-8')
        dictWord['pos1'] = SplitFeature[1].decode('utf-8')
        listLine.append(dictWord)
        dictWord = {} #辞書を空: dictWord.clear()だとうまく動作しなかった : KeyErrorと吐く
        node = node.next
    listParagraph.append(listLine)
    listLine = []#    del listLine[:]#リストを空

####
#出力
####
output = str()
for line in listParagraph:
    for word in line:
        output += word['surface']
    print output.encode('utf-8')+":"
    output=""

    for key in line:
        for element in key:
            print "\t",
            print element+":"+key[element].encode('utf-8')
        print "\n"
    print "\n"

########################################################
#実行させると...
########################################################

# 昔々、インドとシナを支配する王に二人の息子がいた。:
# 	base:昔
# 	pos:名詞
# 	surface:昔
# 	pos1:副詞可能


# 	base:々
# 	pos:記号
# 	surface:々
# 	pos1:一般


# 	base:、
# 	pos:記号
# 	surface:、
# 	pos1:読点


# 	base:インド
# 	pos:名詞
# 	surface:インド
# 	pos1:固有名詞


# 	base:と
# 	pos:助詞
# 	surface:と
# 	pos1:並立助詞


# 	base:シナ
# 	pos:名詞
# 	surface:シナ
# 	pos1:一般


# 	base:を
# 	pos:助詞
# 	surface:を
# 	pos1:格助詞


# 	base:支配
# 	pos:名詞
# 	surface:支配
# 	pos1:サ変接続

#と以上のようになる。
