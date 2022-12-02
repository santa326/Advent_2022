# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 16:11:09 2022

@author: santa
"""

#This has to be the longest code for a simple problem.
# Could have been done in a simple way if planned or praticed
  
with open("A2.txt") as file:
    lines = [line.rstrip() for line in file]

plays = []

i=0
for line in lines:
    plays.insert(i,line.split(' '))
    i=i+1


#QUESTION 1        
#A for Rock, B for Paper, and C for Scissors
#X for Rock, Y for Paper, and Z for Scissors

Player_Score = 0
Elf_Score = 0

j=0

for hand in plays:
    if hand[0] == 'A' and hand[1] == 'Y':
        #print('You win')
        Player_Score = Player_Score + 2 + 6
    elif hand[0] == 'B' and hand[1] == 'Z':
        #print('You win')
        Player_Score = Player_Score + 3 + 6
    elif hand[0] == 'C' and hand[1] == 'X':
        #print('You win')
        Player_Score = Player_Score + 1 + 6
    elif hand[0] == 'A' and hand[1] == 'Z':
        #print('You loose')
        Player_Score = Player_Score + 3 + 0
    elif hand[0] == 'B' and hand[1] == 'X':
        #print('You loose')
        Player_Score = Player_Score + 1 + 0
    elif hand[0] == 'C' and hand[1] == 'Y':
        #print('You loose')
        Player_Score = Player_Score + 2 + 0
    elif hand[0] == 'A' and hand[1] == 'X':
        #print('Tie')
        Player_Score = Player_Score + 1 + 3
    elif hand[0] == 'B' and hand[1] == 'Y':
        #print('Tie')
        Player_Score = Player_Score + 2 + 3
    elif hand[0] == 'C' and hand[1] == 'Z':
        #print('Tie')
        Player_Score = Player_Score + 3 + 3

print(Player_Score)
    
    
#QUESTION 2
#X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
#A for Rock, B for Paper, and C for Scissors
Player_Score2 = 0
for hand in plays:
    if hand[0] == 'A' and hand[1] == 'X':
        Player_Score2 = Player_Score2 + 3 + 0
    elif hand[0] == 'A' and hand[1] == 'Y':
        #print('You win')
        Player_Score2 = Player_Score2 + 1 + 3
    elif hand[0] == 'A' and hand[1] == 'Z':
        #print('You win')
        Player_Score2 = Player_Score2 + 2 + 6
    elif hand[0] == 'B' and hand[1] == 'X':
        #print('You win')
        Player_Score2 = Player_Score2 + 1 + 0
    elif hand[0] == 'B' and hand[1] == 'Y':
        #print('You win')
        Player_Score2 = Player_Score2 + 2 + 3
    elif hand[0] == 'B' and hand[1] == 'Z':
        #print('You win')
        Player_Score2 = Player_Score2 + 3 + 6
    elif hand[0] == 'C' and hand[1] == 'X':
        #print('You win')
        Player_Score2 = Player_Score2 + 2 + 0
    elif hand[0] == 'C' and hand[1] == 'Y':
        #print('You win')
        Player_Score2 = Player_Score2 + 3 + 3
    elif hand[0] == 'C' and hand[1] == 'Z':
        #print('You win')
        Player_Score2 = Player_Score2 + 1 + 6

print(Player_Score2)
    
