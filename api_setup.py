import spotipy

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






