#! /usr/bin/env python
# -*- python -*-
# -*- encoding: utf-8 -*-

import sys

for line in sys.stdin.readline().split("."):
    #文字列先頭の空白部(' ')除去
    print line+"."
