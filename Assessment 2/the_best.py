
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: 10353950
#    Student name: Ethan Houey
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
from tkinter import messagebox

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
main_screen.title('Runescape, Race to top postion') # Title
# main_screen.geometry('400x400') # Set the screen size

#____________________ End of Set Up ____________________#

#____________________ Variables ____________________#
top_10_radio = IntVar()

# Predefinded fonts
font_heading_1 = ("Arial", 25)
button_font = ("Arial", 24)
font_times_15 = ("Times", 15)

# Images
main_screen_leftside_logo_image = PhotoImage(file="archive/images/main_screen_left.png")
main_screen_rightside_logo_image = PhotoImage(file="archive/images/main_screen_right.png")
RS3_logo_image = PhotoImage(file="archive/images/RuneScape_3_Logo.png")
OSRS_logo_image = PhotoImage(file="archive/images/Old_School_RuneScape_logo.png")
Clan_banner_image = PhotoImage(file="archive/images/Clan_Banner.png")

# Please read comments when marking
database_location = 'top_ten.db' # Change the location of the database when marked

#____________________ End of Variables ____________________#

#____________________ Predefinded  Function ____________________#
def alert(button_choice): # Create an alert box if none of the radio button are selected.
    messagebox.showinfo(title="Alert", message=button_choice)

