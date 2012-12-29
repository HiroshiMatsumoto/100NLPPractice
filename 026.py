#!/usr/bin/env python
import re
#inFile = open("025out.txt","r")
inFile = open("test2.txt","r")
outFile = open("026out.txt","w")

Word = inFile.readline()
setWord = set()
while Word:
    #Getting lowered words (located after original_word \t)
    Word.strip("\n")
    pairWord = re.match("^(.*)\t(.*)$",Word)
    loweredWord = pairWord.group(2)
    #print loweredWord
    setWord.add(loweredWord)
    #print listWord
    Word = inFile.readline()
    #break #for debug

listWord = list(setWord) 
listSuffix_ly = set()
#making a list of  -ly words
for i in range(len(listWord)):
    matched = re.match("^(.*)ly$",listWord[i])
    if matched:
        listSuffix_ly.add(matched.group(1))
        #print matched.group(1)
#picking -ness words out of listWord and checking matched with listSuffix_ly
for i in range(len(listWord)):
    matched = re.match("^(.*)ness$",listWord[i])
    if matched and matched.group(1) in listSuffix_ly:
        print matched.group(1)

inFile.close()
outFile.close()

