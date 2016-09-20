import sqlite3
from model import *

class DatabaseManager:

    def __init__(self,filename):
        self.conn = sqlite3.connect(filename)

    def setup_db (self):

        table_script = '''
            CREATE TABLE myPlaylist (
            musicID INTEGER PRIMARY KEY ,
            title TEXT NOT NULL,
            Artist TEXT NOT NULL ,
            Album TEXT NOT NULL
            );



            INSERT INTO myPlaylist VALUES (NULL, 'No Limit', 'Usher', 'Single Album'); '''

        try:
            print("Creating myPlaylistTable...")
            self.conn.executescript(table_script)
            print("Table successfully created")
        except sqlite3.OperationalError as eo:
            print("Error: ", eo)

    def populate_database(self,music_id, title,artist, album):
        """Getting info from the Spotify api then populate the database"""
        try:
            cur = self.conn.cursor()
            query = 'INSERT INTO myPlaylist VALUES (?, ?, ?, ?)'
            cur.execute(query, (music_id, title, artist, album))
            self.conn.commit()

        except sqlite3.OperationalError as oe:
            print('Sql execution error', oe)
        except sqlite3.Error as e:
            print("Connection error ", e)

    def display_info(self):
        """Return data from the myPlaylist."""
        cur = self.conn.cursor()
        query = 'SELECT * FROM myPlaylist'
        cur.execute(query)

        music_list = []
        for row in cur.fetchall():
            musics = music_result(row[0],row[1], row[2], row[3])
            music_list.append(musics)
        return music_list








