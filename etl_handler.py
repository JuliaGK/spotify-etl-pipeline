import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from extract_spotify import ExtractSpotifyAPI
from transform_spotify import TransformSpotify

class ETLHandler():
    def __init__(self) -> None:
        self.sp = self.get_api_connection()
        
    def run(self):
        playlist_url_top_100 = "https://open.spotify.com/playlist/3IsxzDS04BvejFJcQ0iVyW"

        extract_api = ExtractSpotifyAPI(self.sp)
        json_playlist = extract_api.get_playlist_json(playlist_url_top_100)

        TransformSpotify().playlist_json_to_df(json_playlist)

    def get_api_connection(self) -> spotipy.Spotify:
        client_credentials_manager = SpotifyClientCredentials(client_id=config.SPOTIPY_CLIENT_ID, client_secret=config.SPOTIPY_CLIENT_SECRET)
        return spotipy.Spotify(client_credentials_manager=client_credentials_manager)