"""
Creating an object music_result that get a row result from the myPlaylist table
    and return an id, title, artist, and album"""

class music_result:
    def __init__(self,id, title, artist, album):
        self.id = id
        self.title = title
        self.artist = artist
        self.album = album

    def __str__(self):
        idstring = str(self.id)
        if idstring == "None": idstring = "--"
        return idstring + " / " + self.title + " / " + self.artist + " / " + self.album