# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 16:11:09 2022

@author: santa
"""


  
with open("A1.txt") as file:
    lines = [line.rstrip() for line in file]
  
summary = []


elf = 1
elf_Sum = 0

for line in lines:
    #print (line)
    if len(line) == 0:
        summary.append([elf,elf_Sum])
        elf_Sum = 0
        elf = elf + 1
    else:
        elf_Sum = elf_Sum + int(line)
        
        
#Answer to first Finding the elf with highest calories 

CALORIES = []
j = 0
for k in summary:
    #print(k[1])
    CALORIES.insert(j,k[1])
    j=j+1
CALORIES.sort(reverse=True)
print(CALORIES[0])



#Answer to Second

print(CALORIES[0]+CALORIES[1]+CALORIES[2])
        


    
    
    
    


    
