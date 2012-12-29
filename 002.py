#! /usr/bin/en python
# -*- coding: utf-8 -*-
#2) タブ１文字につきスペース１文字に置換したもの．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
#アプローチ：F.split(), F.join関数の利用
#設定変更：タブ１文字につき→コンマ１文字につき
f = open("../43KUMAMO.CSV", "r")
for line in f.readlines():
    print " ".join(line.split(","))
f.close()
