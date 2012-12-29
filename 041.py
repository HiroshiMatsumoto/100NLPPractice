#! /usr/bin/env python
#-*- coding:utf-8 -*-

import sys
import MeCab

m = MeCab.Tagger("-Ochasen")
"""
% mecab -Oyomi (ヨミ付与)
% mecab -Ochasen (ChaSen互換)
% mecab -Odump (全情報を出力)
"""
print m.parse("今日もしないとね")
