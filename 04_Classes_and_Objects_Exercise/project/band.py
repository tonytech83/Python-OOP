from project.album import Album


class Band:
    def __init__(self, name: str, ):
        self.name = name
        self.albums: list = []

    def add_album(self, album: Album) -> str:
        for band_album in self.albums:
            if band_album.name == album.name:
                return f'Band {self.name} already has {album.name} in their library.'

        self.albums.append(album)

        return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name: str) -> str:
        for band_album in self.albums:
            if band_album.published:
                return 'Album has been published. It cannot be removed.'

            elif band_album.name == album_name:
                self.albums.remove(band_album)

                return f'Album {album_name} has been removed.'

        return f'Album {album_name} is not found.'

    def details(self) -> str:
        result = f'Band {self.name}\n'
        result += '\n'.join(f'{album.details()}' for album in self.albums)

        return result
