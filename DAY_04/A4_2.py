# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 15:08:10 2022

@author: santa
"""

import CS


A = CS.read_txt('1.txt')

B = []
for lines in A:
    assignments = lines.split(",")
    B.append(assignments[0])
    B.append(assignments[1])
    

C = []
for ranges in B:
    num = ranges.split("-")
    one = int(num[0])
    two = int(num[1])
    r = set(range(one,two+1))
    C.append(r)
    
    #print(r)

i = 0
j = 1
k = 0
RESULT = []

while j <= len(C):
    X = C[i]
    Y = C[j]
    isEmpty = (len(Y.intersection(X))==0)
    if isEmpty:
        pass
    else:
        #print(Y.intersection(X))
        k = k+1
        
    
    i = i+2
    j = j+2
    
print ("Total number of intersections :", k)