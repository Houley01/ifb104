from turtle import *

setup()
title('draw shapes')
bgcolor('white')
pencolor('black')
speed('normal')


# 8 Bit Microcontroller
pensize(1) # makes sure the pen size is set to 1 before drawing the token
pencolor('black')
# Body
up()
seth(90)
fd(5)
fillcolor('black')
begin_fill()
setheading(0)
down()
fd(20)
seth(90)
fd(90)
seth(180)
fd(40)
seth(270)
fd(90)
seth(0)
fd(0)
fd(20)
end_fill()
# Move to the end of the box
up()
fd(20)
seth(90)
# 4 Metal pin on the right
fillcolor('gray')
for pin in range(4): # Repeat this step 4 times
    up()
    setheading(90)
    fd(15)
    setheading(0)
    down()
    begin_fill()
    fd(10)
    seth(90)
    fd(5)
    seth(180)
    fd(10)
    end_fill()
# Move to the top left corner
up()
seth(90)
fd(10)
seth(180)
fd(40)
# 4 Mental pins
# Right Bottom Pin
for pin in range(4): # Repeat this step 4 times
    up()
    setheading(270)
    fd(15)
    setheading(180)
    down()
    begin_fill()
    fd(10)
    seth(270)
    fd(5)
    seth(0)
    fd(10)
    end_fill()
# Return to the start of the token.
up()
fd(20)
seth(270)
fd(15)
