import sqlite3
import pandas as pd
from datetime import date


class LoadSpotify():
    def __init__(self) -> None:
        self.con = self.get_sqlite_connection()
    
    def run(self, data: pd.DataFrame):
        today_date = date.today()
        cur = self.con.cursor()
        for index, row in data.iterrows():   
            query = """
            INSERT INTO top_100_songs (name, track_number, song_uri, artists, created_date) 
            VALUES (
                "{name}", {track_number}, "{song_uri}", "{artists}", "{created_date}"
            );
            """.format_map({'name': row['name'], 'track_number': row['track_number'], 'song_uri': row['song_uri'], 'artists': row['artists'], 'created_date': today_date})
            cur.execute(query)
        
        self.con.commit()
        self.con.close()

    def get_sqlite_connection(self):
        con = sqlite3.connect("spotify.db")
        return con


    def create_table(self):
        self.con.cursor().execute("""
                CREATE TABLE top_100_songs
                (id INTEGER PRIMARY KEY,
                name TEXT,
                track_number INTEGER,
                song_uri TEXT,
                artists TEXT,
                created_date TEXT);
            """)
        self.con.close()

    def select_all_playlist(self):
        result = self.con.cursor().execute("""
                SELECT * FROM top_100_songs;
            """)
        print(result.fetchall())
        self.con.close()