#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 14:59:34 2021

@author: kritixblaze
"""

def addNumbers():
    x = 5
    y = 10
    print(x + y)
    
def subNumbers(x, y):
    print(x - y)
    
def mulNumbers(x, y, z):
    product = x * y * z
    return product

def divNumbers(x, y=1):
    print(x/y)

def sumOfAllNumbers(*a):
    pass

p1 = mulNumbers(10, 20, 30)
divNumbers(10)