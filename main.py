from databaseDesign import DatabaseManager
from api_setup import *
from voiceRec import *
from model import *
import pyaudio

'''Music search history that saving everything in table called myPlaylist to create music_info.db file,
    that pulls data from the Spotify API
    '''

# some global values so we only have to fix code once if we find a typo in string value
BY_ARTIST = 'artist'
BY_ALBUM = 'album'
BY_TRACK_TITLE = 'track'


'''
methods used in main()
'''
def isValidTrackChoice(tocheck,range):
    # TODO we also need to reject non-integers
    if tocheck.isnumeric():
        return int(tocheck) in range
    return False

def get_user_selection(track_list):
    # this presents users with a list of track so user can pick which album to work with
    track_count = len(track_list)
    for i in range(track_count):
        print (str(i) + " " + str(track_list[i]))
    user_choice = input("Which track would you like to import (type 'exit' (no quotes) to exit)?")
    # there has to be a way to combine these into a single while statement, but I couldn't figure that out.
    if user_choice == 'exit': return None
    while not isValidTrackChoice(user_choice,range(0,track_count)):
        user_choice = input("You have not made a valid selection.  Which track would you like to import?")
    return track_list[int(user_choice)]
# end get_user_selection

def add_to_database(db, my_song):
    try:
        print("the music result: " + str(my_song))
        db.populate_database(my_song.id, my_song.title, my_song.artist, my_song.album)
        print("data successfully input\n")

    # if the result wasn't find
    # or the can't be pushed for some reason
    # print an error message
    except Exception:
        print("No result for this Search. Try again.\n" +
              "Failed to input in music database\n")
# end add_to_database


'''
main method of program
'''
def main():
    # Setting up database and give it the name "music_info"

    db = DatabaseManager("music_info")
    db.setup_db()
    while True:

        #Getting user decision to start or quit the program then print the table

        user_choice = str(input("Do you want to enter data in music table: \n"))

        if user_choice.upper() == "YES":

            what_to_find = ''
            while True:

                # if the user type "yes" then do this
                text_result = input("Type an artist name or press Enter to Skip for Voice Input: \n")
                if text_result:
                    what_to_find = text_result
                    break

                # Getting the voice recognition words and save in a variable

                voice_word = voice_input()
                if voice_word:
                    what_to_find = voice_word
                    break

                else:
                    continue


            # Pass the user parameter as argument to spotify method
            # from api_setup.py file and return values
            '''these don't do quite what Yannick intended, but they can be repurposed for more targeted searches'''
            # title = search_track(search_result)
            # artist = search_artist(search_result)
            # album = search_album(search_result)
            # id = None

            # find matches based on user input
            tracks_found = search_tracks(what_to_find)
            # check that there are results, else report none found and loop back to beginning
            if not (len(tracks_found) > 0):
                print("No results found. Please try again.")
                continue

            # create a music_result object from the data
            my_song = get_user_selection(tracks_found)

            # Here is some exception handling that check for the Spotify api result
            # then tell us if the result was found
            #then push it to the database
            add_to_database(db, my_song)
        # Quit the program if the user input anything but "yes"
        #then print the database "music_info.db

        else:
            break

    result = db.display_info()
    print("Here is your database copy\n")
    print("%2s%60s%60s%60s\n" % ("ID", "TITLE", "ARTIST", "ALBUM_NAME"))
    for music in result:
        print("%2d%60s%60s%60s" % (music.id, music.title, music.artist, music.album))




main()