# Exam: 05. Music
# From: First Steps in OOP - Lab
# URL: https://judge.softuni.org/Contests/Practice/Index/1934#4

class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics


# Test code
song = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())
