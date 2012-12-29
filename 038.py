#! /usr/bin/env python
#-*-encoding:utf-8-*-
#(38) (37)の出力を読み込み，ある単語wに続く単語zの条件付き確率P(z|w)を求めよ．ただし，出力形式は"(条件付き確率)\t(現在の単語)\t(次の単語)"とせよ．
u"""
条件確率
P(A|B) = P(A∩B)/P(B)

P(z|w) = P(z∩w)/P(w)
(Z&Wが起こる確率)/(Wが起こる確率)

(1): (Z&Wが起こる確率) = 037out.txtを用いて  Z&Wの頻度/全頻度の和
(2): (Wが起こる確率) = 025out.txtを用いて　Wの出現数/全単語の出現数の和

"""
import re, sys
from collections import defaultdict

outFile38 = open("038out.txt","w")

#(1): (Z&Wが起こる確率) = 037out.txtを用いて  Z&Wの頻度/全頻度の和
#(37)の出力を読み込み，
inFile37 = open("037out.txt","r") #037out.txt: 頻度\t単語\t単語のリスト
Dict37 = dict() #連語の頻度リスト
sumWZfreq = 0

#037out.txtの内容を辞書型変数Dict37に代入:{"Z\tW":0, ・・・}
#同時にsumWZfreqに全頻度を加算
for line in inFile37:
    item = re.match("^(\d*)\t(.*?\t.*?)$",line.strip("\n"))
    sumWZfreq += int(item.group(1))#頻度の加算
    Dict37[item.group(2)] = int(item.group(1))


#037out.txtの内容を辞書型変数Dict37に代入:{"Z\tW":0, ・・・}
#WZ:ある単語wに続く単語z
probCapWZ = dict() #P(ZandW)
for WZ in Dict37:
    if not WZ in probCapWZ:
        probCapWZ[WZ] = Dict37[WZ]*1.0/sumWZfreq#*100
        print "%s:%f"%(WZ, probCapWZ[WZ])


#(2): (Wが起こる確率) = 025out.txtを用いて　Wの出現数/全単語の出現数の和
#Wの出現総数カウント
inFile25 = open("025out.txt","r") #025out.txt: (単語in原型(大文字もある))\t(単語in小文字)
lineCount = 0
wordList = dict()
for line in inFile25:
    item = re.match("^(.*?)\t(.*?)$",line.strip("\n"))
    lineCount += 1
    if item.group(2) in wordList:
        wordList[item.group(2)] += 1
    else:
        wordList[item.group(2)] = 1

ProbW = dict() #各単語の確率:P(W)
for word in wordList:
    ProbW[word] = wordList[word]*1.0/lineCount#sumWList

ProbWZoverW = dict()
for WZ in probCapWZ:
    item = re.match("^(.*?)\t(.*?)$",WZ)
    ProbWZoverW[WZ] = probCapWZ[WZ]*1.0/ProbW[item.group(1)]
    print str(ProbWZoverW[WZ])+'\t'+WZ
    outFile38.write(str(ProbWZoverW[WZ])+'\t'+WZ+'\n')

outFile38.close()
inFile37.close()
