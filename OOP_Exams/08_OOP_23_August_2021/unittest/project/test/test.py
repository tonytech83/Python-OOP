from project.library import Library
from unittest import TestCase, main


class LibraryTests(TestCase):

    def setUp(self) -> None:
        self.library = Library('Test')

    def test_constructor(self):
        name = 'Test'

        library = Library(name)

        self.assertEqual(name, library.name)
        self.assertEqual({}, library.books_by_authors)
        self.assertEqual({}, library.readers)

    def test_name_setter_with_not_valid_input_raises(self):
        with self.assertRaises(ValueError) as er:
            self.library.name = ""

        self.assertEqual("Name cannot be empty string!", str(er.exception))

    def test_add_book_method(self):
        self.assertEqual({}, self.library.books_by_authors)

        self.library.add_book('Auth_1', 'Title_1')
        self.assertEqual({'Auth_1': ['Title_1']}, self.library.books_by_authors)

        self.library.add_book('Auth_2', 'Title_3')
        self.assertEqual({'Auth_1': ['Title_1'], 'Auth_2': ['Title_3']}, self.library.books_by_authors)

        self.library.add_book('Auth_1', 'Title_2')
        self.assertEqual({'Auth_1': ['Title_1', 'Title_2'], 'Auth_2': ['Title_3']}, self.library.books_by_authors)

    def test_add_reader_method(self):
        self.assertEqual({}, self.library.readers)

        self.library.add_reader('Ivan')
        self.assertEqual({'Ivan': []}, self.library.readers)

        actual_return = self.library.add_reader('Ivan')
        self.assertEqual("Ivan is already registered in the Test library.", actual_return)
        self.assertEqual({'Ivan': []}, self.library.readers)

    def test_rent_book_method(self):
        reader_name = 'Ivan'
        book_author = 'Author_1'
        book_title = 'Title_1'

        missing_reader_name_return = self.library.rent_book(reader_name, book_author, book_title)
        self.assertEqual("Ivan is not registered in the Test Library.", missing_reader_name_return)

        self.library.add_reader(reader_name)
        missing_book_author_return = self.library.rent_book(reader_name, book_author, book_title)
        self.assertEqual(f"Test Library does not have any {book_author}'s books.", missing_book_author_return)

        self.library.add_book(book_author, book_title)
        missing_book_title_return = self.library.rent_book(reader_name, book_author, 'Title_2')
        self.assertEqual(f"""Test Library does not have {book_author}'s "Title_2".""", missing_book_title_return)

        self.assertEqual({'Ivan': []}, self.library.readers)
        self.library.rent_book(reader_name, book_author, book_title)
        self.assertEqual({'Ivan': [{'Author_1': 'Title_1'}]}, self.library.readers)

        self.assertEqual({'Author_1': []}, self.library.books_by_authors)


if __name__ == '__main__':
    main()
