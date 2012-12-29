#!/usr/bin/env python
#-*- coding: utf-8 -*-

from f010 import RankList 

outFile = open("027out.txt","w")
RankedList = RankList("025out.txt")
#ref: http://blog.livedoor.jp/yawamen/archives/51492355.html
for key, value in sorted(RankedList.items(), key=lambda x:x[1]):
    print "%s:%d" % (key, value)
