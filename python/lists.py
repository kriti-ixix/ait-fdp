#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 15:05:56 2021

@author: kritixblaze
"""
'''
1. Lists
2. Tuples
3. Sets
4. Dictionaries
'''

l1 = [1, 2, 3, True, "Hello", 5.5]
l2 = []
l3 = [['A', 'B'], 5.20, "Hey"]

#print(l1)
l1.append("XYZ")
#print(l1)
l1.insert(2, "New Element")
#print(l1)
#print(len(l1))
#removedValue = l1.pop()
l2.append(l1.pop(3))
print(l1)
print(l2)
l1.remove(5.5)
print(l1)
print(l1.index(1))
#print(removedValue)


for el in l1:
    print(el)