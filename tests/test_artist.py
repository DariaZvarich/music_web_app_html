from lib.artist import *

def test_constructs():
    artist = Artist('Pixies', 'Alternative Rock')
    assert artist.name == 'Pixies'
    assert artist.genre == 'Alternative Rock'

def test_equal():
    artist1 = Artist('Pixies', 'Alternative Rock')
    artist2 = Artist('Pixies', 'Alternative Rock')
    assert artist1 == artist2

def test_return_a_string():
    artist = Artist('Pixies', 'Alternative Rock')
    assert str(artist) == "Artist(Pixies, Alternative Rock)"