# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 21:17:50 2022

@author: shykul
"""

my_str = input("Please enter a string:")
my_str = my_str.casefold()
rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
    print("The string is a palindrome.")
else:
    print("The string in not a palindrome")