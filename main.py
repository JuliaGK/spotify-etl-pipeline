from etl_handler import ETLHandler
from load_spotify import LoadSpotify

handler = ETLHandler()
handler.run()
#load_spotify = LoadSpotify()
#load_spotify.select_all_playlist()