# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 16:11:09 2022

@author: santa
"""

import string
  
with open("A3.txt") as file:
    lines = [line.rstrip() for line in file]
  
#Splitting Ruck Sacks into 2 compartments

rSacks = []


def split_string(string):
    if len(string) % 2 == 0:
        return string[:len(string)//2], string[len(string)//2:]
    else:
        return "String length is not even"

# Storing splits into a list    
for i in lines:
    rSacks.append(split_string(i))
    
# Ranking Alphabets

def fill_list(list):
    for i in range(0,26):
        list.append(string.ascii_lowercase[i])
    for j in range(0,26):
        list.append(string.ascii_uppercase[j])

Score = []   
fill_list(Score)
    
def common_letters(string1, string2):
    common = []
    for letter in string1:
        if (letter in string2) and not (letter in common):
            common.append(letter)
    return common


common_items = []
k=0
while k < len(rSacks):
    #print(common_letters(rSacks[k][0], rSacks[k][1]))
    common_items.append(common_letters(rSacks[k][0], rSacks[k][1]))
    k = k + 1
    
def convertTuple(tup):
        # initialize an empty string
    str = ''
    for item in tup:
        str = str + item
    return str

Final_Scores = []

for items in common_items:
    #print(items)
    for g, value in enumerate(Score):
        if value == convertTuple(items):
            #print(g)
            Final_Scores.append(g+1)
            
def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum

print(sum_list(Final_Scores))    