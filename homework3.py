# -*- coding: utf-8 -*-
"""Homework3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZBZQeB3qYMqYJIUDLi_k6xH3RgtE4Hk-
"""

import random
N = int(input("How many sticks in the pile: "))
print("There are",N,"sticks in the pile")
Name = input("what is your name: ")
count = 0
while N > 0 :
    i = random.randint(1,2)

    if N == 5 :
        i = 1       
    elif N == 6 :
        i = 2
    elif N == 1:
        i = 1
    elif N == 3 :
        i = 2
    elif N == 8 :
        i = 1
    elif N == 2 :
        i = 1
    print("I, smart computer take: ", i)
    N = N - i

    if N == 0 :
        print("I, smart computer, take the last stick")
        print(Name," Win!")
        break
    if N > 0  :
        print("There are", N,"sticks in the pile")
    ## take x
        print("How many you take in the pile (1 or 2): ")
        x = int(input()) 
        if x > 2 :
            print("No you cannot take more than 2 sticks!")
        elif x < 1 :
            print("No you cannot take more less than 1 stick!")
        elif x > N :
            print("There are no enough stick to take")
        else :
    
            N = N-x
        if N > 0 :
            print("There are", N,"sticks in the pile")
        if N == 0 :
            print(Name,", Take the last stick ")
            print("I, smart computer Win!")
            break 

        