################################################################################
# Author: Orion Crocker
# Filename: cleancheck.py
# Date: 10/23/19
#
# Parses lyrics objects
# Description: Checks lyrics objects from isitclean main and returns boolean
#	value
################################################################################

def check_lyrics(lyrics):

  # 7 words regulated by FCC with variations
  fcc = ['shit', 'piss', 'fuck', 'cunt', 'cock',
         'tits', 'titty', 'titties']

  clean = True
  lyric_array = lyrics.splitlines()

  for line in lyric_array:
    current_line = line.lower()
    current_line = current_line.split()
    for word in current_line:
      for words in fcc:
        if words in word:
          print(line)
          clean = False

  if clean is False:
    return 'dirty'
  return 'clean'
