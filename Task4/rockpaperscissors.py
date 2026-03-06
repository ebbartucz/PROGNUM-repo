#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
user = input("Make your first move: type R for rock, P for paper and S for scissors (To end game, type:'Stop'):")

code = np.array(['R', 'P', 'S'])

while user != 'Stop':
    indx = np.random.randint(0, len(code))
    turn = code[indx]
    if user == 'R' or 'P' or 'S' or 'Stop':
        print("I played:", turn)
        if user == turn:
            print("It's a tie!")
        if user == 'R':
            if turn == 'P':
                print("I won!")
            if turn == 'S':
                print("You won!")
        if user == 'P':
            if turn == 'S':
                print("I won!")
            if turn == 'R':
                print("You won!")
        if user == 'S':
            if turn == 'R':
                print("I won!")
            if turn == 'P':
                print("You won!")
        user = input("Make your first move: type R for rock, P for paper and S for scissors:")

    else:
        user = input("Make your first move: type R for rock, P for paper and S for scissors:")
        

