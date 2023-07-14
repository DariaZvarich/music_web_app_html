from lib.artist import *

class ArtistRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * from Artists")
        return [ Artist(row["name"], row["genre"]) for row in rows ]
    
    def create(self, artist):
        self._connection.execute (
            "INSERT INTO artists (name, genre) VALUES (%s, %s)",
            [artist.name, artist.genre]
            ) 
        return None