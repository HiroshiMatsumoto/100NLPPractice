#!/usr/bin/env python
import re

fopen = open("024out.txt","r")
fwrite = open("025out.txt","w")
word = fopen.readline()
while word:
    #word = "\n" #for debug
    if not re.match("^\s+\n$",word):
        word = word.strip("\n")
        line = str(word)+"\t"+str(word.lower())+"\n"
        print line,
        fwrite.write(line)
    word = fopen.readline()
    #break #for debug
fopen.close()    
fwrite.close()    

