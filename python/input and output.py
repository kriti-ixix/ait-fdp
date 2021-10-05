#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 14:33:24 2021

@author: kritixblaze
"""
'''
print('Hello world!')
x = 5
y = 10
z = x + y
print(x, y, z, sep='\n', end="...")
print(f"The sum of {x} and {y} is {z}")
print("The sum of {} and {} is {}".format(x, y, z))
'''
'''
Four data types: 
    - integer
    - float
    - string
    - boolean: True / False
'''
'''
x = 5
print(type(x))
x = "Hello"
print(type(x))
x = 5.5
print(type(x))
x = False
print(type(x))
'''

name = input("Enter your name: ")
print(f"Good afternoon {name}")
print("Good afternoon", name)
print("Good afternoon " + name)

first = int(input("Enter first number: "))
second = float(input("Enter second number: "))
print(first + second)

a1 = bool("True")
a2 = str(123)
