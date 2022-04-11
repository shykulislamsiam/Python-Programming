# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 20:32:20 2022

@author: shykul
"""

def solve(s):
    s = list(s)
    for i in range(0,len(s)-1,2):
        s[i],s[i+1] = s[i+1],s[i]
    return "".join(s)

s = input("Please enter any integer:")
print(solve(s))