def preview_list(): # gernerates a tkinter window with data from local files or from a website.
    if top_10_radio.get() == 1: # Previous player data
        search_rs3_player_html_archive = []
        count = 0
        archive_rs3_player_html = open('archive/player.html').read() # Open and read file located in archive with the name of player.html
        placeholder_search_rs3_player_html_archive = findall('[0-9,a-z,A-Z, ,\-,\_]+</a></td>', archive_rs3_player_html) # Find all the players name in the document
        for player in placeholder_search_rs3_player_html_archive:
            search_rs3_player_html_archive.append(placeholder_search_rs3_player_html_archive[count].replace('</a></td>', '')) # Go throught the list of runescape players and removes '</a></td>'
            count = count + 1

        rs3_player_xp_screen = Toplevel() # Top 10 xp gained today after 10am to 9:59am the next day
        rs3_player_xp_screen.title('Top 10 xp gainned in the past')
        postion_1 = Label(rs3_player_xp_screen, text="1:", font=font_times_15, justify="left")
        postion_2 = Label(rs3_player_xp_screen, text="2:", font=font_times_15, justify="left")
        postion_3 = Label(rs3_player_xp_screen, text="3:", font=font_times_15, justify="left")
        postion_4 = Label(rs3_player_xp_screen, text="4:", font=font_times_15, justify="left")
        postion_5 = Label(rs3_player_xp_screen, text="5:", font=font_times_15, justify="left")
        postion_6 = Label(rs3_player_xp_screen, text="6:", font=font_times_15, justify="left")
        postion_7 = Label(rs3_player_xp_screen, text="7:", font=font_times_15, justify="left")
        postion_8 = Label(rs3_player_xp_screen, text="8:", font=font_times_15, justify="left")
        postion_9 = Label(rs3_player_xp_screen, text="9:", font=font_times_15, justify="left")
        postion_10 = Label(rs3_player_xp_screen, text="10:", font=font_times_15, justify="left")

        player_user_name_1 = Label(rs3_player_xp_screen, text=search_rs3_player_html_archive[0], font=font_times_15, justify="left")
        player_user_name_2 = Label(rs3_player_xp_screen, text=search_rs3_player_html_archive[1], font=font_times_15, justify="left")
        player_user_name_3 = Label(rs3_player_xp_screen, text=search_rs3_player_html_archive[2], font=font_times_15, justify="left")
        player_user_name_4 = Label(rs3_player_xp_screen, text=search_rs3_player_html_archive[3], font=font_times_15, justify="left")
        player_user_name_5 = Label(rs3_player_xp_screen, text=search_rs3_player_html_archive[4], font=font_times_15, justify="left")
        player_user_name_6 = Label(rs3_player_xp_screen, text=search_rs3_player_html_archive[5], font=font_times_15, justify="left")
        player_user_name_7 = Label(rs3_player_xp_screen, text=search_rs3_player_html_archive[6], font=font_times_15, justify="left")
        player_user_name_8 = Label(rs3_player_xp_screen, text=search_rs3_player_html_archive[7], font=font_times_15, justify="left")
        player_user_name_9 = Label(rs3_player_xp_screen, text=search_rs3_player_html_archive[8], font=font_times_15, justify="left")
        player_user_name_10 = Label(rs3_player_xp_screen, text=search_rs3_player_html_archive[9], font=font_times_15, justify="left")
            # count = count + 1
        top_player_image = Label(rs3_player_xp_screen, image=RS3_logo_image)
        # Layout for top 10 players of the day
        top_player_image.grid(column=0, row=0, columnspan=4, rowspan=2)
        postion_1.grid(column=1, row=3)
        postion_2.grid(column=1, row=4)
        postion_3.grid(column=1, row=5)
        postion_4.grid(column=1, row=6)
        postion_5.grid(column=1, row=7)
        postion_6.grid(column=1, row=8)
        postion_7.grid(column=1, row=9)
        postion_8.grid(column=1, row=10)
        postion_9.grid(column=1, row=11)
        postion_10.grid(column=1, row=12)

        player_user_name_1.grid(column=2, row=3, sticky=W)
        player_user_name_2.grid(column=2, row=4, sticky=W)
        player_user_name_3.grid(column=2, row=5, sticky=W)
        player_user_name_4.grid(column=2, row=6, sticky=W)
        player_user_name_5.grid(column=2, row=7, sticky=W)
        player_user_name_6.grid(column=2, row=8, sticky=W)
        player_user_name_7.grid(column=2, row=9, sticky=W)
        player_user_name_8.grid(column=2, row=10, sticky=W)
        player_user_name_9.grid(column=2, row=11, sticky=W)
        player_user_name_10.grid(column=2, row=12, sticky=W)

    elif top_10_radio.get() == 2: # Current player data for to 10
        search_rs3_player_html_current = []
        count = 0
        rs3_player_xp_screen = Toplevel() # Top 10 xp gained today after 10am to 9:59am the next day
        rs3_player_xp_screen.title('Top 10 xp gained in RuneScape 3 currently')
        runeclan_top_10_link = 'http://www.runeclan.com/xp-tracker'
        get_webite = urlopen(runeclan_top_10_link) # collect the website html document
        current_top_10_player = get_webite.read() # Read website
        placeholder_search_rs3_player_html_current = findall('[0-9,a-z,A-Z, ,\-,\_]+</a></td>', str(current_top_10_player)) # Find all the players name in the document
        for player in placeholder_search_rs3_player_html_current:
            search_rs3_player_html_current.append(placeholder_search_rs3_player_html_current[count].replace('</a></td>', '')) # Go throught the list of runescape players and removes '</a></td>'
            count = count + 1
        # 2nd Screen Widget ____________________________________________________________________
        postion_1 = Label(rs3_player_xp_screen, text="1:", font=font_times_15, justify="left")
        postion_2 = Label(rs3_player_xp_screen, text="2:", font=font_times_15, justify="left")
        postion_3 = Label(rs3_player_xp_screen, text="3:", font=font_times_15, justify="left")
        postion_4 = Label(rs3_player_xp_screen, text="4:", font=font_times_15, justify="left")
        postion_5 = Label(rs3_player_xp_screen, text="5:", font=font_times_15, justify="left")
        postion_6 = Label(rs3_player_xp_screen, text="6:", font=font_times_15, justify="left")
        postion_7 = Label(rs3_player_xp_screen, text="7:", font=font_times_15, justify="left")
        postion_8 = Label(rs3_player_xp_screen, text="8:", font=font_times_15, justify="left")
        postion_9 = Label(rs3_player_xp_screen, text="9:", font=font_times_15, justify="left")
        postion_10 = Label(rs3_player_xp_screen, text="10:", font=font_times_15, justify="left")

        player_user_name_1 = Label(rs3_player_xp_screen, text=search_rs3_player_html_current[0], font=font_times_15, justify="left")
        player_user_name_2 = Label(rs3_player_xp_screen, text=search_rs3_player_html_current[1], font=font_times_15, justify="left")
        player_user_name_3 = Label(rs3_player_xp_screen, text=search_rs3_player_html_current[2], font=font_times_15, justify="left")
        player_user_name_4 = Label(rs3_player_xp_screen, text=search_rs3_player_html_current[3], font=font_times_15, justify="left")
        player_user_name_5 = Label(rs3_player_xp_screen, text=search_rs3_player_html_current[4], font=font_times_15, justify="left")
        player_user_name_6 = Label(rs3_player_xp_screen, text=search_rs3_player_html_current[5], font=font_times_15, justify="left")
        player_user_name_7 = Label(rs3_player_xp_screen, text=search_rs3_player_html_current[6], font=font_times_15, justify="left")
        player_user_name_8 = Label(rs3_player_xp_screen, text=search_rs3_player_html_current[7], font=font_times_15, justify="left")
        player_user_name_9 = Label(rs3_player_xp_screen, text=search_rs3_player_html_current[8], font=font_times_15, justify="left")
        player_user_name_10 = Label(rs3_player_xp_screen, text=search_rs3_player_html_current[9], font=font_times_15, justify="left")
        top_player_image = Label(rs3_player_xp_screen, image=RS3_logo_image)
        #____________________________________________________________________
        # Layout for top 10 players of the day
        top_player_image.grid(column=0, row=0, columnspan=4, rowspan=2)
        postion_1.grid(column=1, row=3)
        postion_2.grid(column=1, row=4)
        postion_3.grid(column=1, row=5)
        postion_4.grid(column=1, row=6)
        postion_5.grid(column=1, row=7)
        postion_6.grid(column=1, row=8)
        postion_7.grid(column=1, row=9)
        postion_8.grid(column=1, row=10)
        postion_9.grid(column=1, row=11)
        postion_10.grid(column=1, row=12)

        player_user_name_1.grid(column=2, row=3, sticky=W)
        player_user_name_2.grid(column=2, row=4, sticky=W)
        player_user_name_3.grid(column=2, row=5, sticky=W)
        player_user_name_4.grid(column=2, row=6, sticky=W)
        player_user_name_5.grid(column=2, row=7, sticky=W)
        player_user_name_6.grid(column=2, row=8, sticky=W)
        player_user_name_7.grid(column=2, row=9, sticky=W)
        player_user_name_8.grid(column=2, row=10, sticky=W)
        player_user_name_9.grid(column=2, row=11, sticky=W)
        player_user_name_10.grid(column=2, row=12, sticky=W)
        #____________________________________________________________________

    elif top_10_radio.get() == 3: # Previous clan data
        search_rs3_clan_html_archive = []
        count = 0
        archive_rs3_clan_html = open('archive/clan.html').read() # Open and read file located in archive with the name of clan.html
        placeholder_search_rs3_clan_html_archive = findall('[0-9,a-z,A-Z, ,\-,\_]+</a><br /><i', archive_rs3_clan_html) # Find all the clan names in the document
        for clan in placeholder_search_rs3_clan_html_archive:
            search_rs3_clan_html_archive.append(placeholder_search_rs3_clan_html_archive[count].replace('</a><br /><i', '')) # Go throught the list of runescape players and removes '</a></td>'
            count = count + 1

        clan_ranking = Toplevel() # Top 10 clans clan for the day.
        clan_ranking.title('Top 10 Clan for the day')
        # 2nd Screen Widget ____________________________________________________________________
        postion_1 = Label(clan_ranking, text="1:", font=font_times_15, justify="left")
        postion_2 = Label(clan_ranking, text="2:", font=font_times_15, justify="left")
        postion_3 = Label(clan_ranking, text="3:", font=font_times_15, justify="left")
        postion_4 = Label(clan_ranking, text="4:", font=font_times_15, justify="left")
        postion_5 = Label(clan_ranking, text="5:", font=font_times_15, justify="left")
        postion_6 = Label(clan_ranking, text="6:", font=font_times_15, justify="left")
        postion_7 = Label(clan_ranking, text="7:", font=font_times_15, justify="left")
        postion_8 = Label(clan_ranking, text="8:", font=font_times_15, justify="left")
        postion_9 = Label(clan_ranking, text="9:", font=font_times_15, justify="left")
        postion_10 = Label(clan_ranking, text="10:", font=font_times_15, justify="left")

        clan_name_1 = Label(clan_ranking, text=search_rs3_clan_html_archive[0], font=font_times_15, justify="left")
        clan_name_2 = Label(clan_ranking, text=search_rs3_clan_html_archive[1], font=font_times_15, justify="left")
        clan_name_3 = Label(clan_ranking, text=search_rs3_clan_html_archive[2], font=font_times_15, justify="left")
        clan_name_4 = Label(clan_ranking, text=search_rs3_clan_html_archive[3], font=font_times_15, justify="left")
        clan_name_5 = Label(clan_ranking, text=search_rs3_clan_html_archive[4], font=font_times_15, justify="left")
        clan_name_6 = Label(clan_ranking, text=search_rs3_clan_html_archive[5], font=font_times_15, justify="left")
        clan_name_7 = Label(clan_ranking, text=search_rs3_clan_html_archive[6], font=font_times_15, justify="left")
        clan_name_8 = Label(clan_ranking, text=search_rs3_clan_html_archive[7], font=font_times_15, justify="left")
        clan_name_9 = Label(clan_ranking, text=search_rs3_clan_html_archive[8], font=font_times_15, justify="left")
        clan_name_10 = Label(clan_ranking, text=search_rs3_clan_html_archive[9], font=font_times_15, justify="left")
        clan_banner = Label(clan_ranking, image=Clan_banner_image)
        #____________________________________________________________________
        # Layout for top 10 players of the day
        clan_banner.grid(column=0, row=0, columnspan=4, rowspan=2)
        postion_1.grid(column=1, row=3)
        postion_2.grid(column=1, row=4)
        postion_3.grid(column=1, row=5)
        postion_4.grid(column=1, row=6)
        postion_5.grid(column=1, row=7)
        postion_6.grid(column=1, row=8)
        postion_7.grid(column=1, row=9)
        postion_8.grid(column=1, row=10)
        postion_9.grid(column=1, row=11)
        postion_10.grid(column=1, row=12)

        clan_name_1.grid(column=2, row=3, sticky=W)
        clan_name_2.grid(column=2, row=4, sticky=W)
        clan_name_3.grid(column=2, row=5, sticky=W)
        clan_name_4.grid(column=2, row=6, sticky=W)
        clan_name_5.grid(column=2, row=7, sticky=W)
        clan_name_6.grid(column=2, row=8, sticky=W)
        clan_name_7.grid(column=2, row=9, sticky=W)
        clan_name_8.grid(column=2, row=10, sticky=W)
        clan_name_9.grid(column=2, row=11, sticky=W)
        clan_name_10.grid(column=2, row=12, sticky=W)

    elif top_10_radio.get() == 4: # Current clan data
        search_rs3_clan_html_current = []
        count = 0
        runeclan_top_10_link = 'http://www.runeclan.com/hiscores'
        get_webite = urlopen(runeclan_top_10_link) # collect the website html document
        current_top_10_clan = get_webite.read() # Read website
        placeholder_search_rs3_clan_html_current = findall('[0-9,a-z,A-Z, ,\-,\_]+</a><br /><i', str(current_top_10_clan)) # Find all the players name in the document
        for clan in placeholder_search_rs3_clan_html_current:
            search_rs3_clan_html_current.append(placeholder_search_rs3_clan_html_current[count].replace('</a><br /><i', '')) # Go throught the list of runescape players and removes '</a></td>'
            count = count + 1
        clan_ranking = Toplevel() # Top 10 clans for the day.
        clan_ranking.title('Current Top 10 Clan for the day')
        # 2nd Screen Widget ____________________________________________________________________
        postion_1 = Label(clan_ranking, text="1:", font=font_times_15, justify="left")
        postion_2 = Label(clan_ranking, text="2:", font=font_times_15, justify="left")
        postion_3 = Label(clan_ranking, text="3:", font=font_times_15, justify="left")
        postion_4 = Label(clan_ranking, text="4:", font=font_times_15, justify="left")
        postion_5 = Label(clan_ranking, text="5:", font=font_times_15, justify="left")
        postion_6 = Label(clan_ranking, text="6:", font=font_times_15, justify="left")
        postion_7 = Label(clan_ranking, text="7:", font=font_times_15, justify="left")
        postion_8 = Label(clan_ranking, text="8:", font=font_times_15, justify="left")
        postion_9 = Label(clan_ranking, text="9:", font=font_times_15, justify="left")
        postion_10 = Label(clan_ranking, text="10:", font=font_times_15, justify="left")

        clan_name_1 = Label(clan_ranking, text=search_rs3_clan_html_current[0], font=font_times_15, justify="left")
        clan_name_2 = Label(clan_ranking, text=search_rs3_clan_html_current[1], font=font_times_15, justify="left")
        clan_name_3 = Label(clan_ranking, text=search_rs3_clan_html_current[2], font=font_times_15, justify="left")
        clan_name_4 = Label(clan_ranking, text=search_rs3_clan_html_current[3], font=font_times_15, justify="left")
        clan_name_5 = Label(clan_ranking, text=search_rs3_clan_html_current[4], font=font_times_15, justify="left")
        clan_name_6 = Label(clan_ranking, text=search_rs3_clan_html_current[5], font=font_times_15, justify="left")
        clan_name_7 = Label(clan_ranking, text=search_rs3_clan_html_current[6], font=font_times_15, justify="left")
        clan_name_8 = Label(clan_ranking, text=search_rs3_clan_html_current[7], font=font_times_15, justify="left")
        clan_name_9 = Label(clan_ranking, text=search_rs3_clan_html_current[8], font=font_times_15, justify="left")
        clan_name_10 = Label(clan_ranking, text=search_rs3_clan_html_current[9], font=font_times_15, justify="left")
        clan_banner = Label(clan_ranking, image=Clan_banner_image)
        #____________________________________________________________________
        # Layout for top 10 players of the day
        clan_banner.grid(column=0, row=0, columnspan=4, rowspan=2)
        postion_1.grid(column=1, row=3)
        postion_2.grid(column=1, row=4)
        postion_3.grid(column=1, row=5)
        postion_4.grid(column=1, row=6)
        postion_5.grid(column=1, row=7)
        postion_6.grid(column=1, row=8)
        postion_7.grid(column=1, row=9)
        postion_8.grid(column=1, row=10)
        postion_9.grid(column=1, row=11)
        postion_10.grid(column=1, row=12)

        clan_name_1.grid(column=2, row=3, sticky=W)
        clan_name_2.grid(column=2, row=4, sticky=W)
        clan_name_3.grid(column=2, row=5, sticky=W)
        clan_name_4.grid(column=2, row=6, sticky=W)
        clan_name_5.grid(column=2, row=7, sticky=W)
        clan_name_6.grid(column=2, row=8, sticky=W)
        clan_name_7.grid(column=2, row=9, sticky=W)
        clan_name_8.grid(column=2, row=10, sticky=W)
        clan_name_9.grid(column=2, row=11, sticky=W)
        clan_name_10.grid(column=2, row=12, sticky=W)

    elif top_10_radio.get() == 5: # Previous player data from old school RuneScape
        search_OSRS_player_html_archive = []
        count = 0
        archive_OSRS_player_html = open('archive/old_school_xp.html').read() # Open and read file located in archive with the name of old_school_xp.html
        placeholder_search_OSRS_player_html_archive = findall('[0-9,a-z,A-Z, ,\-,\_]+</a></td>', archive_OSRS_player_html) # Find all the players name in the document
        for player in placeholder_search_OSRS_player_html_archive:
            search_OSRS_player_html_archive.append(placeholder_search_OSRS_player_html_archive[count].replace('</a></td>', '')) # Go throught the list of runescape players and removes '</a></td>'
            count = count + 1
        oldschool_player_xp_screen = Toplevel() # Top 10 xp gained today after 10am to 9:59am the next day
        oldschool_player_xp_screen.title('Pervious Top 10 xp gained in Old School RuneScape')
        # 2nd Screen Widget ____________________________________________________________________
        postion_1 = Label(oldschool_player_xp_screen, text="1:", font=font_times_15, justify="left")
        postion_2 = Label(oldschool_player_xp_screen, text="2:", font=font_times_15, justify="left")
        postion_3 = Label(oldschool_player_xp_screen, text="3:", font=font_times_15, justify="left")
        postion_4 = Label(oldschool_player_xp_screen, text="4:", font=font_times_15, justify="left")
        postion_5 = Label(oldschool_player_xp_screen, text="5:", font=font_times_15, justify="left")
        postion_6 = Label(oldschool_player_xp_screen, text="6:", font=font_times_15, justify="left")
        postion_7 = Label(oldschool_player_xp_screen, text="7:", font=font_times_15, justify="left")
        postion_8 = Label(oldschool_player_xp_screen, text="8:", font=font_times_15, justify="left")
        postion_9 = Label(oldschool_player_xp_screen, text="9:", font=font_times_15, justify="left")
        postion_10 = Label(oldschool_player_xp_screen, text="10:", font=font_times_15, justify="left")

        player_user_name_1 = Label(oldschool_player_xp_screen, text=search_OSRS_player_html_archive[0], font=font_times_15, justify="left")
        player_user_name_2 = Label(oldschool_player_xp_screen, text=search_OSRS_player_html_archive[1], font=font_times_15, justify="left")
        player_user_name_3 = Label(oldschool_player_xp_screen, text=search_OSRS_player_html_archive[2], font=font_times_15, justify="left")
        player_user_name_4 = Label(oldschool_player_xp_screen, text=search_OSRS_player_html_archive[3], font=font_times_15, justify="left")
        player_user_name_5 = Label(oldschool_player_xp_screen, text=search_OSRS_player_html_archive[4], font=font_times_15, justify="left")
        player_user_name_6 = Label(oldschool_player_xp_screen, text=search_OSRS_player_html_archive[5], font=font_times_15, justify="left")
        player_user_name_7 = Label(oldschool_player_xp_screen, text=search_OSRS_player_html_archive[6], font=font_times_15, justify="left")
        player_user_name_8 = Label(oldschool_player_xp_screen, text=search_OSRS_player_html_archive[7], font=font_times_15, justify="left")
        player_user_name_9 = Label(oldschool_player_xp_screen, text=search_OSRS_player_html_archive[8], font=font_times_15, justify="left")
        player_user_name_10 = Label(oldschool_player_xp_screen, text=search_OSRS_player_html_archive[9], font=font_times_15, justify="left")
        OSRS_image = Label(oldschool_player_xp_screen, image=OSRS_logo_image)
        #____________________________________________________________________

        # Layout for top 10 players of the day
        OSRS_image.grid(column=0, row=0, columnspan=4, rowspan=2)
        postion_1.grid(column=1, row=3)
        postion_2.grid(column=1, row=4)
        postion_3.grid(column=1, row=5)
        postion_4.grid(column=1, row=6)
        postion_5.grid(column=1, row=7)
        postion_6.grid(column=1, row=8)
        postion_7.grid(column=1, row=9)
        postion_8.grid(column=1, row=10)
        postion_9.grid(column=1, row=11)
        postion_10.grid(column=1, row=12)

        player_user_name_1.grid(column=2, row=3, sticky=W)
        player_user_name_2.grid(column=2, row=4, sticky=W)
        player_user_name_3.grid(column=2, row=5, sticky=W)
        player_user_name_4.grid(column=2, row=6, sticky=W)
        player_user_name_5.grid(column=2, row=7, sticky=W)
        player_user_name_6.grid(column=2, row=8, sticky=W)
        player_user_name_7.grid(column=2, row=9, sticky=W)
        player_user_name_8.grid(column=2, row=10, sticky=W)
        player_user_name_9.grid(column=2, row=11, sticky=W)
        player_user_name_10.grid(column=2, row=12, sticky=W)

    elif top_10_radio.get() == 6: # Current player data from old school RuneScape
        search_OSRS_player_html_current = []
        count = 0
        runeclan_top_10_link = 'http://oldschool.runeclan.com/xp-tracker'
        get_webite = urlopen(runeclan_top_10_link) # collect the website html document
        current_top_10_player = get_webite.read() # Read website
        placeholder_search_OSRS_player_html_current = findall('[0-9,a-z,A-Z, ,\-,\_]+</a></td>', str(current_top_10_player)) # Find all the players name in the document
        for player in placeholder_search_OSRS_player_html_current:
            search_OSRS_player_html_current.append(placeholder_search_OSRS_player_html_current[count].replace('</a></td>', '')) # Go throught the list of runescape players and removes '</a></td>'
            count = count + 1
        oldschool_player_xp_screen = Toplevel() # Top 10 xp gained today after 10am to 9:59am the next day
        oldschool_player_xp_screen.title('Current Top 10 xp gained in Old School RuneScape')
        # 2nd Screen Widget ____________________________________________________________________
        postion_1 = Label(oldschool_player_xp_screen, text="1:", font=font_times_15, justify="left")
        postion_2 = Label(oldschool_player_xp_screen, text="2:", font=font_times_15, justify="left")
        postion_3 = Label(oldschool_player_xp_screen, text="3:", font=font_times_15, justify="left")
        postion_4 = Label(oldschool_player_xp_screen, text="4:", font=font_times_15, justify="left")
        postion_5 = Label(oldschool_player_xp_screen, text="5:", font=font_times_15, justify="left")
        postion_6 = Label(oldschool_player_xp_screen, text="6:", font=font_times_15, justify="left")
        postion_7 = Label(oldschool_player_xp_screen, text="7:", font=font_times_15, justify="left")
        postion_8 = Label(oldschool_player_xp_screen, text="8:", font=font_times_15, justify="left")
        postion_9 = Label(oldschool_player_xp_screen, text="9:", font=font_times_15, justify="left")
        postion_10 = Label(oldschool_player_xp_screen, text="10:", font=font_times_15, justify="left")

        player_user_name_1 = Label(oldschool_player_xp_screen, text=search_OSRS_player_html_current[0], font=font_times_15, justify="left")
        player_user_name_2 = Label(oldschool_player_xp_screen, text=search_OSRS_player_html_current[1], font=font_times_15, justify="left")
        player_user_name_3 = Label(oldschool_player_xp_screen, text=search_OSRS_player_html_current[2], font=font_times_15, justify="left")
        player_user_name_4 = Label(oldschool_player_xp_screen, text=search_OSRS_player_html_current[3], font=font_times_15, justify="left")
        player_user_name_5 = Label(oldschool_player_xp_screen, text=search_OSRS_player_html_current[4], font=font_times_15, justify="left")
        player_user_name_6 = Label(oldschool_player_xp_screen, text=search_OSRS_player_html_current[5], font=font_times_15, justify="left")
        player_user_name_7 = Label(oldschool_player_xp_screen, text=search_OSRS_player_html_current[6], font=font_times_15, justify="left")
        player_user_name_8 = Label(oldschool_player_xp_screen, text=search_OSRS_player_html_current[7], font=font_times_15, justify="left")
        player_user_name_9 = Label(oldschool_player_xp_screen, text=search_OSRS_player_html_current[8], font=font_times_15, justify="left")
        player_user_name_10 = Label(oldschool_player_xp_screen, text=search_OSRS_player_html_current[9], font=font_times_15, justify="left")
        OSRS_image = Label(oldschool_player_xp_screen, image=OSRS_logo_image)
        #____________________________________________________________________
        # Layout for top 10 players of the day
        OSRS_image.grid(column=0, row=0, columnspan=4, rowspan=2)
        postion_1.grid(column=1, row=3)
        postion_2.grid(column=1, row=4)
        postion_3.grid(column=1, row=5)
        postion_4.grid(column=1, row=6)
        postion_5.grid(column=1, row=7)
        postion_6.grid(column=1, row=8)
        postion_7.grid(column=1, row=9)
        postion_8.grid(column=1, row=10)
        postion_9.grid(column=1, row=11)
        postion_10.grid(column=1, row=12)

        player_user_name_1.grid(column=2, row=3, sticky=W)
        player_user_name_2.grid(column=2, row=4, sticky=W)
        player_user_name_3.grid(column=2, row=5, sticky=W)
        player_user_name_4.grid(column=2, row=6, sticky=W)
        player_user_name_5.grid(column=2, row=7, sticky=W)
        player_user_name_6.grid(column=2, row=8, sticky=W)
        player_user_name_7.grid(column=2, row=9, sticky=W)
        player_user_name_8.grid(column=2, row=10, sticky=W)
        player_user_name_9.grid(column=2, row=11, sticky=W)
        player_user_name_10.grid(column=2, row=12, sticky=W)

    else:
        alert("Preview was clicked. To preview a list please click on a button above.")

