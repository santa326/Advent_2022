# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 12:38:02 2022

@author: santa
"""
import re
import CS

Lines = CS.read_txt('1.txt')


def get_trailing_number(s):
    if s[-1] == ':':
        m = re.search(r'\d+$', s[0:len(s)-1])
    else:
        m = re.search(r'\d+$', s)
    return int(m.group()) if m else None



# monkeys = []

# for monk in Lines:
#     if monk[0:1] == 'M':
#         #monkeys.append([get_trailing_number(monk)])
#         monkeys.append([])
#     else:
#         pass





def Convert(string):
    li = list(string.split(","))
    return li

#Decalaring Each Task so the for loop is cleaner
task1,task2,task3,task4,task5,task6 = ('',''),('',''),('',''),('',''),('',''),('','')


#This will summerieze the input and store them in a list
Summary = []

#This variable counts the tasks processed and adds to summary task row and resets to 0
current_task = 0

#Summary Creation
for line in Lines:
    if len(line) == 0:
        task = '**********************'
        #print(task)
        current_task = 0
        #Summary.append([task1[1],task2[1],task3[1],task4[1],task5[1],task6[1]])
    elif line[0:1] == 'M':
        #print(get_trailing_number(line))
        task1 = 'M', get_trailing_number(line)
        #print(task1)
        #Summary.append(task1)
        current_task = current_task + 1
    elif line[2:3] == 'S':
        task2 = 'S',line[18:len(line)]
        t2 = eval(task2[1])
        current_task = current_task + 1
        #arr = eval(task2[1])
        #print(arr)
        #omg = task[1]
        #print(task2)
    elif line[2:3] == 'O':
        task3 = 'O',line[19:len(line)]
        current_task = current_task + 1
        #new = eval(task[1])
        #print(new)
        #print(task3)
    elif line[2:3] == 'T':
        task4 = 'T', get_trailing_number(line)
        current_task = current_task + 1
        #print(task4)
    elif line[7:11] == 'true':
        task5 = '1', get_trailing_number(line)
        current_task = current_task + 1
        #print(task5)
    elif line[7:12] == 'false':
        task6 = '0', get_trailing_number(line)
        current_task = current_task + 1
        #print(task6)
    if current_task == 6:
        Summary.append([task1[1],task2[1],task3[1],task4[1],task5[1],task6[1]])
    else:
        pass

#Running the Summary of Instuctions X times


#Adding Items_Monk
monkeys = []
count = []

for monk in Summary:
    monkeys.append(Convert(monk[1]))
    count.append(0)

X = 20

for run in range(0,X):
    print(X)
    
    #Parse The summary list
    for i in range(0,len(Summary)):
        #start_item = Convert(Summary[i][1])
        #print(Summary[i])
        #print(monkeys[i])
        #print(start_item)
        print(Summary[i][1])
        #Each summary will run for the number of items in task 2
        while len(monkeys[i]) != 0:
            count[i] = count[i]+1
        #for j in range(0,len(monkeys[i])):
            #print(monkeys[i])
            #print(monkeys[j])
            #TASK 2 : Set worry level
            
            #print(run,'-',len(monkeys[i]))
            
            new = 0
            old = int(monkeys[i][0])
            
            #print('Current Worry Level :' , old)
            
            #TASK 3: Updating worry level
            #print(Summary[i][2])
            new = eval(Summary[i][2])
            #print(new)
            
            #print('Increased Worry Level :' , new)
            
            #TASK 3.1 Worry/3 round down to nearest integet 
            #MAKE SURE // is accurate
            new = new//3
            
            #print('New Worry Level :' , new)
        
            #TASK 4 TEST  if divisible by Y
            true_M = Summary[i][4]
            false_M = Summary[i][5]
            Y = Summary[i][3]
            if new % Y == 0:
                #print('True')
                monkeys[true_M].append(new)
                monkeys[i].pop(0)
            else:
                #print('False')
                monkeys[false_M].append(new)
                monkeys[i].pop(0)
            
            
#Removing String from Monkeys
count.sort(reverse=True)
Q1 = count[0]*count[1]
print(Q1)