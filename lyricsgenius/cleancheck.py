################################################################################
# Author: Orion Crocker
# Filename: check_if_clean.py
# Date: 10/23/19
#
# Parses lyrics objects
# Description: Checks lyrics objects from isitclean main and returns boolean
#	value
################################################################################

def check_lyrics(lyrics):

  # 7 words regulated by FCC with variations
  fcc = ['shit', 'shitty', 'shitting' 'piss', 'pissy', 'pissing', 'fuck',
         'fucky', 'fucking', 'motherfucker', 'cunt', 'cock', 'cocksucker',
         'tits', 'titty' 'titties']
  clean = True

  lyric_array = lyrics.splitlines()
  for line in lyric_array:
    current_line = line.split()
    for word in current_line:
      if word in fcc:
        clean = False

  if clean is False:
    return("dirty")
  else:
    return("clean")
