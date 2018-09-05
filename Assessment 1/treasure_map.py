
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10353950
#    Student name: Ethan Houley
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  TREASURE MAP
#
#  This assignment tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "follow_path".  You are required to
#  complete this function so that when the program is run it traces
#  a path on the screen, drawing "tokens" to indicate discoveries made
#  along the way, while using data stored in a list to determine the
#  steps to be taken.  See the instruction sheet accompanying this
#  file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.

from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

grid_size = 100 # pixels
num_squares = 7 # to create a 7x7 map grid
margin = 50 # pixels, the size of the margin around the grid
legend_space = 400 # pixels, the space to leave for the legend
window_height = grid_size * num_squares + margin * 2
window_width = grid_size * num_squares + margin +  legend_space
font_size = 18 # size of characters for the coords
starting_points = ['Top left', 'Top right', 'Centre',
                   'Bottom left', 'Bottom right']

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.  (Very keen students are welcome
# to draw their own background, provided they do not change the map's
# grid or affect the ability to see it.)
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas():

    # Set up the drawing window with enough space for the grid and
    # legend
    setup(window_width, window_height)
    setworldcoordinates(-margin, -margin, window_width - margin,
                        window_height - margin)

    # Draw as quickly as possible
    tracer(False)

    # Choose a neutral background colour (if you want to draw your
    # own background put the code here, but do not change any of the
    # following code that draws the grid)
    bgcolor('light grey')

    # Get ready to draw the grid
    penup()
    color('slate grey')
    width(2)

    # Draw the horizontal grid lines
    setheading(0) # face east
    for y_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        penup()
        goto(0, y_coord)
        pendown()
        forward(num_squares * grid_size)

    # Draw the vertical grid lines
    setheading(90) # face north
    for x_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        penup()
        goto(x_coord, 0)
        pendown()
        forward(num_squares * grid_size)

    # Draw each of the labels on the x axis
    penup()
    y_offset = -27 # pixels
    for x_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        goto(x_coord, y_offset)
        write(str(x_coord), align = 'center',
              font=('Arial', font_size, 'normal'))

    # Draw each of the labels on the y axis
    penup()
    x_offset, y_offset = -5, -10 # pixels
    for y_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        goto(x_offset, y_coord + y_offset)
        write(str(y_coord), align = 'right',
              font=('Arial', font_size, 'normal'))

    # Mark the space for drawing the legend
    goto(800, 680)
    pencolor('white')
    write('    Electronic', align = 'left', font=('Arial', 24, 'normal'))
    goto(800, 550)
    token0()
    goto(850, 600)
    pencolor('white')
    write('  Arduino IDE Icon', align = 'left', font=('Arial', 18, 'normal'))

    goto(800, 450)
    token1()
    goto(850, 500)
    pencolor('white')
    write('Light Emitting Diode', align = 'left', font=('Arial', 18, 'normal'))

    goto(800, 350)
    token2()
    pencolor('white')
    goto(850, 400)
    write('8-Bit Microcontroller', align = 'left', font=('Arial', 18, 'normal'))

    goto(800, 250)
    token3()
    pencolor('white')
    goto(850, 300)
    write(' Triode Transistor', align = 'left', font=('Arial', 18, 'normal'))

    goto(800, 150)
    token4()
    pencolor('white')
    goto(850, 200)
    write(' Push Switch', align = 'left', font=('Arial', 18, 'normal'))


    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()

#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the follow_path function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_path function appearing below.  Your
# program must work correctly for any data set that can be generated
# by the random_path function.
#
# Each of the data sets is a list of instructions expressed as
# triples.  The instructions have two different forms.  The first
# instruction in the data set is always of the form
#
#     ['Start', location, token_number]
#
# where the location may be 'Top left', 'Top right', 'Centre',
# 'Bottom left' or 'Bottom right', and the token_number is an
# integer from 0 to 4, inclusive.  This instruction tells us where
# to begin our treasure hunt and the token that we find there.
# (Every square we visit will yield a token, including the first.)
#
# The remaining instructions, if any, are all of the form
#
#     [direction, number_of_squares, token_number]
#
# where the direction may be 'North', 'South', 'East' or 'West',
# the number_of_squares is a positive integer, and the token_number
# is an integer from 0 to 4, inclusive.  This instruction tells
# us where to go from our current location in the grid and the
# token that we will find in the target square.  See the instructions
# accompanying this file for examples.
#

# Some starting points - the following fixed paths just start a path
# with each of the five tokens in a different location

fixed_path_0 = [['Start', 'Top left', 0]]
fixed_path_1 = [['Start', 'Top right', 1]]
fixed_path_2 = [['Start', 'Centre', 2]]
fixed_path_3 = [['Start', 'Bottom left', 3]]
fixed_path_4 = [['Start', 'Bottom right', 4]]

# Some miscellaneous paths which encounter all five tokens once

fixed_path_5 = [['Start', 'Top left', 0], ['East', 1, 1], ['East', 1, 2],
                ['East', 1, 3], ['East', 1, 4]]
fixed_path_6 = [['Start', 'Bottom right', 0], ['West', 1, 1], ['West', 1, 2],
                ['West', 1, 3], ['West', 1, 4]]
fixed_path_7 = [['Start', 'Centre', 4], ['North', 2, 3], ['East', 2, 2],
                ['South', 4, 1], ['West', 2, 0]]

# A path which finds each token twice

fixed_path_8 = [['Start', 'Bottom left', 1], ['East', 5, 2],
                ['North', 2, 3], ['North', 4, 0], ['South', 3, 2],
                ['West', 4, 0], ['West', 1, 4],
                ['East', 3, 1], ['South', 3, 4], ['East', 1, 3]]

# Some short paths

fixed_path_9 = [['Start', 'Centre', 0], ['East', 3, 2],
                ['North', 2, 1], ['West', 2, 3],
                ['South', 3, 4], ['West', 4, 1]]

fixed_path_10 = [['Start', 'Top left', 2], ['East', 6, 3], ['South', 1, 0],
                 ['South', 1, 0], ['West', 6, 2], ['South', 4, 3]]

fixed_path_11 = [['Start', 'Top left', 2], ['South', 1, 0], ['East', 2, 4],
                 ['South', 1, 1], ['East', 3, 4], ['West', 1, 3],
                 ['South', 2, 0]]

# Some long paths

fixed_path_12 = [['Start', 'Top right', 2], ['South', 4, 0],
                 ['South', 1, 1], ['North', 3, 4], ['West', 4, 0],
                 ['West', 2, 0], ['South', 3, 4], ['East', 2, 3],
                 ['East', 1, 1], ['North', 3, 2], ['South', 1, 3],
                 ['North', 3, 2], ['West', 1, 2], ['South', 3, 4],
                 ['East', 3, 0], ['South', 1, 1]]

fixed_path_13 = [['Start', 'Top left', 1], ['East', 5, 3], ['West', 4, 2],
                 ['East', 1, 3], ['East', 2, 2], ['South', 5, 1],
                 ['North', 2, 0], ['East', 2, 0], ['West', 1, 1],
                 ['West', 5, 0], ['South', 1, 3], ['East', 3, 0],
                 ['East', 1, 4], ['North', 3, 0], ['West', 1, 4],
                 ['West', 3, 1], ['South', 4, 1], ['East', 5, 1],
                 ['West', 4, 0]]

# "I've been everywhere, man!" - this path visits every square in
# the grid, with randomised choices of tokens

fixed_path_99 = [['Start', 'Top left', randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)]

# If you want to create your own test data sets put them here
# NOTE: Custom testing
fixed_path_c = [['Start', 'Bottom left', 2], ['North', 1, 2], ['East', 1, 2], ['East', 1, 2], ['North', 1, 2], ['West', 1, 2], ['South', 2, 2]]
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to assess your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a path
# to follow.  Your program must work for any data set that can be
# returned by this function.  The results returned by calling this
# function will be used as the argument to your follow_path function
# during marking.  For convenience during code development and
# marking this function also prints the path to be followed to the
# shell window.
#
# Note: For brevity this function uses some Python features not taught
# in IFB104 (dictionaries and list generators).  You do not need to
# understand this code to complete the assignment.
#
def random_path(print_path = True):
    # Select one of the five starting points, with a random token
    path = [['Start', choice(starting_points), randint(0, 4)]]
    # Determine our location in grid coords (assuming num_squares is odd)
    start_coords = {'Top left': [0, num_squares - 1],
                    'Bottom left': [0, 0],
                    'Top right': [num_squares - 1, num_squares - 1],
                    'Centre': [num_squares // 2, num_squares // 2],
                    'Bottom right': [num_squares - 1, 0]}
    location = start_coords[path[0][1]]
    # Keep track of squares visited
    been_there = [location]
    # Create a path up to 19 steps long (so at most there will be 20 tokens)
    for step in range(randint(0, 19)):
        # Find places to go in each possible direction, calculating both
        # the new grid square and the instruction required to take
        # us there
        go_north = [[[location[0], new_square],
                     ['North', new_square - location[1], token]]
                    for new_square in range(location[1] + 1, num_squares)
                    for token in [0, 1, 2, 3, 4]
                    if not ([location[0], new_square] in been_there)]
        go_south = [[[location[0], new_square],
                     ['South', location[1] - new_square, token]]
                    for new_square in range(0, location[1])
                    for token in [0, 1, 2, 3, 4]
                    if not ([location[0], new_square] in been_there)]
        go_west = [[[new_square, location[1]],
                    ['West', location[0] - new_square, token]]
                    for new_square in range(0, location[0])
                    for token in [0, 1, 2, 3, 4]
                    if not ([new_square, location[1]] in been_there)]
        go_east = [[[new_square, location[1]],
                    ['East', new_square - location[0], token]]
                    for new_square in range(location[0] + 1, num_squares)
                    for token in [0, 1, 2, 3, 4]
                    if not ([new_square, location[1]] in been_there)]
        # Choose a free square to go to, if any exist
        options = go_north + go_south + go_east + go_west
        if options == []: # nowhere left to go, so stop!
            break
        target_coord, instruction = choice(options)
        # Remember being there
        been_there.append(target_coord)
        location = target_coord
        # Add the move to the list of instructions
        path.append(instruction)
    # To assist with debugging and marking, print the list of
    # instructions to be followed to the shell window
    print('Welcome to the Treasure Hunt!')
    print('Here are the steps you must follow...')
    for instruction in path:
        print(instruction)
    # Return the random path
    return path

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#-----Drawing of tokens----------------------------------------------#
#  Token 0 is the shortcut icon for the Ardunio IDE
def token0():
    pensize(1) # makes sure the pen size is set to 1 before drawing the token
    pencolor('black')
    fillcolor('blue') # Fill colour for the ardunio icon background
    begin_fill()
    setheading(0)
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
    up() # Pen up
    bk(26.75) # Return the token back to the starting postion
    setheading(90)
    bk(50)
    pensize(1) # Returns the pen size back to the orginal size for the next token

def token1():
    # Token 2 Green Light Emitting Diode (LED)
    pensize(1) # makes sure the pen size is set to 1 before drawing the token
    pencolor('white')
    up()
    seth(90)
    fd(32)
    seth(0)
    down()
    fillcolor('green')
    begin_fill()
    fd(25)
    seth(90)
    fd(5)
    seth(180)
    fd(5)
    seth(90)
    fd(40)
    circle(20, extent=180)
    fd(40)
    seth(180)
    fd(5)
    seth(270)
    fd(5)
    seth(0)
    fd(25)
    end_fill()
    # End of led
    #------------------------------#
    # metals poles
    up()
    fillcolor('gray')
    begin_fill()
    setheading(250)
    seth(0)
    fd(12.5)
    seth(270)
    down()
    fd(25)
    seth(180)
    fd(5)
    seth(90)
    fd(25)
    seth(180)
    fd(20)
    seth(270)
    fd(30)
    seth(0)
    fd(5)
    seth(90)
    fd(30)
    end_fill()
    up()
    seth(0)
    fd(7.5)
    seth(270)
    fd(32)

def token2():
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


def token3():
    # 3 Pin, Triode Transistor
    pensize(1) # makes sure the pen size is set to 1 before drawing the token
    pencolor('black')
    up()
    seth(90)
    fd(2)
    seth(180)
    fd(10)
    for pin in range(3):
        up()
        fillcolor('gray')
        down()
        begin_fill()
        fd(5)
        setheading(90)
        fd(40)
        setheading(0)
        fd(5)
        setheading(270)
        fd(40)
        end_fill()
        setheading(0)
        up()
        fd(5)
    # Draw the transistor housing.
    up()
    bk(5)
    seth(90)
    fd(40)
    down()
    fillcolor('black')
    begin_fill()
    seth(0)
    fd(7)
    seth(90)
    fd(40)
    seth(180)
    fd(50)
    seth(270)
    fd(40)
    seth(0)
    fd(50)
    end_fill()
    # Draw the transistor heat spreader.
    fillcolor('gray')
    seth(90)
    fd(40)
    begin_fill()
    down()
    fd(18)
    seth(180)
    fd(50)
    seth(270)
    fd(18)
    end_fill()
    up()
    # Draw the circle in the heat spreader
    fillcolor('white')
    seth(0)
    fd(25)
    seth(90)
    fd(4)
    down()
    begin_fill()
    seth(0)
    circle(5)
    end_fill()
    # Return to the starting postion.
    up()
    bk(2)
    seth(270)
    fd(86)



def token4():
    # Tact switch
    pensize(1) # makes sure the pen size is set to 1 before drawing the token
    fillcolor('black')
    up()
    seth(90)
    fd(16)
    down()
    seth(0)
    begin_fill()
    fd(40)
    seth(90)
    fd(60)
    seth(180)
    fd(80)
    seth(270)
    fd(60)
    seth(0)
    fd(40)
    end_fill()
    # Draw the metal pins
    # Common mental pin
    up()
    fd(10)
    pencolor('black')
    fillcolor('gray')
    begin_fill()
    seth(270)
    down()
    fd(10)
    seth(0)
    fd(15)
    seth(90)
    fd(5)
    seth(180)
    fd(10)
    seth(90)
    fd(5)
    end_fill()
    up()
    # Draw Middle metal pin
    fd(10)
    seth(0)
    fd(25)
    down()
    begin_fill()
    fd(10)
    seth(90)
    fd(5)
    seth(180)
    fd(10)
    end_fill()
    up()
    seth(90)
    fd(10)
    fd(10)
    seth(0)
    down()
    # Draw Middle metal pin
    begin_fill()
    fd(10)
    seth(90)
    fd(5)
    seth(180)
    fd(10)
    end_fill()
    # Draw the button in for the switch.
    up()
    fd(50)
    seth(90)
    fd(20)
    fillcolor('red')
    begin_fill()
    down()
    circle(10 , extent=180)
    end_fill()
    # Return home
    up()
    fd(76)
    seth(0)
    fd(30)
# ___________________________________________________________
# This start coords is used in both bits of Code
# As it is defined in a function above the code bellow
# is unable to understand what start_coords is.
# start_coords examples where the start of the treasure
# map begins.
start_coords = {'Top left': [0, num_squares - 1],
                'Bottom left': [0, 0],
                'Top right': [num_squares - 1, num_squares - 1],
                'Centre': [num_squares // 2, num_squares // 2],
                'Bottom right': [num_squares - 1, 0]}
# ____________________________________________________________#
def follow_path(path):
    if path[0][0] == 'Start':
    # GO to the top left of the grid
        if path[0][1] == 'Top left':
            goto(start_coords['Top left'][0] * 100, start_coords['Top left'][1] * 100)
            setheading(0)
            fd(50)
            down()
            if path[0][2] == 0:
                token0()
            elif path[0][2] == 1:
                token1()
            elif path[0][2] == 2:
                token2()
            elif path[0][2] == 3:
                token3()
            elif path[0][2] == 4:
                token4()
    # Go to bottom left of the grid
        elif path[0][1] == 'Bottom left':
            pencolor('pink')
            goto(start_coords['Bottom left'][0] * 100, start_coords['Bottom left'][1] * 100)
            setheading(0)
            fd(50)
            down()
            if path[0][2] == 0:
                token0()
            elif path[0][2] == 1:
                token1()
            elif path[0][2] == 2:
                token2()
            elif path[0][2] == 3:
                token3()
            elif path[0][2] == 4:
                token4()
    # Go to top right of the screen
        elif path[0][1] == 'Top right':
            goto(start_coords['Top right'][0] * 100, start_coords['Top right'][1] * 100)
            setheading(0)
            fd(50)
            down()
            if path[0][2] == 0:
                token0()
            elif path[0][2] == 1:
                token1()
            elif path[0][2] == 2:
                token2()
            elif path[0][2] == 3:
                token3()
            elif path[0][2] == 4:
                token4()
    # Go to the center of the grid
        elif path[0][1] == 'Centre':
            goto(start_coords['Centre'][0] * 100, start_coords['Centre'][1] * 100)
            setheading(0)
            fd(50)
            down()
            if path[0][2] == 0:
                token0()
            elif path[0][2] == 1:
                token1()
            elif path[0][2] == 2:
                token2()
            elif path[0][2] == 3:
                token3()
            elif path[0][2] == 4:
                token4()
    # Go to the Bottom right of the grid
        elif path[0][1] == 'Bottom right':
            goto(start_coords['Bottom right'][0] * 100, start_coords['Bottom right'][1] * 100)
            setheading(0)
            fd(50)
            down()
            if path[0][2] == 0:
                token0()
            elif path[0][2] == 1:
                token1()
            elif path[0][2] == 2:
                token2()
            elif path[0][2] == 3:
                token3()
            elif path[0][2] == 4:
                token4()
# 2nd item in the list
    for direction in path:
        if direction[0] == 'East':
            setheading(0)
            for steps in range(7):
                if direction[1] == steps:
                    fd(steps * grid_size)
                    if direction[2] == 0:
                        token0()
                    elif direction[2] == 1:
                        token1()
                    elif direction[2] == 2:
                        token2()
                    elif direction[2] == 3:
                        token3()
                    elif direction[2] == 4:
                        token4()
        elif direction[0] == 'North':
            setheading(90)
            for steps in range(7):
                if direction[1] == steps:
                    fd(steps * grid_size)
                    if direction[2] == 0:
                        token0()
                    elif direction[2] == 1:
                        token1()
                    elif direction[2] == 2:
                        token2()
                    elif direction[2] == 3:
                        token3()
                    elif direction[2] == 4:
                        token4()
        elif direction[0] == 'West':
            setheading(180)
            for steps in range(7):
                if direction[1] == steps:
                    fd(steps * grid_size)
                    if direction[2] == 0:
                        token0()
                    elif direction[2] == 1:
                        token1()
                    elif direction[2] == 2:
                        token2()
                    elif direction[2] == 3:
                        token3()
                    elif direction[2] == 4:
                        token4()
        elif direction[0] == 'South':
            setheading(270)
            for steps in range(7):
                if direction[1] == steps:
                    fd(steps * grid_size)
                    if direction[2] == 0:
                        token0()
                    elif direction[2] == 1:
                        token1()
                    elif direction[2] == 2:
                        token2()
                    elif direction[2] == 3:
                        token3()
                    elif direction[2] == 4:
                        token4()


#--------------------------------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "follow_path" function.
#

# Follow the path as per the provided dataset

#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your solution.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('normal')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's theme
# ***** and its tokens
title("Things To Do With Electronic, Arduino IDE, Light Emitting Diode (LED), 8-bit Microprocessor, Triode Transistor, Push Switch")

### Call the student's function to follow the path
### ***** While developing your program you can call the follow_path
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_path()" as the
### ***** argument to the follow_path function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_path function.
# follow_path(fixed_path_c) # <-- used for code development only, not marking
follow_path(random_path()) # <-- used for assessment

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#
