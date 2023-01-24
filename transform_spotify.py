import pandas as pd
import json

class TransformSpotify():
    def __init__(self) -> None:
        pass

    def playlist_json_to_df(self, playlist_json) -> pd.DataFrame:
        for idx, item in enumerate(playlist_json['items']):
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
    


