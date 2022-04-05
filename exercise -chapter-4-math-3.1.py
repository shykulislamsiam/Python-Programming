# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 20:08:26 2022

@author: shykul
"""
year = int(input("Enter an integer number:"))
if year%400==0:
    print(year,"is leap year")
elif year%100==0:
    print(year,"is not leap year")
elif year%4==0:
   print(year,"is leap year")
else:
   print(year,"is not leap year")  
   
  

