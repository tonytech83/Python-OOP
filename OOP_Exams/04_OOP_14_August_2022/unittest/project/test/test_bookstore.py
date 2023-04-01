from project.bookstore import Bookstore

from unittest import TestCase, main


class BookstoreTests(TestCase):

    def setUp(self) -> None:
        self.b = Bookstore(10)

    def test_init(self):
        b = Bookstore(10)

        self.assertEqual(10, b.books_limit)
        self.assertEqual({}, b.availability_in_store_by_book_titles)
        self.assertEqual(0, b.total_sold_books)

    def test_books_limit_setter_with_negative_raises(self):
        with self.assertRaises(ValueError) as er:
            b = Bookstore(-1)

        self.assertEqual("Books limit of -1 is not valid", str(er.exception))

    def test_books_limit_setter_with_zero_raises(self):
        with self.assertRaises(ValueError) as er:
            b = Bookstore(0)

        self.assertEqual("Books limit of 0 is not valid", str(er.exception))

    def test_receive_book_when_books_limit_exceeded_raises(self):
        self.b.receive_book('Book', 5)

        with self.assertRaises(Exception) as ex:
            self.b.receive_book('Test Book', 6)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_new_book(self):
        self.b.receive_book('Test Book', 1)
        expected_return = self.b.receive_book('Book', 8)

        self.assertEqual(8, self.b.availability_in_store_by_book_titles['Book'])
        self.assertEqual("8 copies of Book are available in the bookstore.", expected_return)

    def test_receive_book_when_book_already_exists(self):
        self.b.receive_book('Book', 1)
        self.assertEqual(1, self.b.availability_in_store_by_book_titles['Book'])

        expected_result = self.b.receive_book('Book', 1)

        self.assertEqual(2, self.b.availability_in_store_by_book_titles['Book'])
        self.assertEqual("2 copies of Book are available in the bookstore.", expected_result)
        self.assertEqual(2, len(self.b))

    def test_len_dunder(self):
        self.b.receive_book('Book', 2)
        self.b.receive_book('Test book', 2)

        actual_result = self.b.__len__()

        self.assertEqual(4, actual_result)

    def test_sell_book_when_book_not_exists_raises(self):
        self.b.receive_book('Book', 1)

        with self.assertRaises(Exception) as ex:
            self.b.sell_book('Test Book', 1)

        self.assertEqual("Book Test Book doesn't exist!", str(ex.exception))

    def test_sell_book_when_book_quantity_not_enough_raises(self):
        self.b.receive_book('Book', 1)

        with self.assertRaises(Exception) as ex:
            self.b.sell_book('Book', 2)

        self.assertEqual("Book has not enough copies to sell. Left: 1", str(ex.exception))

    def test_sell_book_when_book_and_quantity_are_valid(self):
        self.b.receive_book('Test Book', 1)
        self.b.receive_book('Book', 2)
        actual_return = self.b.sell_book('Book', 1)

        self.assertEqual(2, len(self.b))
        self.assertEqual(1, self.b.total_sold_books)
        self.assertEqual(1, self.b.availability_in_store_by_book_titles['Test Book'])
        self.assertEqual(1, self.b.availability_in_store_by_book_titles['Book'])
        self.assertEqual(1, self.b.total_sold_books)
        self.assertEqual("Sold 1 copies of Book", actual_return)

        self.b.sell_book('Test Book', 1)
        self.b.sell_book('Book', 1)

        self.assertEqual(3, self.b.total_sold_books)
        self.assertEqual(0, len(self.b))

    def test_str_dunder_with_no_books(self):
        self.b.receive_book('Book', 10)
        self.b.sell_book('Book', 10)

        expected_result = "Total sold books: 10\n" \
                          "Current availability: 0\n" \
                          " - Book: 0 copies"

        actual_result = self.b.__str__()

        self.assertEqual(expected_result, actual_result)

    def test_str_dunder_with_books(self):
        self.b.receive_book('Book', 1)
        self.b.receive_book('Test Book', 1)

        expected_result = f"Total sold books: 0\n" \
                          f"Current availability: 2\n" \
                          f" - Book: 1 copies\n" \
                          f" - Test Book: 1 copies"
        actual_result = self.b.__str__()

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
