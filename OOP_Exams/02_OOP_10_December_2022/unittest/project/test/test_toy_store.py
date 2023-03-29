from unittest import TestCase, main

from project.toy_store import ToyStore


class ToyStoreTests(TestCase):

    def setUp(self) -> None:
        self.store = ToyStore()

    def test_constructor(self):
        store = ToyStore()

        self.assertEqual(dict, type(store.toy_shelf))

    # add_toy method tests

    def test_add_toy_when_shelf_in_not_valid_raises(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy('Z', 'baer')

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_when_shelf_already_has_toy_with_same_name_raises(self):
        self.store.add_toy('G', 'bear')

        with self.assertRaises(Exception) as ex:
            self.store.add_toy('G', 'bear')

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_when_shelf_already_taken_raises(self):
        self.store.add_toy('G', 'bear')

        with self.assertRaises(Exception) as ex:
            self.store.add_toy('G', 'kitty')

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_when_shelf_empty(self):
        return_result = self.store.add_toy('G', 'bear')

        expected_result = 'bear'
        actual_result = self.store.toy_shelf['G']

        self.assertEqual(expected_result, actual_result)
        self.assertEqual("Toy:bear placed successfully!", return_result)

    # remove_toy method tests

    def test_remove_toy_when_shelf_in_not_valid_raises(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('Z', 'bear')

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_when_toy_name_on_shelf_is_different_from_received_raises(self):
        self.store.add_toy('A', 'bear')

        with self.assertRaises(Exception) as ex:
            self.store.remove_toy('A', 'kitty')

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_when_toy_name_is_on_shelf(self):
        self.store.add_toy('A', 'bear')
        return_result = self.store.remove_toy('A', 'bear')

        expected_result = None
        actual_result = self.store.toy_shelf['A']

        self.assertEqual(expected_result, actual_result)
        self.assertEqual("Remove toy:bear successfully!", return_result)


if __name__ == '__main__':
    main()
