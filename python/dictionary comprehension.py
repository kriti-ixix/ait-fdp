#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 15:05:55 2021

@author: kritixblaze
"""

l1 = list(range(1, 11))
l2 = [i**2 for i in l1]
print(l1)
print(l2)

'''
d1 = {}

for (x,y) in zip(l1, l2):
    d1[x] = y
'''

d1 = {x:y for (x, y) in zip(l1, l2)}
   
print(d1)