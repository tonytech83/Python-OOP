from project.song import Song


class Album:
    def __init__(self, name: str, *songs_to_add):
        self.name = name
        self.published = False
        self.songs: list = []
        self.init_songs(songs_to_add)

    def add_song(self, song: Song) -> str:
        if self.published:
            return 'Cannot add songs. Album is published.'

        if song.single:
            return f"Cannot add {song.name}. It's a single"

        for album_song in self.songs:
            if album_song.name == song.name:
                return 'Song is already in the album.'

        self.songs.append(song)

        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return 'Cannot remove songs. Album is published.'

        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)

                return f'Removed song {song_name} from album {self.name}.'

        return 'Song is not in the album.'

    def publish(self) -> str:
        if self.published:
            return f'Album {self.name} is already published.'

        self.published = True

        return f'Album {self.name} has been published.'

    def details(self) -> str:
        result = f'Album {self.name}\n'
        result += '\n'.join(f'== {song.get_info()}' for song in self.songs)

        return result

    def init_songs(self, initial_songs) -> None:
        for song in initial_songs:
            self.add_song(song)
