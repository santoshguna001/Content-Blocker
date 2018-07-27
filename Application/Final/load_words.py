# -*- coding: utf-8 -*-
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

#sorting the database
bad_words_list_final.sort(reverse=True)


#delete unnecessary variables
del bad_words_set_1
del bad_words_set_2
#del bad_words_set_3
del bad_words_list
del x
del y