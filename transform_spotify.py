import pandas as pd
import json

class TransformSpotify():
    def __init__(self) -> None:
        pass

    def playlist_json_to_df(self, playlist_json) -> pd.DataFrame:
        df_columns = ['name', 'track_number', 'song_uri', 'duration', 'artists']

        playlist_infos = []
        for idx, item in enumerate(playlist_json['items']):
            song_infos = []

            song_infos.append(item['track']['name'])
            song_infos.append(idx+1)
            song_infos.append(item['track']['uri'])
            song_infos.append(item['track']['duration_ms'])

            artists = item['track']['artists']
            artists_list = [] 
            for artist in artists:
                artists_list.append(artist['name'])
            song_infos.append(", ".join(artists_list))

            playlist_infos.append(song_infos)
    
        return pd.DataFrame(playlist_infos, columns=df_columns)

