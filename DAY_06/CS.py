# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:25:02 2022

@author: santa
"""


#Import Text and retun a list
# USAGE A = read_txt('.\day_01\A1.txt') 


def read_txt(file):
    """
    Opens and reads a Txt file and closes it.
    
    Arguments:
        file : ".\DAY_01\A1.txt"
    Usage:
        A = CHEATSHEETV1.read_txt(".\DAY_01\A1.txt")
    Returns:
        The text file as a list
    """
    #open file
    with open(file) as file:

    #create array
        List_Name = [line.rstrip() for line in file]

    #loop through each line in file
   

    #close file
    file.close()

    #print array
    #print( List_Name)
    
    #Return List
    return List_Name


"""
Check if a set or string or a list is empty
"""
def Check_Empty(input):
    
    """
    Check if a set or string or a list is empty
    
    Arguments:
        
    s = set()
    X = 'ABCDS'
    Y = ''
    Z = []
    J = [1,2,3]

    Usage:
        
    print(CS.Check_Empty(J))
    
    Returns:
        Return True if Empty
    """
    isEmpty = (len(input) == 0)
     
    if isEmpty:
        return True
    else:
        return False