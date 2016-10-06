from databaseDesign import DatabaseManager
from api_setup import *
from voiceRec import *
from model import *
import pyaudio

'''Music search history that saving everything in table called myPlaylist to create music_info.db file,
    that pulls data from the Spotify API
    '''

def main():
    # Setting up database and give it the name "music_info"

    db = DatabaseManager("music_info")
    db.setup_db()
    while True:

        #Getting user decision to start or quit the program then print the table

        user_choice = str(input("Do you want to enter data in music table: \n"))

        if user_choice.upper() == "YES":

            search_result = ''
            while True:

                # if the user type "yes" then do this
                text_result = input("Type an artist name or press Enter to Skip for Voice Input: \n")
                if text_result:
                    search_result = text_result
                    break

                # Getting the voice recognition words and save in a variable

                voice_word = voice_input()
                if voice_word:
                    search_result = voice_word
                    break

                else:
                    continue


            # Pass the user parameter as argument to spotify method
            # from api_setup.py file and return values

            title = search_track(search_result)
            artist = search_artist(search_result)
            album = search_album(search_result)
            id = None
            # create a music_result object from the data
            my_song = music_result(id,title,artist,album)

            # Here is some exception handling that check for the Spotify api result
            # then tell us if the result was found
            #then push it to the database
            try:
                print("the music result: " + str(my_song))
                db.populate_database(my_song.id, my_song.title, my_song.artist, my_song.album)
                print("data successfully input\n")

            #if the result wasn't find
            #or the can't be pushed for some reason
            #print an error message
            except Exception:
                print("No result for this Search. Try again.\n" +
                      "Failed to input in music database\n")


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