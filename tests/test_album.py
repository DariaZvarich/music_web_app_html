from lib.album import *
'''
constructs with an id, title, release_year and artist_id
'''

def test_constructs():
    album = Album(1, 'test title', 1970, 3)
    assert album.id == 1
    assert album.title == 'test title'
    assert album.release_year == 1970
    assert album.artist_id == 3

'''
albums with equal contents are equal
'''
def test_equal():
    album1 = Album(1, 'test title', 1970, 3)
    album2 = Album(1, 'test title', 1970, 3)
    assert album1 == album2


'''
represent albums as string 
'''
def test_return_a_string():
    album = Album(1, 'test title', 1970, 3)
    assert str(album) == "Album(1, test title, 1970, 3)"