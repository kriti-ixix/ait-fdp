#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 14:35:36 2021

@author: kritixblaze
"""

name = "Kriti"
s1 = f"Hello my name is {name}"
s2 = "Hello world!"

#String Indexing
print(s2[2])
print(s2[-1])
print(s2[-2])

#String slicing
#[start=0: stop=last (exclusive): step=1]
print(s2[1:5])
print(s2[1:8:2])
print(s2[-2:])
print(s2[::-1]) #Reverses the string
print(s2.reverse())

print(s2.upper())
print(s2.lower())

#Splitting a string
print(s1)
print(s1.split())
print(s1.split('i'))

print(len(s1))
print(len(s1.split()))