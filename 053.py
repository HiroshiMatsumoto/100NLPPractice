#! /usr/bin/env python
#-*- encoding:utf-8 -*-
#文節を表すクラスChunkを実装せよ．このクラスは形態素のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．さらに，(51)の解析結果を１文毎に読み込み，１文をChunkオブジェクトのリストとして表現し，適当に表示するプログラムを実装せよ．
#１文をChunkオブジェクトのリスト:この１文は解析結果の一文ではなくて日本語文章のデータ上での一文のこと・・・であってる？

from HiroshiLib import *
import CaboCha
import re
#ref:http://docs.python.org/2/library/xml.etree.elementtree.html
#import xml.etree.ElementTree as ET
from collections import defaultdict

cabocha = CaboCha.Parser('--charset=UTF8')

class Chunk:
    #constructor
    def __init__(self):
        self.reset()
    def display(self):
        print "morphs:",pp(self.morphs),
        print "\n dst:%d"%self.dst,
        print "\n srcs:",pp(self.srcs)
    def reset(self):
        self.morphs = []
        self.dst = 0
        self.srcs = []
        self.num = -1

inFile = open("051out.txt","r")
content = inFile.readlines()

cnt = 0
LineList = []
ChunkList = []
chunk = Chunk()
DstDict = {}#係り先インデックス・リスト;{係り先1：[係り元番号1、係り元番号2・・・], 係り先2：[係り元番号3、係り元番号4・・・]}
for line in content:
    if len(line) > 1:# to exclude "\n"
        line = line.strip("\n")
        #print len(line),
        #print line
        cnt += 1
        if line[0]=="*":#文節終了/文節開始
            chunk.num = line[2]
            if not chunk.num != "0":
                #文節終了プロセス:
                chunk_copy = chunk
                chunk_copy.display()
                ChunkList.append(chunk_copy)
                DstDict = {}
            #文節開始プロセス:* 0 1D 0/1 0.978991の解析
            if chunk.num in DstDict: #係り元がリストにあるか
                chunk.srcs = DstDict[chunk.num]
            chunk.dst = int((((line.split(" "))[2]).split("D"))[0])#.. 1D ..の1を抽出
            if not chunk.dst in DstDict:#DstDictの値の初期化
                DstDict[chunk.dst] = []
            DstDict[chunk.dst].append(chunk.num)#係り元リストに追加
        # elif re.match("^EOS.*",line):#文終了
        #     if chunk.num in DstDict:#係り元がリストにあるか
        #         chunk.srcs = DstDict[chunk.num]
        #     ChunkList.append(chunk)
        #     DstDict = {}
        # elif re.match("^。.*",line):#文終了
        #     print line.strip("\n")
        else: #文節中
            chunk.morphs.append((line.split("\t"))[0].decode("utf-8"))
        #    print pp(chunk.morphs)
        if cnt > 28:
            break
for chunk in ChunkList:
    chunk.display()
