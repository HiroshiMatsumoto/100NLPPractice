#! /usr/bin/env python
#-*- encoding: utf-8 -*-
#(10) 各行の２コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べよ．ただし，(3)で作成したプログラムの出力（col2.txt）を読み込むプログラムとして実装せよ．確認にはcut, uniq, sortコマンドを用い

#はしょり：(3)で作成したプログラムの出力（col2.txt）を読み込むプログラムとして実装せよ
#アプローチ： 読み込みファイルより[文字列, 頻度]のリストを作成

#List = [["abd","asbd"],["wbd","zzdbd","wbd"],["abd","asbd"]]
#List = [[1,2],[3,4,5],[1,2]]
#print List
#NewList = set(List)
#print NewList
#上を実行すると以下の結果となる
"""
[['abd', 'asbd'], ['wbd', 'zzdbd', 'wbd'], ['abd', 'asbd']]
Traceback (most recent call last):
  File "010.py", line 15, in <module>
    NewList = set(List)
TypeError: unhashable type: 'list'
"""
#多重リストにsetは適用不可？

import csv

file = open("43KUMAMO.CSV","r")
Contents = csv.reader(file)

FreqList = [] #[対象文字列(str)、頻度(int)]

for lineContents in Contents: #コンテンツのループ
    fInList = False #リスト用フラグ
    for itemFreqList in FreqList: #リストのループ
        if(lineContents[4]==itemFreqList[0]):#リストの中とのマッチング
            itemFreqList[1] += 1
            fInList = True #リストの中にあったらフラグを立てる
    if(fInList == False): #フラグがたってなかったら、
        #print lineContents[4]
        FreqList.insert(len(FreqList), [lineContents[4], 0])#リストに追加

FreqList.sort(key=lambda x:(x[1]))#, reverse=True)

for item in FreqList:
    print item[0],item[1]

file.close()
