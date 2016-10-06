import spotipy, model
from pprint import pprint

'''
Credit info to Spotify Web API Documenttation
https://developer.spotify.com/web-api/console/tracks/
Importing Spotipy directory from the spotipy package
'''

#Creating a Spotify object called sp

sp = spotipy.Spotify()


def search_artist(value):

    #Get Artist result from spotify API by using the parameter from user input and return it to the variable

    results = sp.search(q=value, limit=1, type='artist')
    for item in results['artists']['items']:
        return item['name']


def search_album(value):

    # Get Album result from spotify API by using the parameter from user input and return it to the variable

    results = sp.search(q=value, limit=1, type='album')
    for item in results['albums']['items']:
        return item['name']


def search_track(value):

    # Get Song result from spotify API by using the parameter from user input and return it to the variable

    results = sp.search(q=value, limit=1, type='track')
    for item in results['tracks']['items']:
        return item['name']


def search_albums_by_artist(artist_name):
    song_list = []
    testres=(sp.search(q=artist_name, limit=5))
    song_results = testres['tracks']['items']
    # counter to iterate through list of songs
    i=0
    for song in song_results:
        song_title = (song['name'])
        album_title = (song['album']['name'])
        artist = (song['artists'][0]['name'])
        this_song = model.music_result(None, song_title, album_title, artist)
        song_list.append(this_song)
        # increment our counter
        i += 1
    #pprint(testres)
    return song_list

# slist = (search_albums_by_artist("Madonna"))
# for entry in slist:
#     print(str(entry))

# pprint(sp.search(q="Madonna", limit=5))