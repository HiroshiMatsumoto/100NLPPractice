#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import re
inFile = open("030out.txt","r")
outFile = open("036out.txt","w")

prevword = str()
word = str()
for line in inFile:
    item = re.match("^(.*?)\t(.*?)\t(.*?)$", line.strip("\n"))
    prevword = word
    word = item.group(2)
    outFile.write(prevword+"\t"+word+"\n")
    
    
    
        
    
    
        

        
        
    