def export_list(): # Searchs for data from local files or from a website and calls another function to write to file with the data.
    if top_10_radio.get() == 1:
        results_for_top_10_username = []
        results_for_top_10_xp = []
        results_user_icon = []
        file_location = 'archive/player.html'
        read_html_file = open(file_location).read() # Open and read file located in archive with the name of player.html
        file_location = '../'+file_location # Add a ../ this cause the browser to go back 1 folder
        # Find all the players name in the document
        placeholder_results_for_top_10_username = findall('[0-9,a-z,A-Z, ,\-,\_]+</a></td>', read_html_file)
        # Find all the user icons in the html document
        placeholder_results_for_user_icon = findall('http://www.runeclan.com/images/chat_head.php\?a=[A-Z,a-z, ,\+,0-9]+', read_html_file)
        #  Find the xp related to the top 10 players who gained the most xp in the day
        placeholder_results_for_top_10_xp_relating_to_player = findall('>[0-9,]+<', read_html_file)
        # finds the day the webpage was gernerated.
        publication_date = findall('((Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) ([0-9]{1,2})(st|nd|rd|th) of (January|February|March|April|May|June|July|August|September|October|November|December) ([0-9]{4}))', read_html_file)
        publication_date = publication_date[0][0]

        count = 0 # This know as count++ in other languages. Count change while inside the loop
        # Loop throught all the list and remove certin characters
        for results in placeholder_results_for_top_10_username: # Loop goes for 50 times
            results_for_top_10_username.append(placeholder_results_for_top_10_username[count].replace('</a></td>', '')) # Go throught the list of runescape players and removes '</a></td>'
            results_user_icon.append('<img src="' + placeholder_results_for_user_icon[count] + '" alt="Runescaps players icons">') # Go throught the list and add img src and alt= text
            count = count + 1 # count++

        count = 0 # Reset count for the next loop
        # Loop throught all the list and remove certin characters
        for results in placeholder_results_for_top_10_xp_relating_to_player: # Loop goes for 318
            results_for_top_10_xp.append(placeholder_results_for_top_10_xp_relating_to_player[count].strip('<>')) # Go throught the list of runescape players and removes '<>'
            count = count + 1
        # Predefinded vaibale need to give the website some content
        HTML_title = "Previous Top 10 players list for xp gained"
        HTML_heading = "<h1>Top 10 players who have gained the most xp today </h1>"
        HTML_heading_image = '<img src="https://vignette.wikia.nocookie.net/runescape2/images/3/3d/RuneScape_3_Logo.png/revision/latest?cb=20140317195258" alt="RuneScape 3 logo from RuneWiki" style="margin-left: 37%;">'
        HTML_table_heading = """<table class="table  table-hover">
        <thead>
            <tr>
              <th>Ranking</th>
              <th>Player Icon</th>
              <th>Username</th>
              <th>Today's XP Gained</th>
            </tr>
        </thead>
        """
        postion_1_for_xp_gained = "<td>" + "1" + "</td>" + "<td>" + results_user_icon[0] +"</td>" + "<td>" + results_for_top_10_username[0] + "</td>" + "<td>" + results_for_top_10_xp[10] + "</td>"
        postion_2_for_xp_gained = "<td>" + "2" + "</td>" + "<td>" + results_user_icon[1] +"</td>" + "<td>" + results_for_top_10_username[1] + "</td>" + "<td>" + results_for_top_10_xp[16] + "</td>"
        postion_3_for_xp_gained = "<td>" + "3" + "</td>" + "<td>" + results_user_icon[2] +"</td>" + "<td>" + results_for_top_10_username[2] + "</td>" + "<td>" + results_for_top_10_xp[22] + "</td>"
        postion_4_for_xp_gained = "<td>" + "4" + "</td>" + "<td>" + results_user_icon[3] +"</td>" + "<td>" + results_for_top_10_username[3] + "</td>" + "<td>" + results_for_top_10_xp[28] + "</td>"
        postion_5_for_xp_gained = "<td>" + "5" + "</td>" + "<td>" + results_user_icon[4] +"</td>" + "<td>" + results_for_top_10_username[4] + "</td>" + "<td>" + results_for_top_10_xp[34] + "</td>"
        postion_6_for_xp_gained = "<td>" + "6" + "</td>" + "<td>" + results_user_icon[5] +"</td>" + "<td>" + results_for_top_10_username[5] + "</td>" + "<td>" + results_for_top_10_xp[40] + "</td>"
        postion_7_for_xp_gained = "<td>" + "7" + "</td>" + "<td>" + results_user_icon[6] +"</td>" + "<td>" + results_for_top_10_username[6] + "</td>" + "<td>" + results_for_top_10_xp[46] + "</td>"
        postion_8_for_xp_gained = "<td>" + "8" + "</td>" + "<td>" + results_user_icon[7] +"</td>" + "<td>" + results_for_top_10_username[7] + "</td>" + "<td>" + results_for_top_10_xp[52] + "</td>"
        postion_9_for_xp_gained = "<td>" + "9" + "</td>" + "<td>" + results_user_icon[8] +"</td>" + "<td>" + results_for_top_10_username[8] + "</td>" + "<td>" + results_for_top_10_xp[58] + "</td>"
        postion_10_for_xp_gained = "<td>" + "10" +  "</td>" + "<td>" + results_user_icon[9] + "</td>" + "<td>" + results_for_top_10_username[9] + "</td>" + "<td>" + results_for_top_10_xp[64] + "</td>"

        write_html_file(HTML_title, HTML_heading, HTML_heading_image, HTML_table_heading, postion_1_for_xp_gained, postion_2_for_xp_gained, postion_3_for_xp_gained, postion_4_for_xp_gained, postion_5_for_xp_gained, postion_6_for_xp_gained, postion_7_for_xp_gained, postion_8_for_xp_gained, postion_9_for_xp_gained, postion_10_for_xp_gained, publication_date, file_location)

    elif top_10_radio.get() == 2:
        results_for_top_10_username = []
        results_for_top_10_xp = []
        results_user_icon = []
        runeclan_top_10_link = 'http://www.runeclan.com/xp-tracker'
        get_webite = urlopen(runeclan_top_10_link) # collect the website html document
        read_html_file = get_webite.read() # Read data from runeclan.com/xp-tracker
        # Find all the players name in the document
        placeholder_results_for_top_10_username = findall('[0-9,a-z,A-Z, ,\-,\_]+</a></td>', str(read_html_file))
        # Find all the user icons in the html document
        placeholder_results_for_user_icon = findall('http://www.runeclan.com/images/chat_head.php\?a=[A-Z,a-z, ,\+,0-9]+', str(read_html_file))
        #  Find the xp related to the top 10 players who gained the most xp in the day
        placeholder_results_for_top_10_xp_relating_to_player = findall('>[0-9,]+<', str(read_html_file))
        # finds the day the webpage was gernerated.
        publication_date = findall('((Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) ([0-9]{1,2})(st|nd|rd|th) of (January|February|March|April|May|June|July|August|September|October|November|December) ([0-9]{4}))', str(read_html_file))
        publication_date = publication_date[0][0]

        count = 0 # This know as count++ in other languages. Count change while inside the loop
        # Loop throught all the list and remove certin characters
        for results in placeholder_results_for_top_10_username: # Loop goes for 50 times
            results_for_top_10_username.append(placeholder_results_for_top_10_username[count].replace('</a></td>', '')) # Go throught the list of runescape players and removes '</a></td>'
            results_user_icon.append('<img src="' + placeholder_results_for_user_icon[count] + '" alt="Runescaps players icons">') # Go throught the list and add img src and alt= text
            count = count + 1 # count++

        count = 0 # Reset count for the next loop
        # Loop throught all the list and remove certin characters
        for results in placeholder_results_for_top_10_xp_relating_to_player: # Loop goes for 318
            results_for_top_10_xp.append(placeholder_results_for_top_10_xp_relating_to_player[count].strip('<>')) # Go throught the list of runescape players and removes '<>'
            count = count + 1

        # Predefinded vaibale need to give the website some content
        HTML_title = "Current Top 10 players list for xp gained"
        HTML_heading = "<h1>Top 10 players who have gained the most xp today </h1>"
        HTML_heading_image = '<img src="https://vignette.wikia.nocookie.net/runescape2/images/3/3d/RuneScape_3_Logo.png/revision/latest?cb=20140317195258" alt="RuneScape 3 logo from RuneWiki" style="margin-left: 37%;">'
        HTML_table_heading = """<table class="table  table-hover">
        <thead>
            <tr>
              <th>Ranking</th>
              <th>Player Icon</th>
              <th>Username</th>
              <th>Today's XP Gained</th>
            </tr>
        </thead>
        """
        postion_1_for_xp_gained = "<td>" + "1" + "</td>" + "<td>" + results_user_icon[0] +"</td>" + "<td>" + results_for_top_10_username[0] + "</td>" + "<td>" + results_for_top_10_xp[10] + "</td>"
        postion_2_for_xp_gained = "<td>" + "2" + "</td>" + "<td>" + results_user_icon[1] +"</td>" + "<td>" + results_for_top_10_username[1] + "</td>" + "<td>" + results_for_top_10_xp[16] + "</td>"
        postion_3_for_xp_gained = "<td>" + "3" + "</td>" + "<td>" + results_user_icon[2] +"</td>" + "<td>" + results_for_top_10_username[2] + "</td>" + "<td>" + results_for_top_10_xp[22] + "</td>"
        postion_4_for_xp_gained = "<td>" + "4" + "</td>" + "<td>" + results_user_icon[3] +"</td>" + "<td>" + results_for_top_10_username[3] + "</td>" + "<td>" + results_for_top_10_xp[28] + "</td>"
        postion_5_for_xp_gained = "<td>" + "5" + "</td>" + "<td>" + results_user_icon[4] +"</td>" + "<td>" + results_for_top_10_username[4] + "</td>" + "<td>" + results_for_top_10_xp[34] + "</td>"
        postion_6_for_xp_gained = "<td>" + "6" + "</td>" + "<td>" + results_user_icon[5] +"</td>" + "<td>" + results_for_top_10_username[5] + "</td>" + "<td>" + results_for_top_10_xp[40] + "</td>"
        postion_7_for_xp_gained = "<td>" + "7" + "</td>" + "<td>" + results_user_icon[6] +"</td>" + "<td>" + results_for_top_10_username[6] + "</td>" + "<td>" + results_for_top_10_xp[46] + "</td>"
        postion_8_for_xp_gained = "<td>" + "8" + "</td>" + "<td>" + results_user_icon[7] +"</td>" + "<td>" + results_for_top_10_username[7] + "</td>" + "<td>" + results_for_top_10_xp[52] + "</td>"
        postion_9_for_xp_gained = "<td>" + "9" + "</td>" + "<td>" + results_user_icon[8] +"</td>" + "<td>" + results_for_top_10_username[8] + "</td>" + "<td>" + results_for_top_10_xp[58] + "</td>"
        postion_10_for_xp_gained = "<td>" + "10" +  "</td>" + "<td>" + results_user_icon[9] + "</td>" + "<td>" + results_for_top_10_username[9] + "</td>" + "<td>" + results_for_top_10_xp[64] + "</td>"

        write_html_file(HTML_title, HTML_heading, HTML_heading_image, HTML_table_heading, postion_1_for_xp_gained, postion_2_for_xp_gained, postion_3_for_xp_gained, postion_4_for_xp_gained, postion_5_for_xp_gained, postion_6_for_xp_gained, postion_7_for_xp_gained, postion_8_for_xp_gained, postion_9_for_xp_gained, postion_10_for_xp_gained, publication_date, runeclan_top_10_link)

    elif top_10_radio.get() == 3:
        results_for_top_10_clan = []
        results_for_top_10_xp = []
        results_clan_icon = []
        file_location = 'archive/clan.html'
        read_html_file = open(file_location).read() # Read data from archive/clan.html
        file_location = '../'+file_location # Add a ../ this cause the browser to go back 1 folder
        # Find all the players name in the document
        placeholder_results_for_top_10_clan = findall('[0-9,a-z,A-Z, ,\-,\_]+</a><br /><i', str(read_html_file))
        # Find all the user icons in the html document
        placeholder_results_for_clan_icon = findall('http://www\.runeclan\.com/images//clan_banner\.php\?a=[A-Z,a-z, ,\+,0-9]+', str(read_html_file))
        #  Find the xp related to the top 10 players who gained the most xp in the day
        placeholder_results_for_top_10_xp_relating_to_clan = findall('>[0-9,]+<', str(read_html_file))
        # finds the day the webpage was gernerated.
        publication_date = findall('((Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) ([0-9]{1,2})(st|nd|rd|th) of (January|February|March|April|May|June|July|August|September|October|November|December) ([0-9]{4}))', str(read_html_file))
        publication_date = publication_date[0][0]

        count = 0 # This know as count++ in other languages. Count change while inside the loop
        # Loop throught all the list and remove certin characters
        for results in placeholder_results_for_top_10_clan: # Loop goes for 50 times
            results_for_top_10_clan.append(placeholder_results_for_top_10_clan[count].replace('</a></td>', '')) # Go throught the list of runescape players and removes '</a></td>'
            results_clan_icon.append('<img src="' + placeholder_results_for_clan_icon[count] + '" alt="Runescaps players icons">') # Go throught the list and add img src and alt= text
            count = count + 1 # count++

        count = 0 # Reset count for the next loop
        # Loop throught all the list and remove certin characters
        for results in placeholder_results_for_top_10_xp_relating_to_clan: # Loop goes for 318
            results_for_top_10_xp.append(placeholder_results_for_top_10_xp_relating_to_clan[count].strip('<>')) # Go throught the list of runescape players and removes '<>'
            count = count + 1

        # Predefinded vaibale need to give the website some content
        HTML_title = "Previous Top 10 clan"
        HTML_heading = "<h1>Previously top 10 clans based on how much xp the clan has gathered in a day.</h1>"
        HTML_heading_image = '<img src="http://www.runeclan.com/images/clan_banner.php?a=blank+banner" alt="Runescape 3 clan banner" style="margin-left: 37%;">'
        HTML_table_heading = """<table class="table  table-hover">
        <thead>
            <tr>
            <th>Ranking</th>
            <th>Clan Banner</th>
            <th>Clan Name</th>
            <th>Today's XP Gained</th>
            </tr>
        </thead>
        """
        postion_1_for_xp_gained = "<td>" + "1" + "</td>" + "<td>" + results_clan_icon[0] +"</td>" + "<td>" + results_for_top_10_clan[0] + "</td>" + "<td>" + results_for_top_10_xp[10] + "</td>"
        postion_2_for_xp_gained = "<td>" + "2" + "</td>" + "<td>" + results_clan_icon[1] +"</td>" + "<td>" + results_for_top_10_clan[1] + "</td>" + "<td>" + results_for_top_10_xp[16] + "</td>"
        postion_3_for_xp_gained = "<td>" + "3" + "</td>" + "<td>" + results_clan_icon[2] +"</td>" + "<td>" + results_for_top_10_clan[2] + "</td>" + "<td>" + results_for_top_10_xp[22] + "</td>"
        postion_4_for_xp_gained = "<td>" + "4" + "</td>" + "<td>" + results_clan_icon[3] +"</td>" + "<td>" + results_for_top_10_clan[3] + "</td>" + "<td>" + results_for_top_10_xp[28] + "</td>"
        postion_5_for_xp_gained = "<td>" + "5" + "</td>" + "<td>" + results_clan_icon[4] +"</td>" + "<td>" + results_for_top_10_clan[4] + "</td>" + "<td>" + results_for_top_10_xp[34] + "</td>"
        postion_6_for_xp_gained = "<td>" + "6" + "</td>" + "<td>" + results_clan_icon[5] +"</td>" + "<td>" + results_for_top_10_clan[5] + "</td>" + "<td>" + results_for_top_10_xp[40] + "</td>"
        postion_7_for_xp_gained = "<td>" + "7" + "</td>" + "<td>" + results_clan_icon[6] +"</td>" + "<td>" + results_for_top_10_clan[6] + "</td>" + "<td>" + results_for_top_10_xp[46] + "</td>"
        postion_8_for_xp_gained = "<td>" + "8" + "</td>" + "<td>" + results_clan_icon[7] +"</td>" + "<td>" + results_for_top_10_clan[7] + "</td>" + "<td>" + results_for_top_10_xp[52] + "</td>"
        postion_9_for_xp_gained = "<td>" + "9" + "</td>" + "<td>" + results_clan_icon[8] +"</td>" + "<td>" + results_for_top_10_clan[8] + "</td>" + "<td>" + results_for_top_10_xp[58] + "</td>"
        postion_10_for_xp_gained = "<td>" + "10" +  "</td>" + "<td>" + results_clan_icon[9] + "</td>" + "<td>" + results_for_top_10_clan[9] + "</td>" + "<td>" + results_for_top_10_xp[64] + "</td>"

        write_html_file(HTML_title, HTML_heading, HTML_heading_image, HTML_table_heading, postion_1_for_xp_gained, postion_2_for_xp_gained, postion_3_for_xp_gained, postion_4_for_xp_gained, postion_5_for_xp_gained, postion_6_for_xp_gained, postion_7_for_xp_gained, postion_8_for_xp_gained, postion_9_for_xp_gained, postion_10_for_xp_gained, publication_date, file_location)

    elif top_10_radio.get() == 4:
        results_for_top_10_clan = []
        results_for_top_10_xp = []
        results_clan_icon = []
        runeclan_top_10_link = 'http://www.runeclan.com/hiscores'
        get_webite = urlopen(runeclan_top_10_link) # collect the website html document
        read_html_file = get_webite.read() # Read data from runeclan.com/xp-tracker
        # Find all the players name in the document
        placeholder_results_for_top_10_clan = findall('[0-9,a-z,A-Z, ,\-,\_]+</a><br /><i', str(read_html_file))
        # Find all the user icons in the html document
        placeholder_results_for_clan_icon = findall('http://www\.runeclan\.com/images//clan_banner\.php\?a=[A-Z,a-z, ,\+,0-9]+', str(read_html_file))
        #  Find the xp related to the top 10 players who gained the most xp in the day
        placeholder_results_for_top_10_xp_relating_to_clan = findall('>[0-9,]+<', str(read_html_file))
        # finds the day the webpage was gernerated.
        publication_date = findall('((Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) ([0-9]{1,2})(st|nd|rd|th) of (January|February|March|April|May|June|July|August|September|October|November|December) ([0-9]{4}))', str(read_html_file))
        publication_date = publication_date[0][0]

        count = 0 # This know as count++ in other languages. Count change while inside the loop
        # Loop throught all the list and remove certin characters
        for results in placeholder_results_for_top_10_clan: # Loop goes for 50 times
            results_for_top_10_clan.append(placeholder_results_for_top_10_clan[count].replace('</a></td>', '')) # Go throught the list of runescape players and removes '</a></td>'
            results_clan_icon.append('<img src="' + placeholder_results_for_clan_icon[count] + '" alt="Runescaps players icons">') # Go throught the list and add img src and alt= text
            count = count + 1 # count++

        count = 0 # Reset count for the next loop
        # Loop throught all the list and remove certin characters
        for results in placeholder_results_for_top_10_xp_relating_to_clan: # Loop goes for 318
            results_for_top_10_xp.append(placeholder_results_for_top_10_xp_relating_to_clan[count].strip('<>')) # Go throught the list of runescape players and removes '<>'
            count = count + 1

        # Predefinded vaibale need to give the website some content
        HTML_title = "Current Top 10 clan"
        HTML_heading = "<h1>Current Top 10 clans based on how much xp the clan has gathered today.</h1>"
        HTML_heading_image = '<img src="http://www.runeclan.com/images/clan_banner.php?a=blank+banner" alt="Runescape 3 clan banner" style="margin-left: 37%;">'
        HTML_table_heading = """<table class="table  table-hover">
        <thead>
            <tr>
              <th>Ranking</th>
              <th>Clan Banner</th>
              <th>Clan Name</th>
              <th>Today's XP Gained</th>
            </tr>
        </thead>
        """
        # The following turn out to be
        # <td> 1 </td> <td> <img src="http://www.runeclan.com/images/clan_banner.php?a=blank+banner"> </td> <td> clan name </td> <td> 9,999,999,999 </td>
        postion_1_for_xp_gained = "<td>" + "1" + "</td>" + "<td>" + results_clan_icon[0] +"</td>" + "<td>" + results_for_top_10_clan[0] + "</td>" + "<td>" + results_for_top_10_xp[10] + "</td>"
        postion_2_for_xp_gained = "<td>" + "2" + "</td>" + "<td>" + results_clan_icon[1] +"</td>" + "<td>" + results_for_top_10_clan[1] + "</td>" + "<td>" + results_for_top_10_xp[16] + "</td>"
        postion_3_for_xp_gained = "<td>" + "3" + "</td>" + "<td>" + results_clan_icon[2] +"</td>" + "<td>" + results_for_top_10_clan[2] + "</td>" + "<td>" + results_for_top_10_xp[22] + "</td>"
        postion_4_for_xp_gained = "<td>" + "4" + "</td>" + "<td>" + results_clan_icon[3] +"</td>" + "<td>" + results_for_top_10_clan[3] + "</td>" + "<td>" + results_for_top_10_xp[28] + "</td>"
        postion_5_for_xp_gained = "<td>" + "5" + "</td>" + "<td>" + results_clan_icon[4] +"</td>" + "<td>" + results_for_top_10_clan[4] + "</td>" + "<td>" + results_for_top_10_xp[34] + "</td>"
        postion_6_for_xp_gained = "<td>" + "6" + "</td>" + "<td>" + results_clan_icon[5] +"</td>" + "<td>" + results_for_top_10_clan[5] + "</td>" + "<td>" + results_for_top_10_xp[40] + "</td>"
        postion_7_for_xp_gained = "<td>" + "7" + "</td>" + "<td>" + results_clan_icon[6] +"</td>" + "<td>" + results_for_top_10_clan[6] + "</td>" + "<td>" + results_for_top_10_xp[46] + "</td>"
        postion_8_for_xp_gained = "<td>" + "8" + "</td>" + "<td>" + results_clan_icon[7] +"</td>" + "<td>" + results_for_top_10_clan[7] + "</td>" + "<td>" + results_for_top_10_xp[52] + "</td>"
        postion_9_for_xp_gained = "<td>" + "9" + "</td>" + "<td>" + results_clan_icon[8] +"</td>" + "<td>" + results_for_top_10_clan[8] + "</td>" + "<td>" + results_for_top_10_xp[58] + "</td>"
        postion_10_for_xp_gained = "<td>" + "10" +  "</td>" + "<td>" + results_clan_icon[9] + "</td>" + "<td>" + results_for_top_10_clan[9] + "</td>" + "<td>" + results_for_top_10_xp[64] + "</td>"

        write_html_file(HTML_title, HTML_heading, HTML_heading_image, HTML_table_heading, postion_1_for_xp_gained, postion_2_for_xp_gained, postion_3_for_xp_gained, postion_4_for_xp_gained, postion_5_for_xp_gained, postion_6_for_xp_gained, postion_7_for_xp_gained, postion_8_for_xp_gained, postion_9_for_xp_gained, postion_10_for_xp_gained, publication_date, runeclan_top_10_link)

    elif top_10_radio.get() == 5:
        results_for_top_10_username = []
        results_for_top_10_xp = []
        results_user_icon = []
        file_location = 'archive/old_school_xp.html'
        read_html_file = open(file_location).read() # Open and read file located in archive with the name of old_school_xp.html
        file_location = '../'+file_location # Add a ../ this cause the browser to go back 1 folder
        # Find all the players name in the document
        placeholder_results_for_top_10_username = findall('[0-9,a-z,A-Z, ,\-,\_]+</a></td>', str(read_html_file))
        # Find all the user icons in the html document
        placeholder_results_for_user_icon = findall('http://www\.runeclan\.com/images/chat_head_os\.php\?a=[A-Z,a-z, ,\+,0-9]+', str(read_html_file))
        #  Find the xp related to the top 10 players who gained the most xp in the day
        placeholder_results_for_top_10_xp_relating_to_player = findall('>[0-9,]+</td>', str(read_html_file))
        # finds the day the webpage was gernerated.
        publication_date = findall('((Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) ([0-9]{1,2})(st|nd|rd|th) of (January|February|March|April|May|June|July|August|September|October|November|December) ([0-9]{4}))', str(read_html_file))
        publication_date = publication_date[0][0]

        count = 0 # This know as count++ in other languages. Count change while inside the loop
        # Loop throught all the list and remove certin characters
        for results in placeholder_results_for_top_10_username: # Loop goes for 50 times
            results_for_top_10_username.append(placeholder_results_for_top_10_username[count].replace('</a></td>', '')) # Go throught the list of runescape players and removes '</a></td>'
            results_user_icon.append('<img src="' + placeholder_results_for_user_icon[count] + '" alt="Runescaps players icons">') # Go throught the list and add img src and alt= text
            count = count + 1 # count++

        count = 0 # Reset count for the next loop
        # Loop throught all the list and remove certin characters
        for results in placeholder_results_for_top_10_xp_relating_to_player: # Loop goes for 318
            results_for_top_10_xp.append(placeholder_results_for_top_10_xp_relating_to_player[count].strip('<>/td')) # Go throught the list of runescape players and removes '<>/td'
            count = count + 1
        # Predefinded vaibale need to give the website some content
        HTML_title = "Current Top 10 old school players list for xp gained"
        HTML_heading = "<h1>Current  Top 10 old school player based on how much xp the player has gathered on the today</h1>"
        HTML_heading_image = '<img src="https://upload.wikimedia.org/wikipedia/en/a/a7/Old_School_Runescape_Logo.png" alt="Old school Runscape photo" style="margin-left: 37%;">'
        HTML_table_heading = """<table class="table  table-hover">
        <thead>
            <tr>
              <th>Ranking</th>
              <th>Player Icon</th>
              <th>Username</th>
              <th>Today's XP Gained</th>
            </tr>
        </thead>
        """
        postion_1_for_xp_gained = "<td>" + "1" + "</td>" + "<td>" + results_user_icon[0] +"</td>" + "<td>" + results_for_top_10_username[0] + "</td>" + "<td>" + results_for_top_10_xp[1] + "</td>"
        postion_2_for_xp_gained = "<td>" + "2" + "</td>" + "<td>" + results_user_icon[1] +"</td>" + "<td>" + results_for_top_10_username[1] + "</td>" + "<td>" + results_for_top_10_xp[7] + "</td>"
        postion_3_for_xp_gained = "<td>" + "3" + "</td>" + "<td>" + results_user_icon[2] +"</td>" + "<td>" + results_for_top_10_username[2] + "</td>" + "<td>" + results_for_top_10_xp[13] + "</td>"
        postion_4_for_xp_gained = "<td>" + "4" + "</td>" + "<td>" + results_user_icon[3] +"</td>" + "<td>" + results_for_top_10_username[3] + "</td>" + "<td>" + results_for_top_10_xp[19] + "</td>"
        postion_5_for_xp_gained = "<td>" + "5" + "</td>" + "<td>" + results_user_icon[4] +"</td>" + "<td>" + results_for_top_10_username[4] + "</td>" + "<td>" + results_for_top_10_xp[25] + "</td>"
        postion_6_for_xp_gained = "<td>" + "6" + "</td>" + "<td>" + results_user_icon[5] +"</td>" + "<td>" + results_for_top_10_username[5] + "</td>" + "<td>" + results_for_top_10_xp[31] + "</td>"
        postion_7_for_xp_gained = "<td>" + "7" + "</td>" + "<td>" + results_user_icon[6] +"</td>" + "<td>" + results_for_top_10_username[6] + "</td>" + "<td>" + results_for_top_10_xp[37] + "</td>"
        postion_8_for_xp_gained = "<td>" + "8" + "</td>" + "<td>" + results_user_icon[7] +"</td>" + "<td>" + results_for_top_10_username[7] + "</td>" + "<td>" + results_for_top_10_xp[43] + "</td>"
        postion_9_for_xp_gained = "<td>" + "9" + "</td>" + "<td>" + results_user_icon[8] +"</td>" + "<td>" + results_for_top_10_username[8] + "</td>" + "<td>" + results_for_top_10_xp[49] + "</td>"
        postion_10_for_xp_gained = "<td>" + "10" +  "</td>" + "<td>" + results_user_icon[9] + "</td>" + "<td>" + results_for_top_10_username[9] + "</td>" + "<td>" + results_for_top_10_xp[55] + "</td>"

        write_html_file(HTML_title, HTML_heading, HTML_heading_image, HTML_table_heading, postion_1_for_xp_gained, postion_2_for_xp_gained, postion_3_for_xp_gained, postion_4_for_xp_gained, postion_5_for_xp_gained, postion_6_for_xp_gained, postion_7_for_xp_gained, postion_8_for_xp_gained, postion_9_for_xp_gained, postion_10_for_xp_gained, publication_date, file_location)

    elif top_10_radio.get() == 6:
        results_for_top_10_username = []
        results_for_top_10_xp = []
        results_user_icon = []
        runeclan_top_10_link = 'http://oldschool.runeclan.com/xp-tracker'
        get_webite = urlopen(runeclan_top_10_link) # collect the website html document
        read_html_file = get_webite.read() # Read data from runeclan.com/xp-tracker
        # Find all the players name in the document
        placeholder_results_for_top_10_username = findall('[0-9,a-z,A-Z, ,\-,\_]+</a></td>', str(read_html_file))
        # Find all the user icons in the html document
        placeholder_results_for_user_icon = findall('http://www\.runeclan\.com/images/chat_head_os\.php\?a=[A-Z,a-z, ,\+,0-9]+', str(read_html_file))
        #  Find the xp related to the top 10 players who gained the most xp in the day
        placeholder_results_for_top_10_xp_relating_to_player = findall('>[0-9,]+</td>', str(read_html_file))
        # finds the day the webpage was gernerated.
        publication_date = findall('((Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) ([0-9]{1,2})(st|nd|rd|th) of (January|February|March|April|May|June|July|August|September|October|November|December) ([0-9]{4}))', str(read_html_file))
        publication_date = publication_date[0][0]

        count = 0 # This know as count++ in other languages. Count change while inside the loop
        # Loop throught all the list and remove certin characters
        for results in placeholder_results_for_top_10_username: # Loop goes for 50 times
            results_for_top_10_username.append(placeholder_results_for_top_10_username[count].replace('</a></td>', '')) # Go throught the list of runescape players and removes '</a></td>'
            results_user_icon.append('<img src="' + placeholder_results_for_user_icon[count] + '" alt="Runescaps players icons">') # Go throught the list and add img src and alt= text
            count = count + 1 # count++

        count = 0 # Reset count for the next loop
        # Loop throught all the list and remove certin characters
        for results in placeholder_results_for_top_10_xp_relating_to_player: # Loop goes for 318
            results_for_top_10_xp.append(placeholder_results_for_top_10_xp_relating_to_player[count].strip('<>/td')) # Go throught the list of runescape players and removes '<>/td'
            count = count + 1
        # Predefinded vaibale need to give the website some content
        HTML_title = "Current Top 10 old school players list for xp gained"
        HTML_heading = "<h1>Current  Top 10 old school player based on how much xp the player has gathered on the today</h1>"
        HTML_heading_image = '<img src="https://upload.wikimedia.org/wikipedia/en/a/a7/Old_School_Runescape_Logo.png" alt="Old school Runscape photo" style="margin-left: 37%;">'
        HTML_table_heading = """<table class="table  table-hover">
        <thead>
            <tr>
              <th>Ranking</th>
              <th>Player Icon</th>
              <th>Username</th>
              <th>Today's XP Gained</th>
            </tr>
        </thead>
        """
        postion_1_for_xp_gained = "<td>" + "1" + "</td>" + "<td>" + results_user_icon[0] +"</td>" + "<td>" + results_for_top_10_username[0] + "</td>" + "<td>" + results_for_top_10_xp[1] + "</td>"
        postion_2_for_xp_gained = "<td>" + "2" + "</td>" + "<td>" + results_user_icon[1] +"</td>" + "<td>" + results_for_top_10_username[1] + "</td>" + "<td>" + results_for_top_10_xp[7] + "</td>"
        postion_3_for_xp_gained = "<td>" + "3" + "</td>" + "<td>" + results_user_icon[2] +"</td>" + "<td>" + results_for_top_10_username[2] + "</td>" + "<td>" + results_for_top_10_xp[13] + "</td>"
        postion_4_for_xp_gained = "<td>" + "4" + "</td>" + "<td>" + results_user_icon[3] +"</td>" + "<td>" + results_for_top_10_username[3] + "</td>" + "<td>" + results_for_top_10_xp[19] + "</td>"
        postion_5_for_xp_gained = "<td>" + "5" + "</td>" + "<td>" + results_user_icon[4] +"</td>" + "<td>" + results_for_top_10_username[4] + "</td>" + "<td>" + results_for_top_10_xp[25] + "</td>"
        postion_6_for_xp_gained = "<td>" + "6" + "</td>" + "<td>" + results_user_icon[5] +"</td>" + "<td>" + results_for_top_10_username[5] + "</td>" + "<td>" + results_for_top_10_xp[31] + "</td>"
        postion_7_for_xp_gained = "<td>" + "7" + "</td>" + "<td>" + results_user_icon[6] +"</td>" + "<td>" + results_for_top_10_username[6] + "</td>" + "<td>" + results_for_top_10_xp[37] + "</td>"
        postion_8_for_xp_gained = "<td>" + "8" + "</td>" + "<td>" + results_user_icon[7] +"</td>" + "<td>" + results_for_top_10_username[7] + "</td>" + "<td>" + results_for_top_10_xp[43] + "</td>"
        postion_9_for_xp_gained = "<td>" + "9" + "</td>" + "<td>" + results_user_icon[8] +"</td>" + "<td>" + results_for_top_10_username[8] + "</td>" + "<td>" + results_for_top_10_xp[49] + "</td>"
        postion_10_for_xp_gained = "<td>" + "10" +  "</td>" + "<td>" + results_user_icon[9] + "</td>" + "<td>" + results_for_top_10_username[9] + "</td>" + "<td>" + results_for_top_10_xp[55] + "</td>"

        write_html_file(HTML_title, HTML_heading, HTML_heading_image, HTML_table_heading, postion_1_for_xp_gained, postion_2_for_xp_gained, postion_3_for_xp_gained, postion_4_for_xp_gained, postion_5_for_xp_gained, postion_6_for_xp_gained, postion_7_for_xp_gained, postion_8_for_xp_gained, postion_9_for_xp_gained, postion_10_for_xp_gained, publication_date,  runeclan_top_10_link)

    else:
        alert("Export was clicked. To export a list please click on a button above.")

