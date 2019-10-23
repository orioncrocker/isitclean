################################################################################
# Author: Orion Crocker
# Filename: isitclean.py
# Date: 10/23/19
#
# Is It Clean?
# Description: Is it clean test file
################################################################################

# user specific client access token in another file
from token import client_access_token

import lyricsgenius

genius = lyricsgenius.Genius(config.client_access_token);
artist = genius.search_artist("Aesop Rock", max_songs=3, sort="title")
print(artist.songs)
