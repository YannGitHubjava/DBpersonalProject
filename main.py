from databaseDesign import DatabaseManager
from api_setup import *

'''Music search history that saving everything in table called myPlaylist to create music_info.db file,
    that pulls data from the Spotify API
    '''

def main():
    # Setting up database and give it the name "music_info"

    db = DatabaseManager("music_info")
    db.setup_db()
    while True:

        #Getting user decision to start or quit the program then print the table

        user_choice = str(input("Do you want to enter data in music table: "))

        if user_choice.upper() == "YES":

            #if the user type "yes" then do this

            search_result = input("enter the artist name:")

            # Pass the user parameter as argument to spotify method
            # from api_setup.py file and return values

            title = search_track(search_result)
            artist = search_artist(search_result)
            album = search_album(search_result)
            id = None

            # Here is some exception handling that check for the Spotify api result
            # then tell us if the result was found
            #then push it to the database
            try:
                print("the music result: " + str(id) + title + artist + album)
                db.populate_database(id, title, artist, album)
                print("data successfully input")

            #if the result wasn't find
            #or the can't be pushed for some reason
            #print an error message
            except Exception:
                print("No result for this Search. Try again.\n" +
                      "Failed to input in music database")


        # Quit the program if the user input anything but "yes"
        #then print the database "music_info.db

        else:
            break
    result = db.display_info()
    print("Here is your database copy")
    for music in result:
        print(str(music.id) + "  " + "  " + music.title + "  " + music.artist + "      " + music.album)

main()