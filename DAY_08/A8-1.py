# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 00:00:37 2022

@author: santa
"""
import numpy as np


#Importing The text file 
with open("1.txt") as file:
    lines = [line.rstrip() for line in file]

#print(lines)

np_lines = np.array(lines)
#Seperating tress to individual list items
Trees = []
i = 0
for i in range(0,len(lines)):
    #print(i,len(lines[i]))
    current_line = []
    for j in range(0,len(str(lines[i]))):
        current_line.append(lines[i][j])
        #print(lines[i][j],'Tree in the line',i)
    
    Trees.append(current_line)


#print(Trees)
np_Trees = np.array(Trees)

#np_slice = np_Trees[1:0,2:0]
#print(np_slice)
# Getting a list of outer most trees
Outer_most_Trees = []
for row in range(0,len(Trees)):

    for tree in range (0,len(Trees[row])):
        if row == 0 or row == (len(Trees) - 1):
            Outer_most_Trees.append(Trees[row][tree])
        elif tree == 0 or tree == (len(Trees[row])-1):
            Outer_most_Trees.append(Trees[row][tree])

#print(len(Outer_most_Trees))

#Working on Inner trees 
Inner_Visible_Trees = []


    
def Invisible(height,np_list):
    state = 'VIS'
    for iy, ix in np.ndindex(np_list.shape):
        if int(height) <= int(np_list[iy, ix]):
            state = 'INVIS'
            break
    return state
            


for in_row in range(1,(len(lines)-1)):
    #print(lines[in_row])
    for in_col in range(1,(len(lines[in_row])-1)):
        #print(lines[in_row][in_col])
        top_slice = np_Trees[0:(in_row),in_col:in_col+1]
        bot_slice = np_Trees[in_row+1:len(lines),in_col:in_col+1]
        left_slice = np_Trees[in_row:in_row+1,0:in_col]
        right_slice = np_Trees[in_row:in_row+1,in_col+1:(len(lines[in_row])+1)]
        # print('TOP',top_slice.shape,'  For  ',lines[in_row][in_col])
        # print('BOT',bot_slice.shape,'  For  ',lines[in_row][in_col])
        # print('LEFT',left_slice.shape,'  For  ',lines[in_row][in_col])
        #print('RIGHT',right_slice.shape,'  For  ',lines[in_row][in_col])
        
        # Checking tree against all the slice to see if any item is greate or equal to current tree This will tell us that its invisible
        # if not add it to a list of visible trees
        #print(type(lines[in_row][in_col]))
        # print(lines[in_row][in_col])
        # print(Invisible(lines[in_row][in_col],top_slice),' From Top')
        # print(Invisible(lines[in_row][in_col],bot_slice),' From Bot')
        # print(Invisible(lines[in_row][in_col],left_slice),' From Left')
        # print(Invisible(lines[in_row][in_col],right_slice),' From Right')
        
        if Invisible(lines[in_row][in_col],top_slice) == 'VIS' or Invisible(lines[in_row][in_col],bot_slice) == 'VIS' or Invisible(lines[in_row][in_col],left_slice) == 'VIS' or Invisible(lines[in_row][in_col],right_slice) == 'VIS':
              Inner_Visible_Trees.append(lines[in_row][in_col])
              
              
print(len(Outer_most_Trees)+len(Inner_Visible_Trees))

# Calculating Scenic Score , We can skip the outermost safely.

def find_scenic_score(tree,slice):
    T_score = 0
    for T in range (0,slice.shape[1]):
        #print(top_slice_N[0,T])
        if  int(slice[0,T]) >= int(tree):
            T_score = T_score+1
            #print(top_slice_N[0,T],'is >= than',Trees[in_row][in_col],'Incremented Score and will break')
            break
        else:
            T_score = T_score+1
            #print(top_slice_N[0,T],'is < than',Trees[in_row][in_col],'Incremented Score')
    return T_score
    
SCENIC_SCORE = 0
for in_row in range(1,(len(lines)-1)):
    #print(lines[in_row])
    
    for in_col in range(1,(len(lines[in_row])-1)):
        
        #
        #Reshaping and Flipping arrays so they start from our tree in question, 
        #this will make it easy to find tall tree from 1 direction and only have 1 row
        #Only Top and Bot need to be Transpose
        #Only Top and left need to be Flipped
        top_slice = np_Trees[0:(in_row),in_col:in_col+1]
        right_slice = np_Trees[in_row:in_row+1,in_col+1:(len(lines[in_row])+1)]
        bot_slice = np_Trees[in_row+1:len(lines),in_col:in_col+1]
        left_slice = np_Trees[in_row:in_row+1,0:in_col]
       
        #print(Trees[in_row][in_col])
        top_slice_N = np.fliplr(top_slice.transpose())
        left_slice_N = np.fliplr(left_slice)
        bot_slice_N = bot_slice.transpose()
        right_slice_N = right_slice
        # print('TOP\n',top_slice)
        # print('TOP_NEW\n',top_slice_N)
        # print('BOT\n',bot_slice)
        # print('BOT_NEW\n',bot_slice_N)
        # print('LEFT\n',left_slice)
        # print('LEFT_NEW\n',left_slice_N)
        # print('RIGHT\n',right_slice)
        # print('RIGHT_NEW\n',right_slice_N)
        
        #print(top_slice_N.shape[1])
        
        
        # T_score = 0
        # for T in range (0,top_slice_N.shape[1]):
        #     #print(top_slice_N[0,T])
        #     if  int(top_slice_N[0,T]) >= int(Trees[in_row][in_col]):
        #         T_score = T_score+1
        #         #print(top_slice_N[0,T],'is >= than',Trees[in_row][in_col],'Incremented Score and will break')
        #         break
        #     else:
        #         T_score = T_score+1
        #         #print(top_slice_N[0,T],'is < than',Trees[in_row][in_col],'Incremented Score')

        #print('Scenic Score for ',Trees[in_row][in_col],'  is  \n',T_score)
        T = find_scenic_score(Trees[in_row][in_col],top_slice_N)
        B = find_scenic_score(Trees[in_row][in_col],bot_slice_N)
        R = find_scenic_score(Trees[in_row][in_col],right_slice_N)
        L = find_scenic_score(Trees[in_row][in_col],left_slice_N)
        
        current_score = T*B*R*L
        #print(current_score,'for',Trees[in_row][in_col])
        if current_score > SCENIC_SCORE:
            #print(current_score)
            SCENIC_SCORE = current_score
print(SCENIC_SCORE)
        
    
        