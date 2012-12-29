#! /usr/bin/env python  
# -*- python -*-
# -*- encoding: utf-8 -*-
import re

#f=open("test2.txt","r")
f=open("j98_1002.txt","r")
w=open("024out.txt","w")
line = f.readline()
while line:
    line = line.strip("\n")
    word = re.findall("\s*,?([\(\)\<\>\{\}]|[^\".\n][\w'-]*)[\s\.,]?", line)
    #word = re.findall("\s*,?([^\".\n][\w'-]*)[\s\.,]?", line) #proto#1
    #word = re.findall("([^,\n]\w+)", line)
    #print word
    for i in range(len(word)):
        if len(line):
            print word[i]
            w.write(word[i])
            w.write("\n")
    print "\n",
    w.write("\n")
    line = f.readline()
f.close()
w.close()
