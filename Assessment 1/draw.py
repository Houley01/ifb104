from turtle import *

setup()
title('draw shapes')
bgcolor('white')
pencolor('black')
speed('normal')

pensize(1) # makes sure the pen size is set to 1 before drawing the token
pencolor('black')
fillcolor('blue') # Fill colour for the ardunio icon background
begin_fill()
circle(50)
end_fill()
up() # Pen up
setheading(90)
fd(50) # Forward
setheading(0)
down() # Pen Down
pencolor('white') # Change pen colour to white for the infenty sign
setheading(90)
pensize(5)
circle(20) # Circle drawn to the left inside the blue circle
circle(-20) # Circle drawn to the right inside the blue circle
up() # Pen up
setheading(0)
fd(12)
down()
fd(14.5)
bk(7.25)
setheading(90)
fd(7.25)
bk(14.5)
fd(7.25)
# Move for the negitve sign
up() # Pen up
setheading(180)
fd(31.5)
down()
fd(14.5)
pensize(1) # Returns the pen size back to the orginal size for the next token
up() # Pen up for the next token to be drawn
bk(26.75)
setheading(90)
bk(50)

    
# def horizontal_lines_of_the_net(gap_between_lines, langth_of_lines):
#     left(90)
#     up()
#     fd(gap_between_lines)
#     down()
#     left(90)
#     fd(langth_of_lines)
#     up()
#     right(90)
#     fd(gap_between_lines)
#     down()
#     right(90)
#     fd(langth_of_lines)
#
# def goal_net():
#     # Draw the metal Bars of the goals
#     pencolor('red')
#     left(90)
#     fd(75)
#     left(90)
#     fd(100)
#     left(90)
#     fd(75)
#     bk(10)
#     left(90)
#     pencolor('gray')
#     fd(100)
#     # right_to_left_netlines()
#     for netlines in range(6):
#         horizontal_lines_of_the_net(5, 100)
#     up()
#     # Move the turtle into postion to draw the vertical lines
#     left(90)
#     fd(5)
#     left(90)
#     fd(5)
#     left(90)
#     down()
#     # Start drawing the lines of the net
#     for netline in range(9):
#         fd(65)
#         right(90)
#         fd(5)
#         right(90)
#         fd(65)
#         left(90)
#         fd(5)
#         left(90)
#     fd(65)
# goal_net()
