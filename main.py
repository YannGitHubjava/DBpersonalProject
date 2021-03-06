from databaseDesign import DatabaseManager
from api_setup import *
from voiceRec import *
from menus import *
from model import *
import pyaudio

'''Music search history that saving everything in table called myPlaylist to create music_info.db file,
    that pulls data from the Spotify API
    '''

# some global values so we only have to fix code once if we find a typo in string value
BY_ARTIST = 'artist'  # these three are static values passed as parameters to search_tracks
BY_ALBUM = 'album'
BY_TRACK_TITLE = 'track'


'''
methods used in main()
'''
def isValidTrackChoice(tocheck,range):
    '''
    validates user input
    :param tocheck: the value to validate
    :param range: a numeric range in which the valuse must fall
    :return: True if validated, False if not.
    '''
    # TODO we also need to reject non-integers
    if tocheck.isnumeric():
        return int(tocheck) in range
    return False

def get_search_term():
    '''
    this solicits user input for a search string.
    :return: the search string to be used in the spotify API call
    '''
    while True:

        # if the user type "yes" then do this
        display_artist_input()
        text_result = input()
        if text_result:
            what_to_find = text_result
            break

        # Getting the voice recognition words and save in a variable
        # uses google voice API behind the scenes
        voice_word = voice_input()
        if voice_word:
            what_to_find = voice_word
            break

        else:
            continue

    return what_to_find
# end get_search_term

def get_search_type():
    '''
    solicits user input on a search type to use: in artist name field, in album title field, in track title field,
    or just a general text search
    :return: a global variable that stores a string indicating a particular search type
    '''
    display_options_menu()

    while True:
        # keep soliciting input until a valid option is chosen.
        choice = 0
        try:
            choice = int(input())
        except ValueError:
            display_error()
        if choice == 1:
            return None
        elif choice == 2:
            return BY_ARTIST
        elif choice == 3:
            return BY_ALBUM
        elif choice == 4:
            return BY_TRACK_TITLE


# end get_search_type

def get_user_selection(track_list):
    '''
    This presents users with a list of track so user can pick which album to work with
    :param track_list: an array of tracks the user will choose from
    :return: a model.music_result object or other array element
    '''
    track_count = len(track_list)
    for i in range(track_count):
        print (str(i) + " " + str(track_list[i]))
    display_track_import()
    user_choice = str(input())
    # there has to be a way to combine these into a single while statement, but I couldn't figure that out.
    if user_choice.upper() == 'EXIT':
        return None
    else:
        while not isValidTrackChoice(user_choice,range(0,track_count)):
            display_error_2()
            user_choice = input()
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
    display_initial_message()

    while True:

        #Getting user decision to start or quit the program then print the table


        display_music_query()
        user_choice = str(input())

        if user_choice.upper() == "YES":
            # get the search string for Spotify
            what_to_find = get_search_term()
            # also get the search type
            field_to_search = get_search_type()

            # Pass the user parameter as argument to spotify method
            # from api_setup.py file and return values
            # find matches based on user input
            tracks_found = search_tracks(what_to_find,field_to_search)
            # check that there are results, else report none found and loop back to beginning
            if not (len(tracks_found) > 0):
                print("No results found. Please try again.\n")
                continue

            # create a music_result object from the data
            my_song = get_user_selection(tracks_found)

            # Here is some exception handling that check for the Spotify api result
            # then tell us if the result was found
            #then push it to the database
            add_to_database(db, my_song)
        # Quit the program if the user input anything but "yes"
        #then print the database "music_info.db

        elif user_choice.upper() == "NO":
            # if the user typed in anything other than "yes", break out of the while loop and exit the program.
            break
        else:
            display_error()

    result = db.display_info()
    print("Here is your database copy\n")
    print("%2s%60s%60s%60s\n" % ("ID", "TITLE", "ARTIST", "ALBUM_NAME"))
    for music in result:
        print("%2d%60s%60s%60s" % (music.id, music.title, music.artist, music.album))


'''
This is where the code acutally executes.
'''
main()