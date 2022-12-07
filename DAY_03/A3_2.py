# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 16:11:09 2022

@author: santa
"""

import string
  
with open("A3_2.txt") as file:
    lines = [line.rstrip() for line in file]
  

    
# Ranking Alphabets

def fill_list(list):
    for i in range(0,26):
        list.append(string.ascii_lowercase[i])
    for j in range(0,26):
        list.append(string.ascii_uppercase[j])

Score = []   
fill_list(Score)
    
def common_letters(string1, string2, string3):
    common_list = []
    for letter in string1:
        if letter in string2 and letter in string3:
            common_list.append(letter)
    return common_list


common_items = []
a = 0
while a < len(lines):
    #print(common_letters(rSacks[k][0], rSacks[k][1]))
    common_items.append(common_letters(lines[a], lines[a+1], lines[a+2]))
    
    a = a + 3
    
def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str

Final_Scores = []

for items in common_items:
    print(items)
    for g, value in enumerate(Score):
        if value == convertTuple(items[0]):
            #print(g)
            Final_Scores.append(g+1)
            
def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum

print(sum_list(Final_Scores))    




