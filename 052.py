#! /usr/bin/env python
# -*- encoding:utf-8 -*-
#(52) 形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，(51)の解析結果を１文毎に読み込み，１文をMorphオブジェクトのリストとして表現し，適当に表示するプログラムを実装せよ．
import MeCab
from HiroshiLib import *
from collections import defaultdict

class Morph:#needs: import MeCab 
    #private
    def parseMeCab(self,surface):
        mecab = MeCab.Tagger("-Ochasen")
        items = mecab.parse(surface).split('\t')
        self.surface = items[0].decode('utf-8')
        if len(items) > 1:
            self.base = items[2].decode('utf-8')
        if len(items) > 2:
            self.pos = (items[3].split("-"))[0].decode('utf-8')
        if len(items) > 3:
            if len(items[3].split("-")) > 1:
                self.pos1 = (items[3].split("-"))[1].decode('utf-8')
        
    #public (kinda?)
    #constructor: 
    def __init__(self, surface):
        self.surface = ""
        self.base = ""
        self.pos = ""
        self.pos1 = ""
        self.parseMeCab(surface)

        #The following returns: AttributeError: Morph instance has no attribute 'dictMorph'
        ###########################################################
        # self.dictMorph['surface'] = items[0].decode('utf-8')
        # self.dictMorph['base'] = items[2].decode('utf-8')
        # self.dictMorph['pos'] = (items[3].split("-"))[0].decode('utf-8')
        # self.dictMorph['pos1'] = (items[3].split("-"))[1].decode('utf-8')
        ###########################################################
    #returns all-four-packed dictionary
    def dict(self):
        dictMorph = dict()
        dictMorph['surface'] = self.surface
        dictMorph['base'] = self.base
        dictMorph['pos'] = self.pos
        dictMorph['pos1'] = self.pos1
        return dictMorph

inFile = open("JpData.txt","r")
Content = inFile.readlines()
mecab = MeCab.Tagger("-Ochasen")

for line in Content:
    for sentence in line.split("。"):
        listPrsdStc = [] #list init
        node = mecab.parseToNode(sentence)
        node = node.next
        while node:
            word = Morph(node.surface)
            listPrsdStc.append(word.dict())
            node = node.next
        print pp(listPrsdStc)
