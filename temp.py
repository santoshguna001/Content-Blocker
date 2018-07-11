# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 20:40:28 2018

@author: Santosh
"""
from load_words import bad_words_list_final1
import re

#strings are immutable in python
#this method is used to replace a character with a string at an index
def replacer(s, newstring, index, nofail=False):
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")
    if index < 0:
        return newstring + s
    if index > len(s):
        return s + newstring
    return s[:index] + newstring + s[index + 1:]

#generates all the indices of a substring in a string
def substring_indexes(substring, string):
    last_found = -1  
    while True:
        last_found = string.find(substring, last_found + 1)
        if last_found == -1:  
            break  # All occurrences have been found
        yield last_found
        

        
text=input("Enter the text message to check for abusive content:\n")
temp2=text
for i in range(len(bad_words_list_final1)):
    text=temp2
    temp=re.findall(r"\b%s\b" %bad_words_list_final1[i], text,re.IGNORECASE)
    temp1=list(substring_indexes(bad_words_list_final1[i],text.lower()))
    #temp1=re.search(r"\b%s\b" %bad_words_list_final1[i], text,re.IGNORECASE)
    if temp:
        text1=text
        for m in range(len(temp1)):
            #print(temp1[m])
            k=temp1[m]+len(bad_words_list_final1[i])
            for j in range(temp1[m]+1,k):
                text1=replacer(text1, '*', j)
        text=text1
    temp2=text
print(text)

del i,k,j,m,temp,temp1,temp2,text1

        

