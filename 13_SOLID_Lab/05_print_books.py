class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book) -> str:
        return book.content


class Printer:
    def get_book(self, book: Book, formatter):
        return formatter.format(book)


# Sample test code
b = Book('Some content')  # instantiate book with some content
f = Formatter()  # crete instance of formatter

p = Printer()  # create instance of printer

print(p.get_book(b, f))
