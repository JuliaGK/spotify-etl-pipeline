import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import json
import config
from datetime import datetime

scope = "user-library-read"

client_credentials_manager = SpotifyClientCredentials(client_id=config.SPOTIPY_CLIENT_ID,
client_secret=config.SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


playlist_url_top_100 = "https://open.spotify.com/playlist/3IsxzDS04BvejFJcQ0iVyW"

results = sp.playlist_items(playlist_url_top_100)
for idx, item in enumerate(results['items']):
    name = item['track']['name']
    track_number = item['track']['track_number']
    song_uri = item['track']['uri']
    artists = item['track']['artists']
    artists_list = [] 
    duration = item['track']['duration_ms']
    for artist in artists:
        artists_list.append(artist['name'])
    
    print("\n\nPOSITION: ", idx+1)
    print("SONG NAME: ", name)
    print("TRACK NUMBER: ",track_number)
    print("SONG URI: ",song_uri)
    print("ARTISTS: ", ", ".join(artists_list))
    print("DURATION(ms): ", duration)
    