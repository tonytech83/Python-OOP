# Exam: 01. Photo Album
# From: Static and Class Methods - Exercise
# https://judge.softuni.org/Contests/Compete/Index/2431#0
import math


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: list = self.__init_pages(pages)  # list of lists

    @staticmethod
    def __init_pages(pages):
        return [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        needed_pages = math.ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(needed_pages)

    def add_photo(self, label: str):
        for idx, page in enumerate(self.photos):
            if len(page) == PhotoAlbum.PHOTOS_PER_PAGE:
                continue

            self.photos[idx].append(label)

            return f'{label} photo added successfully on page {idx + 1} slot {len(page)}'

        return 'No more free slots'

    def display(self):
        separator = '-' * 11
        result = [separator]
        for page in self.photos:
            result.append(" ".join([f'[]' for _ in page]))
            result.append(separator)

        return '\n'.join(result)


# Test code:
album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
