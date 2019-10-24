################################################################################
# Author: Orion Crocker
# Filename: isitclean.py
# Date: 10/23/19
#
# Is It Clean?
# Description: Is it clean main file
################################################################################

import config
import lyricsgenius
import argparse


def main(args=None):

  parser = argparse.ArgumentParser()
  parser.add_argument("search_type", type=str.lower, choices=["song", "artist"],
                      help="Specify whether search is for 'song' or 'artist'")
  parser.add_argument("terms", type=str, nargs="+",
                      help="Provide terms for search")
  parser.add_argument("--max-songs", type=int,
                      help="Specify number of songs when searching for artist")
  args = parser.parse_args()

  genius = lyricsgenius.Genius(config.client_access_token)

  if args.search_type == "song":
    song = genius.search_song(*args.terms,
                              isitclean=True)
    if not song:
      print("Could not find specified song. Check spelling?")
    else:
      print("\n{} - {} {}" .format(song.title, song.artist,
            song.clean))

  elif args.search_type == "artist":
    artist = genius.search_artist(args.terms[0],
                               max_songs=args.max_songs,
                               sort='popularity',
                               isitclean=True)

  else:
    print("Add some arguments man!\n",
          "For example: python3 -m isitclean song 'Rings' 'Aesop Rock'")

if __name__ == "__main__":
  main()
