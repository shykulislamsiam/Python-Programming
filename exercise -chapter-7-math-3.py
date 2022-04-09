# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 23:51:30 2022
@author: shykul
"""
def mult_num(n=1):
    m = 1
    while m <= 10:
        print(n,"x",m,"=",n*m)
        m += 1
mult_num(n=1)


def mult_num(n):
    m = 1
    while m <= 10:
        print(n,"x",m,"=",n*m)
        m += 1
n = int(input("Please enter an integer number:"))
mult_num(n)





    
    
