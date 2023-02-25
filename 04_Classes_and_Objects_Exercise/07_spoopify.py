# Exam: 07. Spoopify
# From: Classes and Objects - Exercise
# URL: https://judge.softuni.org/Contests/Compete/Index/1937#6
from project.band import Band
from project.album import Album
from project.song import Song

# Test code
song = Song("Running in the 90s", 3.45, False)
song_1 = Song("My-ha-ha", 5.02, False)
song_2 = Song('Bla-bla-bla', 4.50, True)

print(song.get_info())
album = Album("Initial D", song, song_1)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(song_2))
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
