#! /usr/bin/env python
#-*- encoding: utf-8 -*-

import re
import sys
import pprint
import MeCab

#文字列chunkを句読点でスプリットさせリストにいれたものをリターン
def OneLineEach(chunk):
    retList = list()
    SplitChunk = chunk.split("。")
    for line in SplitChunk:
        if not re.match("[\n\z]",line):
            retList.append(line+"。")
    return retList

#print listなどで起こる文字化けを解消
def pp(obj):
    pp = pprint.PrettyPrinter(indent=4, width=160)
    str = pp.pformat(obj)
    return re.sub(r"\\u([0-9a-f]{4})", lambda x: unichr(int("0x"+x.group(1),16)), str)

#Morph(word)で宣言されたwordの
class Morph:#needs: import MeCab 
    #instructor: 
    def __init__(self, surface):
        mecab = MeCab.Tagger("-Ochasen")
        items = mecab.parse(surface).split('\t')
        self.surface = items[0].decode('utf-8')
        self.base = ""
        self.pos = ""
        self.pos1 = ""
        if len(items) > 1:
            self.base = items[2].decode('utf-8')
        if len(items) > 2:
            self.pos = (items[3].split("-"))[0].decode('utf-8')
        if len(items) > 3:
            if len(items[3].split("-")) > 1:
                self.pos1 = (items[3].split("-"))[1].decode('utf-8')       
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
