################################################################################
# Author: Orion Crocker
# Filename: isitclean.py
# Date: 10/23/19
#
# Is It Clean?
# Description: Is it clean test file
################################################################################

# user specific client access token in another file
import config

import lyricsgenius
import os
import argparse

def main(args=None):

  parser = argparse.ArgumentParser()
  parser.add_argument("search_type", type=str.lower, choices=["song", "artist"],
                      help="Specify whether search is for 'song' or 'artist'")
  parser.add_argument("terms", type=str, nargs="+",
                      help="Provide terms for search")
  args = parser.parse_args()

  genius = lyricsgenius.Genius(config.client_access_token)

  if args.search_type == "song":
    song = genius.search_song(*args.terms)
    if not song:
      print("Could not find specified song. Check spelling?")

    else:
      # need to parse song for dirty words
      print("Found {} by {}\n" .format(song.title, song.artist))
      print(song.lyrics)

  else:
    print("Add some arguments man!\n",
          "For example: python3 isitclean 'Rings' 'Aesop Rock'")

if __name__ == "__main__":
  main()
