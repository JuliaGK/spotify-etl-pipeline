from spotipy import Spotify

class ExtractSpotifyAPI():
    def __init__(self, spotify: Spotify) -> None:
        self.sp = spotify
    
    def get_playlist_json(self, playlist_id):
        results = self.sp.playlist_items(playlist_id)
        return results

