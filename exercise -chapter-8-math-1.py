# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 17:43:27 2022

@author: shykul
"""

from string import punctuation,whitespace

my_string = input("Please enter any string:")
upper_letters = "".join([letter for letter in my_string if letter.isupper()])
print(upper_letters)
lower_letters = "".join([letter for letter in my_string if letter.islower()])
print(lower_letters)
digit_letters = "".join([letter for letter in my_string if letter.isdigit()])
print(digit_letters)
other_ele = "".join([letter for letter in my_string if letter in punctuation or letter 
                     in whitespace])
print(other_ele)