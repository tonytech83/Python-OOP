from project.user import User


class Library:
    def __init__(self):
        self.user_records: list = []  # list with objects
        self.books_available: dict = {}  # {author: [books]}
        self.rented_books: dict = {}  # ({usernames: {book names: days to return}})

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        if book_name in self.books_available[author]:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)

            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}

            if book_name not in self.rented_books[user.username]:
                self.rented_books[user.username][book_name] = days_to_return

            return f'{book_name} successfully rented for the next {days_to_return} days!'

        for books in self.rented_books.values():
            for book in books:
                if book_name == book:
                    return f'The book "{book_name}" is already rented and will be available in {books[book]} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in user.books:
            user.books.remove(book_name)
            del self.rented_books[user.username][book_name]
            self.books_available[author].append(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"
