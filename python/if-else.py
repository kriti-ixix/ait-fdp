#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 15:10:53 2021

@author: kritixblaze
"""

age = int(input("Enter your age: "))

if age > 17:
    print("You are eligible to vote")
    
elif age > 15 and age < 18:
    print("You are almost eligible to vote")

else:
    print("You are not eligible to vote")