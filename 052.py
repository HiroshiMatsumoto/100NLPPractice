#! /usr/bin/env python
# -*- encoding:utf-8 -*-
#(52) 形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，(51)の解析結果を１文毎に読み込み，１文をMorphオブジェクトのリストとして表現し，適当に表示するプログラムを実装せよ．
import MeCab

class Morph:#needs: import MeCab 
    #instructor: 
    #Morph word(Word)
    def __init__(self, surface):
        self.surface = surface.strip('\n')
        mecab = MeCab.Tagger("-Ochasen")
        items = mecab.parse(surface).split('\t')
        self.base = items[2]
        self.pos = (items[3].split("-"))[0]
        self.pos1 = (items[3].split("-"))[1]
        self.dictMorph['surface'] = item[0].encode('utf-8')
        self.dictMorph['base'] = items[2].encode('utf-8')
        self.dictMorph['pos'] = (items[3].split("-"))[0].encode('utf-8')
        self.dictMorph['pos1'] = (items[3].split("-"))[1].encode('utf-8')
    #returns all-four-packed dictionary
    def dict(self):
        return self.dictMorph

inFile = open("JpData.txt","r")
Content = inFile.readlines()
mecab = MeCab.Tagger("-Ochasen")

print Content
for sentence in Content.strip('\n').split("。"):
    listPrsdStc = [] #list init
    node = mecab.parseToNode("sentence")
    node = node.next
    while node:
        word = Morph(node.surface)
        listPrsdStc.append(word)
        node = node.next
    print listPrsdStc
        
    
    
