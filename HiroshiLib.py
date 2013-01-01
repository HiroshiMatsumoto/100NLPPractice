#! /usr/bin/env python
#-*- encoding: utf-8 -*-

import re
import sys

#文字列chunkを句読点でスプリットさせリストにいれたものをリターンする。
def OneLineEach(chunk):
    retList = list()
    SplitChunk = chunk.split("。")
    for line in SplitChunk:
        if not re.match("[\n\z]",line):
            retList.append(line+"。")
    return retList


