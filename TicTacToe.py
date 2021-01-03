# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import sys
import random
game=[" ", " ", " ", " ", " ", " ", " ", " ", " "]
def print_game():
    print (game[0]+" |" + game[1]+" |" + game[2])
    print ("__|__|__")
    print (game[3]+" |" + game[4]+" |" + game[5])
    print ("__|__|__")
    print (game[6]+" |" + game[7]+" |" + game[8])
    print ("  |  |  ")

#Define function for player 1 move

def play1(p):
    print("Choose an empty space from 1-9")
    t=int(input())
    if game[t-1]!=" ":
        print ("space not empty")
        play1(p)
    else:
        game[t-1]=p
        print_game()
        
#Define function for player 2 move
       
def play2(n,p):
    blank_spaces=[]
    for i in range(9):
        if game[i]==" ":
            blank_spaces.append(i)
            game[i]=6
    case1=list((game[0], game[1],game[2]))
    case2=list((game[0], game[3],game[6]))
    case3=list((game[0], game[4],game[8]))
    case4=list((game[1], game[4],game[7]))
    case5=list((game[2], game[5],game[8]))
    case6=list((game[2], game[4],game[6]))
    case7=list((game[3], game[4],game[5]))
    case8=list((game[6], game[7],game[8]))
    
    #dictionary of all possible cases
    
    result={1:case1,2:case2,3:case3,4:case4,5:case5,6:case6,7:case7,8:case8}    
    
    #dictionary to find out blank spaces in which next move can be played
    
    result1={1:(0,1,2),2:(0,3,6),3:(0,4,8),4:(1,4,7),5:(2,5,8),6:(2,4,6),7:(3,4,5),8:(6,7,8)}    
    
    #check if winning in next move (attack)
    
    for i in range(1,9):
        if result[i].count (6)==1 and result[i].count(p)==2:
                s=result[i].index(6)
                t=result1[i][s]
                game[t]=p
                break
            
    #check if losing in next move (defend)
    #check only if not winning in next move
    
    else:
        for i in range(1,9):
            if result[i].count (6)==1 and result[i].count(n)==2:
                    s=result[i].index(6)
                    t=result1[i][s]
                    game[t]=p
                    break            
                
    #random move if no win or loss in next move
    #check only if neither winning nor losing in next move
    
        else:
                s=random.choice(blank_spaces)
                game[s]=p
        
    for i in range(9):
        if game[i]==6:
            game[i]=" "
    print ("Player 2 has played")
    print_game()      
    
def check_result(p1,p2):
    value=6
    for i in range(9):
        if game[i]==" ":
            game[i]=6
    solution1=list(set((game[0], game[1],game[2])))
    solution2=list(set((game[0], game[3],game[6])))
    solution3=list(set((game[0], game[4],game[8])))
    solution4=list(set((game[1], game[4],game[7])))
    solution5=list(set((game[2], game[5],game[8])))
    solution6=list(set((game[2], game[4],game[6])))
    solution7=list(set((game[3], game[4],game[5])))
    solution8=list(set((game[6], game[7],game[8])))
    result=[solution1,solution2,solution3,solution4,solution5,solution6,solution7,solution8]    
    for i in range(8):
        if len(result[i])==1 and result[i][0]!=6:
            if result[i][0]==p1:
                print ("Player 1 wins")
            else:
                print ("Player 2 wins")
            value=5
    count=0
    for i in range(9):
        if game[i]==6:
            game[i]=" "
            count+=1
            
    #check if all boxes are filled up (draw)
    
    if count==0 and value==6:
        print ("It's a draw")
        sys.exit()
        return 3
    elif value==5:
        return 1
    else:
        return 2
        
def begin():
    n=2
    print(" Press 1) Player1='X' and Player2= '0' \n 2) Player1='0' and Player2= 'X'")
    tr=int(input())
    if tr==1:
        player1='X'
        player2='0'
    else:
        player1='0'
        player2='X'
    while True:
        print("Player1's turn")
        play1(player1)
        n=check_result(player1,player2)
        if n==1:
            sys.exit()
        #print("Player2's turn")
        play2(player1,player2)
        n=check_result(player1,player2)
        if n==1:
            sys.exit()
print("The pattern of tic tac toe board is as follows:")
print("1 |2 |3")
print("__|__|__")
print("4 |5 |6")
print("__|__|__")
print("7 |8 |9")
print("  |  |  ")
begin()




