# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 20:33:18 2022

@author: shykul
"""

year = int(input("Enter an integer number:"))   
if year%4!=0:
    print(year,"is not leap year")
else:
    if year%100!=0:
        print(year,"is leap year")
    else:
        if year%400!=0:
            print(year,"is not leap year")
        else:
            print(year,"is leap year")