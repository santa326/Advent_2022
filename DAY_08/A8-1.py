# -*- coding: utf-8 -*-

import numpy as np


#Importing The text file 
with open("1.txt") as file:
    lines = [line.rstrip() for line in file]


#Converting Above list to numpy List
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


#Converting Above list to numpy Array
np_Trees = np.array(Trees)

#This is not needed , just count the trees based on grid size
Outer_most_Trees = []
for row in range(0,len(Trees)):

    for tree in range (0,len(Trees[row])):
        if row == 0 or row == (len(Trees) - 1):
            Outer_most_Trees.append(Trees[row][tree])
        elif tree == 0 or tree == (len(Trees[row])-1):
            Outer_most_Trees.append(Trees[row][tree])



#Working on Inner trees 
Inner_Visible_Trees = []


#This checks if a tree is visible or not from outside
def Invisible(height,np_list):
    state = 'VIS'
    for iy, ix in np.ndindex(np_list.shape):
        if int(height) <= int(np_list[iy, ix]):
            state = 'INVIS'
            break
    return state
            

#Slicing and Getting the trees in all 4 direction of a tree
for in_row in range(1,(len(lines)-1)):
    #print(lines[in_row])
    for in_col in range(1,(len(lines[in_row])-1)):
        #print(lines[in_row][in_col])
        top_slice = np_Trees[0:(in_row),in_col:in_col+1]
        bot_slice = np_Trees[in_row+1:len(lines),in_col:in_col+1]
        left_slice = np_Trees[in_row:in_row+1,0:in_col]
        right_slice = np_Trees[in_row:in_row+1,in_col+1:(len(lines[in_row])+1)]
        
      #A Tree vibile from any 1 direction is added to Inner_Visible_Tress list  
        if Invisible(lines[in_row][in_col],top_slice) == 'VIS' or \
                        Invisible(lines[in_row][in_col],bot_slice) == 'VIS' or \
                                Invisible(lines[in_row][in_col],left_slice) == 'VIS' or \
                                        Invisible(lines[in_row][in_col],right_slice) == 'VIS':
              Inner_Visible_Trees.append(lines[in_row][in_col])
              
#To get all the visible tree we add length of outer trees and inner visible trees          
print('Trees that are vibile from outside the grid :',len(Outer_most_Trees)+len(Inner_Visible_Trees))

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
 
    
    for in_col in range(1,(len(lines[in_row])-1)):
        
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
        
        
        T = find_scenic_score(Trees[in_row][in_col],top_slice_N)
        B = find_scenic_score(Trees[in_row][in_col],bot_slice_N)
        R = find_scenic_score(Trees[in_row][in_col],right_slice_N)
        L = find_scenic_score(Trees[in_row][in_col],left_slice_N)
        
        current_score = T*B*R*L

        if current_score > SCENIC_SCORE:

            SCENIC_SCORE = current_score
print('Highest Possible Scenic Score :',SCENIC_SCORE)
        
    
        