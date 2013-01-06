#! /usr/bin/env python
#-*- encoding:utf-8 -*-

from HiroshiLib import *

class testClass:
    def __init__(self, num):
        self.num = num
    def ret(self):
        return self.num
    def reset(self):
        self.num = 0

testDic = {}
testList = []
x = 1
testList.append(x)
x = 2
testCNum = testClass(100)
testList.append(testNum)
print pp(testCNum.ret())

testCNum.reset()
print pp(testCNum.ret())
