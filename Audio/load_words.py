# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 12:42:16 2018

@author: Santosh
"""
"""
import pandas as pd

#load the datasets having the bad words
bad_words_set_1=pd.read_csv('en.csv')
bad_words_set_2=pd.read_csv('bad-words.csv')
bad_words_set_3=pd.read_csv('bad-words1.csv')

#merging all the datasets into one and deleting the duplicates
bad_words_list=pd.concat([bad_words_set_1,bad_words_set_2]).drop_duplicates().reset_index(drop=True)
bad_words_list_final=pd.concat([bad_words_list,bad_words_set_3]).drop_duplicates().reset_index(drop=True)

#converting all the words to lower case for simplification
bad_words_list_final['words'] = bad_words_list_final['words'].str.lower()

#sorting the database
bad_words_list=bad_words_list_final.sort_values(by=['words'])

#delete unnecessary variables
del bad_words_set_1
del bad_words_set_2
del bad_words_set_3
del bad_words_list_final
"""


import csv


#load the datasets having the bad words
with open('test.csv','r') as f:
    reader = csv.reader(f)
    bad_words_set_1=list(reader)
    
    
with open('test1_mod.csv','r') as f:
    reader = csv.reader(f)
    bad_words_set_2=list(reader)


#merging all the datasets into one and deleting the duplicates    
bad_words_list = list(bad_words_set_1)
bad_words_list.extend(x for x in bad_words_set_2 if x not in bad_words_list)

#converting list of lists to list
bad_words_list_final = []
for x in bad_words_list:
    for y in x:
        bad_words_list_final.append(y)
#bad_words_list_final.remove('words')

#sorting the database
bad_words_list_final.sort(reverse=True)


#delete unnecessary variables
del bad_words_set_1
del bad_words_set_2
#del bad_words_set_3
del bad_words_list
del x
del y
#del bad_words_list_final


#thefile = open('test.txt', 'w')
#for item in bad_words_list_final1:
  #thefile.write("%s\n" % item)

#bad_words_list_final1.sort()
#thefile = open('test1.txt', 'w')
#for item in bad_words_list_final1:
  #thefile.write("%s\n" % item)

#del item
    
