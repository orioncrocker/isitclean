# isitclean, fork of LyricsGenius by johnwmillr
[![Build Status](https://travis-ci.org/johnwmillr/LyricsGenius.svg?branch=master)](https://travis-ci.org/johnwmillr/LyricsGenius)
[![PyPI version](https://badge.fury.io/py/lyricsgenius.svg)](https://pypi.org/project/lyricsgenius/)
[![Python version](https://img.shields.io/badge/python-3.x-brightgreen.svg)](https://pypi.org/project/lyricsgenius/)

`lyricsgenius` provides a simple interface to the song, artist, and lyrics data stored on [Genius.com](https://www.genius.com).

`isitclean` utilizes `lyricsgenius` to quickly find ["clean"](https://www.fcc.gov/consumers/guides/obscene-indecent-and-profane-broadcasts) songs by a specific artist or album.

## Setup
Before using this package you'll need to sign up for a (free) account that authorizes access to [the Genius API](http://genius.com/api-clients). The Genius account provides a `client_access_token` that is required by the package. See the [Usage section](https://github.com/johnwmillr/LyricsGenius#usage) below for examples.
By default, isitclean imports a config file with a variable named client\_access\_token. Create your own config.py and store your unique client access token from Genius there.

## Installation
`lyricsgenius` requires Python 3.

Use `pip` to install the package from PyPI:

```bash
NOT YET IMPLEMENTED
pip install isitclean
```

Or, clone the latest version of the package from GitHub:

```bash
git clone https://github.com/orioncrocker/isitclean
```

## Usage
Search for song with arguments 'song' and 'artist'

```bash
python3 -m isitclean song "Feed The Horses" "Thank You Scientist"
```

Search for an artist, by default most popular songs will be fetched

```bash
python3 -m isitclean artist "Smashing Pumpkins"
```

Search for ten songs by 'Protest The Hero'

```bash
python3 -m isitclean artist "Protest The Hero" --max-songs 10
```

Import the package and search for songs by a given artist:

```python
import isitclean
genius = lyricsgenius.Genius("my_client_access_token_here")
artist = genius.search_artist("Andy Shauf", max_songs=3, sort="title")
print(artist.songs)
```

Search for a single song by the same artist:

```python
song = genius.search_song("To You", artist.name)
print(song.lyrics)
```

Add the song to the artist object:

```python
artist.add_song(song)
```

Save the artist's songs to a JSON file:

```python
artist.save_lyrics()
```

There are various options configurable as parameters within the `Genius` class:

```python
genius.clean = False # Doesn't print if songs have profanities or not
genius.verbose = False # Turn off status messages
genius.remove_section_headers = True # Remove section headers (e.g. [Chorus]) from lyrics when searching
genius.skip_non_songs = False # Include hits thought to be non-songs (e.g. track lists)
genius.excluded_terms = ["(Remix)", "(Live)"] # Exclude songs with these words in their title
```

## Planned features:
Search by album rather than limited to just song or artist search
```bash
python3 -m isitclean album "Float" "Aesop Rock"
```

## Example projects from lyricsgenius author johnwmillr

  - [Trucks and Beer: A textual analysis of popular country music](http://www.johnwmillr.com/trucks-and-beer/)
  - [Neural machine translation: Explaining the Meaning Behind Lyrics](https://github.com/tsandefer/dsi_capstone_3)
  - [What makes some blink-182 songs more popular than others?](http://jdaytn.com/posts/download-blink-182-data/)
  - [Sentiment analysis on hip-hop lyrics](https://github.com/Hugo-Nattagh/2017-Hip-Hop)
  - [Does Country Music Drink More Than Other Genres?](https://towardsdatascience.com/does-country-music-drink-more-than-other-genres-a21db901940b)
  - [49 Years of Lyrics: Why So Angry?](https://towardsdatascience.com/49-years-of-lyrics-why-so-angry-1adf0a3fa2b4)
