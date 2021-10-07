#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:41:48 2021

@author: kritixblaze
"""
'''
s1 = {"XYZ", 4.5, "Hi", "ABC"}
print(s1)
s1.add(50)
print(s1)
s1.add("Hi")
print(s1)

s = set()

l1 = [1, 2, 3, "Hi", 1, 5, 1, 2]
newList = list(set(l1))
print(newList)
'''

s1 = {1, 2, 4, 6, 8}
s2 = {2, 5, 10, 30}

#Union
print(s1 | s2)
print(s1.union(s2))

#Intersection
print(s1 & s2)
print(s1.intersection(s2))

#Set Difference
print(s1 - s2)
print(s1.difference(s2))

#Symmetric Difference
print(s1 ^ s2)
print(s1.symmetric_difference(s2))

