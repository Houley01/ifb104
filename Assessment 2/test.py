from urllib.request import urlopen
from re import *

archive_rs3_player_html = open('archive/player.html').read()
search_rs3_player_html_archive = findall('[0-9,a-z,A-Z, ,\-,\_]+</a></td>', str(archive_rs3_player_html)) # Find all the players name in the document

search_rs3_clan_html_archive_xp_rate = findall('>[0-9,]+<', archive_rs3_player_html)

print(search_rs3_clan_html_archive_xp_rate[10].strip('<>')) #1
print(search_rs3_clan_html_archive_xp_rate[16].strip('<>')) #2
print(search_rs3_clan_html_archive_xp_rate[22].strip('<>')) #3
print(search_rs3_clan_html_archive_xp_rate[28].strip('<>')) #4
print(search_rs3_clan_html_archive_xp_rate[34].strip('<>')) #5
print(search_rs3_clan_html_archive_xp_rate[40].strip('<>')) #6
print(search_rs3_clan_html_archive_xp_rate[46].strip('<>')) #7
print(search_rs3_clan_html_archive_xp_rate[52].strip('<>')) #8
print(search_rs3_clan_html_archive_xp_rate[58].strip('<>')) #9
print(search_rs3_clan_html_archive_xp_rate[64].strip('<>')) #10

HTML_head = """<!DOCTYPE html>
<html lang="en">
  <head>
    <link rel="stylesheet" href="css/master.css">
    <meta charset="utf-8">
    <title>Top 10 XP Gained</title>
  </head>
  <style media="screen">
    .column {
      float: left;
    }
  </style>
  <body>
"""

HTML_end= """

  <body>
</html>
"""
create_html_file = open("archive/export.html", "w")
create_html_file.write(HTML_head)
create_html_file.write("<h1>")
create_html_file.write(search_rs3_player_html_archive[9])
create_html_file.write("</h1>")
create_html_file.write("<h1>HI</h1>")
create_html_file.write(HTML_end)
