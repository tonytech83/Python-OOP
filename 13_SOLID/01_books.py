from typing import List


class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.page: int = 0

    def turn_page(self, page) -> None:
        self.page = page


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def find_book(self, title: str) -> str:
        try:
            book = [b for b in self.books if b.title == title][0]

            return book.title

        except IndexError:
            return 'Book with this title was not found in the library!'
