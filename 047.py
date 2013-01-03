#! /usr/bin/env python
#-*- encoding: utf-8 -*-
#(47)(42)から(46)までの処理を１つのプログラムに統合し，処理内容をコマンドライン引数でOn/Offできるようにせよ．コマンドライン引数の処理には，optparseモジュールを用い，オプションには適当な名前（例えば(42)は--verbなど）とドキュメント（-hを引数にすることで表示される）を書け．

#ref:http://docs.python.jp/2.4/lib/module-optparse.html
from optparse import OptionParser
from HiroshiLib import OneLineEach
import MeCab


#####################################################################
#OptionParser
#####################################################################
parser = OptionParser()
"""
#(43)
parser.add_option("-a", "--abc", 
                  action="store", 
                  dest="input",
                  help="string passed by command")
"""
#(42)
#デフォでFalseで、フラグたったらstore_trueでTrueをもたせる。
#parser.add_option(短いオプション記号, 長いオプション記号, dest=変数名, default=デフォ値, action=変数に代入する方法, help=$python ファイル名 -hで表記させるコメント)
parser.add_option("-v", "--verb", 
                  action="store_true", 
                  dest="verb",
                  default=False,
                  help=u"文章中に出現するすべての動詞を抜き出す．")
#(43)
parser.add_option("-b", "--vbase", 
                  action="store_true", 
                  dest="vbase", 
                  default=False, 
                  help=u"文章中に出現するすべての動詞の基本形を抜き出す.")
#(44)
parser.add_option("-s", "--sahen", 
                  action="store_true", 
                  dest="sahen", 
                  default=False, 
                  help=u"サ変名詞をすべて抜き出す．")
#(45)
parser.add_option("-a", "--anb", 
                  action="store_true", 
                  dest="anb", 
                  default=False, 
                  help=u"文章中の「ＡのＢ」という表現（ＡとＢは名詞の１形態素）をすべて抜き出す．")
#(46)
parser.add_option("-c", "--consnoun", #Consecutive Nouns
                  action="store_true", 
                  dest="consnoun", 
                  default=False, 
                  help=u"文章中のすべての名詞の連接（１形態素以上）を抜き出す．")

(options, args) = parser.parse_args()
#options.destで入力にアクセスできる

inFile = open("JpData.txt","r")
mecab = MeCab.Tagger("-Ochasen")

EachLineList = list()
for line in inFile.readlines():
    EachLineList += OneLineEach(line)

ConsNoun = ""
for line in EachLineList:
    node = mecab.parseToNode(line)
    node = node.next
    while node:
        SplitFeature = node.feature.split(",")
        if (31 <= node.posid and node.posid <=33):#posidによるフィルタ
            if options.verb:#(42)
#                print "動詞:"+node.surface
                print node.surface
            if options.vbase:#(43)
#                print "動詞(基本形):"+SplitFeature[6]
                print SplitFeature[6]
        elif((options.sahen or options.anb or options.consnoun) and (36<= node.posid and node.posid <=67)):
            if (options.sahen and (node.next.feature.split(","))[6]=='する'):#(44)
                #(node.next.feature.split(","))[6]: 丸括弧で囲えば出力オブジェクトにアクセスできることがわかった。
                print "サ変名詞:"+node.surface+node.next.surface
            if (options.anb and node.next.surface=='の'):#(45)
                if (36<= node.next.next.posid and node.next.next.posid <=67):
                    print "「AのB」表現:"+node.surface+node.next.surface+node.next.next.surface
            if (options.consnoun):#(46)
                Counter = 0
                while True:
                    if (36<= node.posid and node.posid <=67):#Noun
                        ConsNoun += node.surface
                        node = node.next
                        Counter += 1
                    else:
                        print "連接名詞:"+ConsNoun
                        ConsNoun=""
                        while Counter > 0:
                            node = node.prev
                            Counter -= 1
                        break
        node = node.next