def write_html_file(title, heading_1, image, table_heading, postion_1, postion_2, postion_3, postion_4, postion_5,postion_6, postion_7, postion_8, postion_9, postion_10, publication_date, location_of_info): # Gets data from export_list() and gernerated a website.
    HTML_head_part_a = """<!DOCTYPE html>
    <html lang="en">
      <head>
          <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
          <meta charset="utf-8">
          <title>"""
    HTML_head_part_b = """</title>
      </head>
      <style media="screen">
        .column {
          float: left;
        }
      </style>
      <body>
    """
    start_of_table_row = "<tr>"
    end_of_table_row = '</tr>'
    HTML_end= """

    <body>
    </html>
    """
    create_html_file = open("archive/export.html", "w")
    create_html_file.write(HTML_head_part_a)
    create_html_file.write(title)
    create_html_file.write(HTML_head_part_b)
    create_html_file.write(heading_1)
    create_html_file.write(image)
    create_html_file.write(table_heading) # Write the heading table
    create_html_file.write('<tbody>') # body of the table
    # start of the row 1 of 10
    create_html_file.write(start_of_table_row)
    create_html_file.write(postion_1)
    create_html_file.write(end_of_table_row)
    # start of the row 2 of 10
    create_html_file.write(start_of_table_row)
    create_html_file.write(postion_2)
    create_html_file.write(end_of_table_row)
    # start of the row 3 of 10
    create_html_file.write(start_of_table_row)
    create_html_file.write(postion_3)
    create_html_file.write(end_of_table_row)
    # start of the row 4 of 10
    create_html_file.write(start_of_table_row)
    create_html_file.write(postion_4)
    create_html_file.write(end_of_table_row)
    # start of the row 5  of 10
    create_html_file.write(start_of_table_row)
    create_html_file.write(postion_5)
    create_html_file.write(end_of_table_row)
    # start of the row 6
    create_html_file.write(start_of_table_row)
    create_html_file.write(postion_6)
    create_html_file.write(end_of_table_row)
    # start of the row 7 of 10
    create_html_file.write(start_of_table_row)
    create_html_file.write(postion_7)
    create_html_file.write(end_of_table_row)
    # start of the row 8 of 10
    create_html_file.write(start_of_table_row)
    create_html_file.write(postion_8)
    create_html_file.write(end_of_table_row)
    # start of the row 9 of 10
    create_html_file.write(start_of_table_row)
    create_html_file.write(postion_9)
    create_html_file.write(end_of_table_row)
    # start of the row 10 of 10
    create_html_file.write(start_of_table_row)
    create_html_file.write(postion_10)
    create_html_file.write(end_of_table_row)
    create_html_file.write('</tbody>') # End tag of the table body.
    create_html_file.write("</table>") # End tag of the table
    # End of the table
    create_html_file.write('<p>Date of publication: ' +     publication_date+'</p>') # Write the publication date of the webpage to the html docment
    create_html_file.write('<a href="' + location_of_info + '"> Location from '+location_of_info + '</a>') # Write the where the data came from
    create_html_file.write(HTML_end)

