#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:27:52 2021

@author: kritixblaze
"""

l1 = list(range(1, 11))
print(l1)

'''
l2 = []

for i in l1:
    if i%2 == 0:
        l2.append(i ** 2)
'''

#List comprehension
l2 = [i**2 for i in l1 if i%2 == 0]
print(l2)
