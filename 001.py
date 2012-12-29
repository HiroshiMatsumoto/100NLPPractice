#! /usr/bin/en python
# -*- coding: utf-8 -*-
#1) 行数をカウントしたもの．確認にはwcコマンドを用いよ
#アプローチ：F.readlines()で行ごとに読み込みリスト化、
#そのリストの要素数カウントをlen()関数で行う。

f = open("../43KUMAMO.CSV", "r")
Content = f.readlines()
print len(Content)
f.close()