# Date it was published, Ranking Postion, Username, Xp gained
def insert_into_db(): # Insert data from the website into the database publication_date, ranking_postion, item, main_attribute
    if top_10_radio.get() == 1: # Previous player data
        conn = connect(database=database_location)
        top_ten_db = conn.cursor()
        username = []
        xp = []
        read_html_file = open('archive/player.html').read() # Open and read file located in archive with the name of player.html
        count = 0
        placeholder_username = findall('[0-9,a-z,A-Z, ,\-,\_]+</a></td>', str(read_html_file))
        placeholder_xp = findall('>[0-9,]+<', str(read_html_file))
        # finds the day the webpage was gernerated.
        publication_date = findall('((Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) ([0-9]{1,2})(st|nd|rd|th) of (January|February|March|April|May|June|July|August|September|October|November|December) ([0-9]{4}))', str(read_html_file))
        publication_date = publication_date[0][0]

        count = 0 # This know as count++ in other languages. Count change while inside the loop
        # Loop throught all the list and remove certin characters
        for results in placeholder_username: # Loop goes for 50 times
            username.append(placeholder_username[count].replace('</a></td>', '')) # Go throught the list of runescape players and removes '</a></td>'
            count = count + 1 # count++

        count = 0 # Reset count for the next loop
        # Loop throught all the list and remove certin characters
        for results in placeholder_xp: # Loop goes for 318
            xp.append(placeholder_xp[count].strip('<>')) # Go throught the list of runescape players and removes '<>'
            count = count + 1

            #publication_date, ranking, username, xp
        sql = """INSERT INTO top_ten VALUES
        ('"""+publication_date+"""',1,'"""+username[0]+"""', '"""+xp[10]+"""'),
        ('"""+publication_date+"""',2,'"""+username[1]+"""', '"""+xp[16]+"""'),
        ('"""+publication_date+"""',3,'"""+username[2]+"""', '"""+xp[22]+"""'),
        ('"""+publication_date+"""',4,'"""+username[3]+"""', '"""+xp[28]+"""'),
        ('"""+publication_date+"""',4,'"""+username[4]+"""', '"""+xp[34]+"""'),
        ('"""+publication_date+"""',6,'"""+username[5]+"""', '"""+xp[40]+"""'),
        ('"""+publication_date+"""',5,'"""+username[6]+"""', '"""+xp[46]+"""'),
        ('"""+publication_date+"""',8,'"""+username[7]+"""', '"""+xp[52]+"""'),
        ('"""+publication_date+"""',6,'"""+username[8]+"""', '"""+xp[58]+"""'),
        ('"""+publication_date+"""',10,'"""+username[9]+"""', '"""+xp[64]+"""')"""
        # Close the cursor and release the server connection.
        top_ten_db.execute(sql)
        conn.commit()
        top_ten_db.close()
        conn.close()

    elif top_10_radio.get() == 2: # Current player data for to 10
        conn = connect(database=database_location)
        top_ten_db = conn.cursor()
        username = []
        xp = []
        runeclan_top_10_link = 'http://www.runeclan.com/xp-tracker'
        get_webite = urlopen(runeclan_top_10_link) # collect the website html document
        read_html_file = get_webite.read() # Read data from runeclan.com/xp-tracker
        # Find all the players name in the document
        count = 0
        placeholder_username = findall('[0-9,a-z,A-Z, ,\-,\_]+</a></td>', str(read_html_file))
        placeholder_xp = findall('>[0-9,]+<', str(read_html_file))
        # finds the day the webpage was gernerated.
        publication_date = findall('((Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) ([0-9]{1,2})(st|nd|rd|th) of (January|February|March|April|May|June|July|August|September|October|November|December) ([0-9]{4}))', str(read_html_file))
        publication_date = publication_date[0][0]

        count = 0 # This know as count++ in other languages. Count change while inside the loop
        # Loop throught all the list and remove certin characters
        for results in placeholder_username: # Loop goes for 50 times
            username.append(placeholder_username[count].replace('</a></td>', '')) # Go throught the list of runescape players and removes '</a></td>'
            count = count + 1 # count++

        count = 0 # Reset count for the next loop
        # Loop throught all the list and remove certin characters
        for results in placeholder_xp: # Loop goes for 318
            xp.append(placeholder_xp[count].strip('<>')) # Go throught the list of runescape players and removes '<>'
            count = count + 1

            #publication_date, ranking, username, xp
        sql = """INSERT INTO top_ten VALUES
        ('"""+publication_date+"""',1,'"""+username[0]+"""', '"""+xp[10]+"""'),
        ('"""+publication_date+"""',2,'"""+username[1]+"""', '"""+xp[16]+"""'),
        ('"""+publication_date+"""',3,'"""+username[2]+"""', '"""+xp[22]+"""'),
        ('"""+publication_date+"""',4,'"""+username[3]+"""', '"""+xp[28]+"""'),
        ('"""+publication_date+"""',4,'"""+username[4]+"""', '"""+xp[34]+"""'),
        ('"""+publication_date+"""',6,'"""+username[5]+"""', '"""+xp[40]+"""'),
        ('"""+publication_date+"""',5,'"""+username[6]+"""', '"""+xp[46]+"""'),
        ('"""+publication_date+"""',8,'"""+username[7]+"""', '"""+xp[52]+"""'),
        ('"""+publication_date+"""',6,'"""+username[8]+"""', '"""+xp[58]+"""'),
        ('"""+publication_date+"""',10,'"""+username[9]+"""', '"""+xp[64]+"""')"""
        # Close the cursor and release the server connection.
        top_ten_db.execute(sql)
        conn.commit()
        top_ten_db.close()
        conn.close()

    elif top_10_radio.get() == 3: # Previous clan data
        conn = connect(database=database_location)
        top_ten_db = conn.cursor()
        clan = []
        xp = []
        file_location = 'archive/clan.html'
        read_html_file = open(file_location).read() # Read data from archive/clan.html
        placeholder_clan = findall('[0-9,a-z,A-Z, ,\-,\_]+</a><br /><i', read_html_file) # Find all the clan names in the document

        count = 0
        for each_clan in placeholder_clan:
            clan.append(placeholder_clan[count].replace('</a><br /><i', '')) # Go throught the list of runescape clan and removes '</a></td>'
            count = count + 1

        publication_date = findall('((Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) ([0-9]{1,2})(st|nd|rd|th) of (January|February|March|April|May|June|July|August|September|October|November|December) ([0-9]{4}))', str(read_html_file))
        publication_date = publication_date[0][0]
        count = 0 # Reset count for the next loop
        # Loop throught all the list and remove certin characters
        placeholder_xp = findall('>[0-9,]+<', str(read_html_file))
        for results in placeholder_xp: # Loop goes for 318
            xp.append(placeholder_xp[count].strip('<>')) # Go throught the list of runescape players and removes '<>'
            count = count + 1

            #publication_date, ranking, username, xp
        sql = """INSERT INTO top_ten VALUES
        ('"""+publication_date+"""',1,'"""+clan[0]+"""', '"""+xp[10]+"""'),
        ('"""+publication_date+"""',2,'"""+clan[1]+"""', '"""+xp[16]+"""'),
        ('"""+publication_date+"""',3,'"""+clan[2]+"""', '"""+xp[22]+"""'),
        ('"""+publication_date+"""',4,'"""+clan[3]+"""', '"""+xp[28]+"""'),
        ('"""+publication_date+"""',4,'"""+clan[4]+"""', '"""+xp[34]+"""'),
        ('"""+publication_date+"""',6,'"""+clan[5]+"""', '"""+xp[40]+"""'),
        ('"""+publication_date+"""',5,'"""+clan[6]+"""', '"""+xp[46]+"""'),
        ('"""+publication_date+"""',8,'"""+clan[7]+"""', '"""+xp[52]+"""'),
        ('"""+publication_date+"""',6,'"""+clan[8]+"""', '"""+xp[58]+"""'),
        ('"""+publication_date+"""',10,'"""+clan[9]+"""', '"""+xp[64]+"""')"""
        # Close the cursor and release the server connection.
        top_ten_db.execute(sql)
        conn.commit()
        top_ten_db.close()
        conn.close()

    elif top_10_radio.get() == 4: # Current clan data
        conn = connect(database=database_location)
        top_ten_db = conn.cursor()
        clan = []
        xp = []
        runeclan_top_10_link = 'http://www.runeclan.com/hiscores'
        get_webite = urlopen(runeclan_top_10_link) # collect the website html document
        read_html_file = get_webite.read() # Read data from runeclan.com/xp-tracker
        placeholder_clan = findall('[0-9,a-z,A-Z, ,\-,\_]+</a><br /><i', str(read_html_file)) # Find all the clan names in the document

        count = 0
        for each_clan in placeholder_clan:
            clan.append(placeholder_clan[count].replace('</a><br /><i', '')) # Go throught the list of runescape clan and removes '</a></td>'
            count = count + 1

        publication_date = findall('((Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) ([0-9]{1,2})(st|nd|rd|th) of (January|February|March|April|May|June|July|August|September|October|November|December) ([0-9]{4}))', str(read_html_file))
        publication_date = publication_date[0][0]
        count = 0 # Reset count for the next loop
        # Loop throught all the list and remove certin characters
        placeholder_xp = findall('>[0-9,]+<', str(read_html_file))
        for results in placeholder_xp: # Loop goes for 318
            xp.append(placeholder_xp[count].strip('<>')) # Go throught the list of runescape players and removes '<>'
            count = count + 1

            #publication_date, ranking, username, xp
        sql = """INSERT INTO top_ten VALUES
        ('"""+publication_date+"""',1,'"""+clan[0]+"""', '"""+xp[10]+"""'),
        ('"""+publication_date+"""',2,'"""+clan[1]+"""', '"""+xp[16]+"""'),
        ('"""+publication_date+"""',3,'"""+clan[2]+"""', '"""+xp[22]+"""'),
        ('"""+publication_date+"""',4,'"""+clan[3]+"""', '"""+xp[28]+"""'),
        ('"""+publication_date+"""',4,'"""+clan[4]+"""', '"""+xp[34]+"""'),
        ('"""+publication_date+"""',6,'"""+clan[5]+"""', '"""+xp[40]+"""'),
        ('"""+publication_date+"""',5,'"""+clan[6]+"""', '"""+xp[46]+"""'),
        ('"""+publication_date+"""',8,'"""+clan[7]+"""', '"""+xp[52]+"""'),
        ('"""+publication_date+"""',6,'"""+clan[8]+"""', '"""+xp[58]+"""'),
        ('"""+publication_date+"""',10,'"""+clan[9]+"""', '"""+xp[64]+"""')"""
        # Close the cursor and release the server connection.
        top_ten_db.execute(sql)
        conn.commit()
        top_ten_db.close()
        conn.close()

    elif top_10_radio.get() == 5: # Previous player data from old school RuneScape
        conn = connect(database=database_location)
        top_ten_db = conn.cursor()
        username = []
        xp = []
        read_html_file = open('archive/old_school_xp.html').read() # Open and read file located in archive with the name of player.html
        count = 0
        placeholder_username = findall('[0-9,a-z,A-Z, ,\-,\_]+</a></td>', str(read_html_file))
        placeholder_xp = findall('>[0-9,]+</td>', str(read_html_file))
        # finds the day the webpage was gernerated.
        publication_date = findall('((Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) ([0-9]{1,2})(st|nd|rd|th) of (January|February|March|April|May|June|July|August|September|October|November|December) ([0-9]{4}))', str(read_html_file))
        publication_date = publication_date[0][0]

        count = 0 # This know as count++ in other languages. Count change while inside the loop
        # Loop throught all the list and remove certin characters
        for results in placeholder_username: # Loop goes for 50 times
            username.append(placeholder_username[count].replace('</a></td>', '')) # Go throught the list of runescape players and removes '</a></td>'
            count = count + 1 # count++

        count = 0 # Reset count for the next loop
        # Loop throught all the list and remove certin characters
        for results in placeholder_xp: # Loop goes for 318
            xp.append(placeholder_xp[count].strip('<>/td')) # Go throught the list of runescape players and removes '<>/td'
            count = count + 1

            #publication_date, ranking, username, xp
        sql = """INSERT INTO top_ten VALUES
        ('"""+publication_date+"""',1,'"""+username[0]+"""', '"""+xp[1]+"""'),
        ('"""+publication_date+"""',2,'"""+username[1]+"""', '"""+xp[7]+"""'),
        ('"""+publication_date+"""',3,'"""+username[2]+"""', '"""+xp[13]+"""'),
        ('"""+publication_date+"""',4,'"""+username[3]+"""', '"""+xp[19]+"""'),
        ('"""+publication_date+"""',5,'"""+username[4]+"""', '"""+xp[25]+"""'),
        ('"""+publication_date+"""',6,'"""+username[5]+"""', '"""+xp[31]+"""'),
        ('"""+publication_date+"""',7,'"""+username[6]+"""', '"""+xp[37]+"""'),
        ('"""+publication_date+"""',8,'"""+username[7]+"""', '"""+xp[43]+"""'),
        ('"""+publication_date+"""',9,'"""+username[8]+"""', '"""+xp[49]+"""'),
        ('"""+publication_date+"""',10,'"""+username[9]+"""', '"""+xp[55]+"""')"""
        # Close the cursor and release the server connection.
        top_ten_db.execute(sql)
        conn.commit()
        top_ten_db.close()
        conn.close()

    elif top_10_radio.get() == 6: # Current player data from old school RuneScape
        conn = connect(database=database_location)
        top_ten_db = conn.cursor()
        username = []
        xp = []
        runeclan_top_10_link = 'http://oldschool.runeclan.com/xp-tracker'
        get_webite = urlopen(runeclan_top_10_link) # collect the website html document
        read_html_file = get_webite.read() # Read data from runeclan.com/xp-tracker
        count = 0
        placeholder_username = findall('[0-9,a-z,A-Z, ,\-,\_]+</a></td>', str(read_html_file))
        placeholder_xp = findall('>[0-9,]+</td>', str(read_html_file))
        # finds the day the webpage was gernerated.
        publication_date = findall('((Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) ([0-9]{1,2})(st|nd|rd|th) of (January|February|March|April|May|June|July|August|September|October|November|December) ([0-9]{4}))', str(read_html_file))
        publication_date = publication_date[0][0]

        count = 0 # This know as count++ in other languages. Count change while inside the loop
        # Loop throught all the list and remove certin characters
        for results in placeholder_username: # Loop goes for 50 times
            username.append(placeholder_username[count].replace('</a></td>', '')) # Go throught the list of runescape players and removes '</a></td>'
            count = count + 1 # count++

        count = 0 # Reset count for the next loop
        # Loop throught all the list and remove certin characters
        for results in placeholder_xp: # Loop goes for 318
            xp.append(placeholder_xp[count].strip('<>/td')) # Go throught the list of runescape players and removes '<>'
            count = count + 1

            # publication_date, ranking, username, xp
        sql = """INSERT INTO top_ten VALUES
        ('"""+publication_date+"""',1,'"""+username[0]+"""', '"""+xp[1]+"""'),
        ('"""+publication_date+"""',2,'"""+username[1]+"""', '"""+xp[7]+"""'),
        ('"""+publication_date+"""',3,'"""+username[2]+"""', '"""+xp[13]+"""'),
        ('"""+publication_date+"""',4,'"""+username[3]+"""', '"""+xp[19]+"""'),
        ('"""+publication_date+"""',5,'"""+username[4]+"""', '"""+xp[25]+"""'),
        ('"""+publication_date+"""',6,'"""+username[5]+"""', '"""+xp[31]+"""'),
        ('"""+publication_date+"""',7,'"""+username[6]+"""', '"""+xp[37]+"""'),
        ('"""+publication_date+"""',8,'"""+username[7]+"""', '"""+xp[43]+"""'),
        ('"""+publication_date+"""',9,'"""+username[8]+"""', '"""+xp[49]+"""'),
        ('"""+publication_date+"""',10,'"""+username[9]+"""', '"""+xp[55]+"""')"""
        # Close the cursor and release the server connection.
        top_ten_db.execute(sql)
        conn.commit()
        top_ten_db.close()
        conn.close()

    else:
        alert("Save to database was pressed. To save a the 10 list please click on a button above.")

