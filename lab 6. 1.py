# -*- coding: utf-8 -*-
"""
Created on Sun May 16 10:33:32 2021

@author: marty
"""

x = input("x = ")
x = int(x)
for i in range(-x, x+1):
    if(i % 2 == 0):
        print(i)