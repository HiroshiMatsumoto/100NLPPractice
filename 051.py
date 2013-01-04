#! /usr/bin/env python
#-*- encoding:utf-8 -*-
#(51) 日本語の文章をCaboChaで係り受け解析し，ラティス形式（-f1オプション）の解析結果を得よ．
#ref:http://nltk.googlecode.com/svn/trunk/doc/book-jp/ch12.html#cabocha
import CaboCha
cabocha = CaboCha.Parser('--charset=UTF8')
#sent = u"太郎はこの本を二郎を見た女性に渡した。".encode('utf-8')


inFile = open("JpData.txt","r")
Contents = inFile.readlines()
for line in Contents:
    for setence in line.strip('\n').split("。"):
        setence+="。"
        sent = setence
        """
        print "parseToString:"
        print cabocha.parseToString(sent)
        """
        #print "tree.toString:"
        tree = cabocha.parse(sent)
        print tree.toString(CaboCha.FORMAT_LATTICE)