def exit_program(): # A function which ends the program.
    main_screen.destroy()

#____________________ End Of Predefinded  ____________________#
#____________________ Widgets ____________________#
Title_label = Label(main_screen, text="Race To The Top Postion", font=font_heading_1)
runescape_logo_label_left = Label(image = main_screen_leftside_logo_image)
preview_button = Button(text = ' Preview', font = button_font, command = preview_list)
export_button = Button(text = ' Export', font = button_font, command=export_list)
save_to_database_button = Button(text = ' Save to Database', font = button_font, command=insert_into_db)
close_window_button = Button(text = ' Exit ', font = button_font, command=exit_program)
runescape_logo_label_right = Label(image = main_screen_rightside_logo_image)

# group 1
group_1_widgets = LabelFrame(main_screen, text='Top 10 players who have gained the most xp', font=font_times_15)
group_1_preview_radio_button = Radiobutton(group_1_widgets, text = ' Previous', variable = top_10_radio, value = 1, font=font_times_15)
group_1_current_radio_button = Radiobutton(group_1_widgets, text = ' Current', variable = top_10_radio, value = 2, font=font_times_15)

# group 2
group_2_widgets = LabelFrame(main_screen, text='Top 10 clans who have gained the most xp', font=font_times_15)
group_2_preview_radio_button = Radiobutton(group_2_widgets, text = ' Previous', variable = top_10_radio, value = 3, font=font_times_15)
group_2_current_radio_button = Radiobutton(group_2_widgets, text = ' Current', variable = top_10_radio, value = 4, font=font_times_15)

