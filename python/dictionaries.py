#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:52:32 2021

@author: kritixblaze
"""

myDict = {"A":10, 20:"B", 40:True, "Hey":"Hi"}
'''
print(myDict)
print(myDict[40])
print(myDict["A"])
'''
myDict["A"] = 40
#print(myDict)
myDict["Kriti"] = "Bhatia"
#print(myDict)
'''
for k in myDict.keys():
    print(k)
'''

#print(myDict.keys())
#print(myDict.values())
#print(myDict.items())

#Dictionary unpacking
for (x, y) in myDict.items():
    print("Key:", x, "Value:", y)