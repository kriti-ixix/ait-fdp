#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 14:50:40 2021

@author: kritixblaze
"""

i = 1

while i<11:
    print(i)
    i += 1

#range(start=0, stop (exclusive), step=1)

for x in range(1, 11):
    print(x, end="\t")

s1 = "Hello world!"

for s in s1:
    print(s)
    
for s in s1[::-1]:
    print(s)

if 'o' in s1:
    print(True)
else:
    print(False)
