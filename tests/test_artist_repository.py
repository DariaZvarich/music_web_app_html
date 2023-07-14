from lib.artist import *
from lib.artist_repository import *


def test_all(db_connection):
    db_connection.seed("seeds/MusicAlbums.sql")
    repository = ArtistRepository(db_connection)
    assert repository.all() == [
        Artist('Pixies', 'Alternative Rock'), 
        Artist('ABBA', 'Pop'), 
        Artist('Taylor Swift', 'Pop'),
        Artist('Nina Simone', 'Jazz')]
    
def test_create(db_connection):
    db_connection.seed("seeds/MusicAlbums.sql")
    repository = ArtistRepository(db_connection)
    artist = Artist(name= "Wild nothing", genre="Indei")
    repository.create(artist) 
    assert repository.all() == [
        Artist('Pixies', 'Alternative Rock'), 
        Artist('ABBA', 'Pop'), 
        Artist('Taylor Swift', 'Pop'),
        Artist('Nina Simone', 'Jazz'),
        Artist('Wild nothing', 'Indei')
        ]