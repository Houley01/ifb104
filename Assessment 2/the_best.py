
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: *****PUT YOUR STUDENT NUMBER HERE*****
#    Student name: *****PUT YOUR NAME HERE*****
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  The Best, Then and Now
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application that allows the user to preview and print lists of
#  top-ten rankings.  See the instruction sheet accompanying this
#  file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.  YOU MAY NOT USE
# ANY NON-STANDARD MODULES SUCH AS 'Beautiful Soup' OR 'Pillow'.  ONLY
# MODULES THAT COME WITH A STANDARD PYTHON 3 INSTALLATION MAY BE
# USED.

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)
from urllib.request import urlopen

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.)
from tkinter import *

# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL

# Import the standard SQLite functions (just in case they're
# needed).
from sqlite3 import *

#
#--------------------------------------------------------------------#



#-----Downloader Function--------------------------------------------#
#
# This is our function for downloading a web page's content and both
# saving it on a local file and returning its source code
# as a Unicode string. The function tries to produce a
# meaningful error message if the attempt fails.  WARNING: This
# function will silently overwrite the target file if it
# already exists!  NB: You should change the filename extension to
# "xhtml" when downloading an XML document.  (You do NOT need to use
# this function in your solution if you choose to call "urlopen"
# directly, but it is provided for your convenience.)
#
def download(url, target_filename, filename_extension):

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        web_page = urlopen(url)
    except ValueError:
        raise Exception("Download error - Cannot find document at URL '" + url + "'")
    except HTTPError:
        raise Exception("Download error - Access denied to document at URL '" + url + "'")
    except:
        raise Exception("Download error - Something went wrong when trying to download " + \
                        "the document at URL '" + url + "'")

    # Read its contents as a Unicode string
    try:
        web_page_contents = web_page.read().decode('UTF-8')
    except UnicodeDecodeError:
        raise Exception("Download error - Unable to decode document at URL '" + \
                        url + "' as Unicode text")

    # Write the contents to a local text file as Unicode
    # characters (overwriting the file if it
    # already exists!)
    try:
        text_file = open(target_filename + '.' + filename_extension,
                         'w', encoding = 'UTF-8')
        text_file.write(web_page_contents)
        text_file.close()
    except:
        raise Exception("Download error - Unable to write to file '" + \
                        target_file + "'")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

main_screen = Tk() # Main screen


#____________________ Setup ____________________#

# Main screen settings
main_screen.title('Runescape') # Title
# main_screen.geometry('400x400') # Set the screen size

#____________________ End of Set Up ____________________#

#____________________ Variables ____________________#
top_10_radio = IntVar()
main_screen_logo_image = PhotoImage(file = 'archive/images/placeholder.png')
#____________________ End of Variables ____________________#

#____________________ Widgets ____________________#
runescape_logo_label = Label(image = main_screen_logo_image)
preview_button = Button(text = ' Preview', font = ('Arial', 24))
updated_button = Button(text = ' Updated', font = ('Arial', 24))

# group 1
group_1_preview_radio_button = Radiobutton(text = ' Previous', variable = top_10_radio, value = 1)
group_1_current_radio_button = Radiobutton(text = ' Current', variable = top_10_radio, value = 2)

# group 2
group_2_preview_radio_button = Radiobutton(text = ' Previous', variable = top_10_radio, value = 3)
group_2_current_radio_button = Radiobutton(text = ' Current', variable = top_10_radio, value = 4)

# group 3
group_3_preview_radio_button = Radiobutton(text = ' Previous', variable = top_10_radio, value = 5)
group_3_current_radio_button = Radiobutton(text = ' Current', variable = top_10_radio, value = 6)

#____________________ End of Widget ____________________#
def preview_list_in_new_window():
    if top_10_radio == 1: # Previous player data
        rs3_player_xp_screen = Tk() # Top 10 xp gained today after 10am to 9:59am the next day

    elif top_10_radio == 2: # Current player data
        rs3_player_xp_screen = Tk() # Top 10 xp gained today after 10am to 9:59am the next day

    elif top_10_radio == 3: # Previous clan data
        clan_ranking = Tk() # Top 10 clans clan for the day.

    elif top_10_radio == 4: # Current clan data
        clan_ranking = Tk() # Top 10 clans clan for the day.

    elif top_10_radio == 5: # Previous player data from old school RuneScape
        oldschool_player_xp_screen = Tk() # Top 10 xp gained today after 10am to 9:59am the next day

    elif top_10_radio == 6: # Current player data from old school RuneScape
        oldschool_player_xp_screen = Tk() # Top 10 xp gained today after 10am to 9:59am the next day
        
    else:
        pass
def export_list_to_web():
    pass
# Top 10 xp gained screen settings
# player_xp_screen.title('Top 10 XP Gained Today') # Title
# player_xp_screen.geometry('400x400') # Set the screen size
#
# # Top 10 clans Settins
# clan_ranking.title('Top 10 Clan with the most of XP Today') # Title
# clan_ranking.geometry('400x400') # Set the screen size

#____________________ Widget Placement ____________________#
# Sceen 1
runescape_logo_label.grid(column=0, row=0, columnspan=2, rowspan=3, sticky=W+E+N+S)
group_1_preview_radio_button.grid(column=3, row=0)
group_1_current_radio_button.grid(column=4, row=0)
group_2_preview_radio_button.grid(column=3, row=1)
group_2_current_radio_button.grid(column=4, row=1)
group_3_preview_radio_button.grid(column=3, row=2)
group_3_current_radio_button.grid(column=4, row=2)
preview_button.grid(column=3, row=3)
updated_button.grid(column=4, row=3)

# Screen 2
# Screen 3s
#____________________ End 0f Widget Placement ____________________#

#__________ Collect Information from Websie ____________#
def download_top_10_player():
    download('http://www.runeclan.com/xp-tracker', 'archive/player', 'html')

def download_top_10_clan():
    download('http://www.runeclan.com/hiscores', 'archive/clan', 'html')

def download_top_10_old_school():
    download('http://oldschool.runeclan.com/xp-tracker', 'archive/old_school_xp', 'html')

# download_top_10_clan()
# download_top_10_player()
# download_top_10_old_school()
#__________  End of Collect Information from Websie ____________#
# Start the event loop
main_screen.mainloop() # Main Screen
# player_xp_screen.mainloop() # Top 10 players of the day.
# clan_ranking.mainloop() # Top 10 clans for the day.
