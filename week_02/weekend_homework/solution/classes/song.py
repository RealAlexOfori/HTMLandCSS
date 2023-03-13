class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def equals(self, squirrel):
        return squirrel.title == self.title and squirrel.artist == self.artist
