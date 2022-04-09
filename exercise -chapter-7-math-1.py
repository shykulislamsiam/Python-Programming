# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:50:53 2022

@author: shykul
"""

import turtle
def draw_square(side_length):
    for i in range(3):
        turtle.forward(side_length)
        turtle.left(120)
draw_square(100)
turtle.exitonclick()