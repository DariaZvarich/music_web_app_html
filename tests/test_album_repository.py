from lib.album_repository import *
from lib.album import *
''''
when i call  #ll
i get all the albums in the albums table
'''
def test_all(db_connection):
    db_connection.seed("seeds/MusicAlbums.sql")
    repository = AlbumRepository (db_connection)
    assert repository.all() == [Album(1,'Born in the U.S.A.', 1984, 1)]


''''
when we call # create
i create an album in the database 
and i can see it back in #all 
'''
def test_create(db_connection):
    db_connection.seed("seeds/MusicAlbums.sql")
    repository = AlbumRepository (db_connection)
    album = Album(None, 'test title', 1970, 3)
    repository.create(album)
    assert repository.all() == [Album(1,'Born in the U.S.A.', 1984, 1), Album(2, 'test title', 1970, 3)]