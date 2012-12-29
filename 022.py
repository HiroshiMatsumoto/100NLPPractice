#! /usr/bin/env python
# -*- python -*-
# -*- encoding: utf-8 -*-
# Task:標準入力から英語のテキストを読み込み，ピリオド→スペース→大文字を文の区切りと見なし，１行１文の形式で標準出力に書き出せ．

import sys
import re

for line in sys.stdin.readline().split("."):
    print re.match("\.\s[A-Z]",line)
