# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 20:20:29 2022

@author: shykul
"""

year = int(input("Enter an integer number:"))   
if year%100!=0 and year%4==0:
    print(year,"is leap year")
elif year%100==0 and year%400==0:
    print(year,"is leap year") 
else:
    print(year,"is not leap year")    
