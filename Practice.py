#! /usr/bin/en python
# -*- coding: utf-8 -*-

#for文
print "while\n"
seq = range(10)
for item in seq:
    print item

#while
print "while\n"
cnt = 0
while cnt < 10:
    print cnt
    cnt +=1

#do...while
print "do ... while\n"
cnt = 0
while True:
    print cnt
    cnt += 1
    if cnt >= 9:
        break

#関数
def iterate(num, word):
    seq = range(num)
    for word in word:
        print word

iterate(1,2)


#ファイル読み込み
f = open()



