
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

# Predefinded fonts
heading_1 = ("Arial", 25)
font_times_15 = ("Times", 15)

# Images
main_screen_logo_image = PhotoImage(file = 'archive/images/placeholder.png')
RS3_logo_image = PhotoImage(file="archive/images/RuneScape_3_Logo.png")
OSRS_logo_image = PhotoImage(file="archive/images/Old_School_RuneScape_logo.png")
Clan_banner_image = PhotoImage(file="archive/images/Clan_Banner.png")
#____________________ End of Variables ____________________#

def preview_list():
    if top_10_radio.get() == 1: # Previous player data
        search_rs3_player_html_archive = []
        count = 0
        archive_rs3_player_html = open('archive/player.html').read() # Open and read file located in archive with the name of player.html
        placeholder_search_rs3_player_html_archive = findall('[0-9,a-z,A-Z, ,\-,\_]+</a></td>', archive_rs3_player_html) # Find all the players name in the document
        for player in placeholder_search_rs3_player_html_archive:
            search_rs3_player_html_archive.append(placeholder_search_rs3_player_html_archive[count].replace('</a></td>', '')) # Go throught the list of runescape players and removes '</a></td>'
            count = count + 1

        rs3_player_xp_screen = Toplevel() # Top 10 xp gained today after 10am to 9:59am the next day
        rs3_player_xp_screen.title('Top 10')
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
        rs3_player_xp_screen.title('Top 10')
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
        pass
        # Currently does nothing.
def export_list():
    if top_10_radio == 1:
        HTML_title = "Previous Top 10 players list for xp gained"
        HTML_heading = "<h1>Top 10 players who have gained the most xp today </h1>"
        HTML_heading_image = '<img src="https://vignette.wikia.nocookie.net/runescape2/images/3/3d/RuneScape_3_Logo.png/revision/latest?cb=20140317195258" alt="RuneScape 3 lolgo from RuneWiki">'
        HTML_table_heading = """<table>
        <tr>
          <th>Ranking</th>
          <th>Player Icon</th>
          <th>Username</th>
          <th>Today's XP Gained</th>
        </tr>
        """

    elif top_10_radio == 2:
        HTML_title = "Current Top 10 players list for xp gained"
        HTML_heading = "<h1>Top 10 players who have gained the most xp today </h1>"
        HTML_heading_image = '<img src="https://vignette.wikia.nocookie.net/runescape2/images/3/3d/RuneScape_3_Logo.png/revision/latest?cb=20140317195258" alt="RuneScape 3 lolgo from RuneWiki">'
        HTML_table_heading = """<table>
        <tr>
          <th>Ranking</th>
          <th>Player Icon</th>
          <th>Username</th>
          <th>Today's XP Gained</th>
        </tr>
        """

    elif top_10_radio == 3:
        HTML_title = "Previous Top 10 clan"
        HTML_heading = "<h1>Previously top 10 clans based on how much xp the clan has gathered in a day.</h1>"
        HTML_heading_image = '<img src="" alt="">'
        HTML_table_heading = """<table>
        <tr>
          <th>Ranking</th>
          <th>Clan Banner</th>
          <th>Clan Name</th>
          <th>Today's XP Gained</th>
        </tr>
        """

    elif top_10_radio == 4:
        HTML_title = "Current Top 10 clan"
        HTML_heading = "<h1>Current Top 10 clans based on how much xp the clan has gathered today.</h1>"
        HTML_heading_image = '<img src="" alt="">'
        HTML_table_heading = """<table>
        <tr>
          <th>Ranking</th>
          <th>Clan Banner</th>
          <th>Clan Name</th>
          <th>Today's XP Gained</th>
        </tr>
        """

    elif top_10_radio == 5:
        HTML_title = "Previous Top 10 old school players list for xp gained"
        HTML_heading = "<h1>Previous Top 10 old school player based on how much xp the player has gathered on the day.</h1>"
        HTML_heading_image = '<img src="" alt="">'
        HTML_table_heading = """<table>
        <tr>
          <th>Ranking</th>
          <th>Player Icon</th>
          <th>Username</th>
          <th>Today's XP Gained</th>
        </tr>
        """

    elif top_10_radio == 6:
        HTML_title = "Current Top 10 old school players list for xp gained"
        HTML_heading = "<h1>Current  Top 10 old school player based on how much xp the player has gathered on the today</h1>"
        HTML_heading_image = '<img src="" alt="">'
        HTML_table_heading = """<table>
        <tr>
          <th>Ranking</th>
          <th>Player Icon</th>
          <th>Username</th>
          <th>Today's XP Gained</th>
        </tr>
        """

    else:
        HTML_title = "No data is given"

    create_html_file = open("archive/export.html", "w")
    create_html_file.write(HTML_head_part_a)
    create_html_file.write(HTML_title)
    create_html_file.write(HTML_head_part_b)
    create_html_file.write("info HERE")
    create_html_file.write(HTML_end)
#____________________ Widgets ____________________#
runescape_logo_label = Label(image = main_screen_logo_image)
preview_button = Button(text = ' Preview', font = ('Arial', 24), command = preview_list)
export_button = Button(text = ' Export', font = ('Arial', 24), command=export_list)

# group 1
group_1_preview_radio_button = Radiobutton(text = ' Previous', variable = top_10_radio, value = 1,)
group_1_current_radio_button = Radiobutton(text = ' Current', variable = top_10_radio, value = 2)

# group 2
group_2_preview_radio_button = Radiobutton(text = ' Previous', variable = top_10_radio, value = 3)
group_2_current_radio_button = Radiobutton(text = ' Current', variable = top_10_radio, value = 4)

# group 3
group_3_preview_radio_button = Radiobutton(text = ' Previous', variable = top_10_radio, value = 5)
group_3_current_radio_button = Radiobutton(text = ' Current', variable = top_10_radio, value = 6)

#____________________ End of Widget ____________________#


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
export_button.grid(column=4, row=3)

# RuneScape Top 10 players of the day screen layout.
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
