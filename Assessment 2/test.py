from urllib.request import urlopen
from re import *
top_10_radio = 5
search_rs3_player_html_archive = []
archive_rs3_player_html = open('archive/player.html').read()
placeholder = findall('[0-9,a-z,A-Z, ,\-,\_]+</a></td>', str(archive_rs3_player_html)) # Find all the players name in the document
count = 0

for player in placeholder:
    search_rs3_player_html_archive.append(placeholder[count].replace('</a></td>', ''))
    count = count + 1
print(search_rs3_player_html_archive)
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

HTML_head_part_a = """<!DOCTYPE html>
<html lang="en">
  <head>
    <link rel="stylesheet" href="css/master.css">
    <meta charset="utf-8">
    <title>"""

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

HTML_head_part_b = """</title>
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

print(HTML_head_part_a)
print(HTML_title)
print(HTML_head_part_b)
print(HTML_heading_image)
print(HTML_heading)
print(HTML_table_heading)

# create_html_file = open("archive/export.html", "w")
# create_html_file.write(HTML_head_part_a)
# create_html_file.write(HTML_title)
# create_html_file.write(HTML_head_part_b)
# create_html_file.write("<h1>")
# create_html_file.write(search_rs3_player_html_archive[9])
# create_html_file.write("</h1>")
# create_html_file.write("<h1>HI</h1>")
# create_html_file.write(HTML_end)
