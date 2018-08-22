from turtle import *

setup()
title('draw shapes')
bgcolor('white')
pencolor('black')
speed('slow')

def horizontal_lines_of_the_net(gap_between_lines, langth_of_lines):
    left(90)
    up()
    fd(gap_between_lines)
    down()
    left(90)
    fd(langth_of_lines)
    up()
    right(90)
    fd(gap_between_lines)
    down()
    right(90)
    fd(langth_of_lines)

def goal_net():
    # Draw the metal Bars of the goals
    pencolor('red')
    left(90)
    fd(75)
    left(90)
    fd(100)
    left(90)
    fd(75)
    bk(10)
    left(90)
    pencolor('gray')
    fd(100)
    # right_to_left_netlines()
    for netlines in range(6):
        horizontal_lines_of_the_net(5, 100)
    up()
    # Move the turtle into postion to draw the vertical lines
    left(90)
    fd(5)
    left(90)
    fd(5)
    left(90)
    down()
    # Start drawing the lines of the net
    for netline in range(9):
        fd(65)
        right(90)
        fd(5)
        right(90)
        fd(65)
        left(90)
        fd(5)
        left(90)
    fd(65)
goal_net()