# group 3
group_3_widgets = LabelFrame(main_screen, text='Top 10 OSRS Players who have gained the most xp', font=font_times_15)
group_3_preview_radio_button = Radiobutton(group_3_widgets, text = ' Previous', variable = top_10_radio, value = 5, font=font_times_15)
group_3_current_radio_button = Radiobutton(group_3_widgets, text = ' Current', variable = top_10_radio, value = 6, font=font_times_15)

#____________________ End of Widget ____________________#


#____________________ Widget Placement ____________________#
# Sceen 1
Title_label.grid(column=2, row=0, columnspan=2)
runescape_logo_label_left.grid(column=0, row=1, columnspan=2, rowspan=4, sticky=W)
group_1_widgets.grid(column=2, row=1, columnspan=2) # Place a boarded in the window for group 1 of Radiobutton
group_1_preview_radio_button.grid(column=1, row=1) # Place in group_1_widgets
group_1_current_radio_button.grid(column=2, row=1) # Place in group_1_widgets
runescape_logo_label_right.grid(column=4, row=1, columnspan=2, rowspan=4, sticky=E)

group_2_widgets.grid(column=2, row=2, columnspan=2) # Place a boarded in the window for group 2 of Radiobutton
group_2_preview_radio_button.grid(column=1, row=1) # Place in group_2_widgets
group_2_current_radio_button.grid(column=2, row=1) # Place in group_2_widgets

group_3_widgets.grid(column=2, row=3, columnspan=2) # Place a boarded in the window for group 2 of Radiobutton
group_3_preview_radio_button.grid(column=1, row=1) # Place in group_3_widgets
group_3_current_radio_button.grid(column=2, row=1) # Place in group_3_widgets

preview_button.grid(column=1, row=7) # Buttons are place at the bottom of the window
export_button.grid(column=2, row=7) # Buttons are place at the bottom of the window
save_to_database_button.grid(column=3, row=7) # Buttons are place at the bottom of the window
close_window_button.grid(column=4, row=7) # Buttons are place at the bottom of the window
#____________________ End 0f Widget Placement ____________________#

# Start the event loop
main_screen.mainloop() # Main Screen
