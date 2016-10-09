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


def search_tracks(search_string,search_type=None):
    # this just returns results based on whatever search stirng the user enters
    # it could be an artist's name, an album title, or even a specific song.
    track_list = []  # this stores the list of results
    if search_type is not None:
        # if a search type is specified, prefix it to the search string
        # see https://developer.spotify.com/web-api/search-item/
        search_string = search_type + ":" + search_string
        print(search_string)
    tracksfound=(sp.search(q=search_string, limit=5))
    # debugging: pprint(tracksfound)
    tracks = tracksfound['tracks']['items']
    for track in tracks:
        song_title = (track['name'])
        album_title = (track['album']['name'])
        artist = (track['artists'][0]['name'])
        # build a music_result object so we can exploit its methods
        this_song = model.music_result(None, song_title, artist, album_title)
        track_list.append(this_song)
    # and then return the array of tracks found
    return track_list

'''
debugging/testing
'''
if __name__ == "__main__":
    #this works
    slist = (search_tracks("Madonna"))
    for entry in slist:
        print(entry.artist)

    # but this doesn't??
    slist = (search_tracks("Madonna","artist"))
    for entry in slist:
        print(entry.artist)
