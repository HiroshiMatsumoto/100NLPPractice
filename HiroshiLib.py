#! /usr/bin/env python
#-*- encoding: utf-8 -*-

import re
import sys
import print

#文字列chunkを句読点でスプリットさせリストにいれたものをリターンする。
def OneLineEach(chunk):
    retList = list()
    SplitChunk = chunk.split("。")
    for line in SplitChunk:
        if not re.match("[\n\z]",line):
            retList.append(line+"。")
    return retList

#print listなどで文字化けを解消する
def pp(obj):
    pp = pprint.PrettyPrinter(indent=4, width=160)
    str = pp.pformat(obj)
    return re.sub(r"\\u([0-9a-f]{4})", lambda x: unichr(int("0x"+x.group(1),16)), str)
