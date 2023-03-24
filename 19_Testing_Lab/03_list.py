class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class IntegerListTests(TestCase):

    def test_constructor_without_data(self):
        lst = IntegerList()

        self.assertEqual([], lst._IntegerList__data)

    def test_constructor_with_data(self):
        lst = IntegerList(1, 2, 3, 4, 'a', 'b', 2.3)

        self.assertEqual([1, 2, 3, 4], lst._IntegerList__data)

    def test_get_data_method(self):
        lst = IntegerList(5)

        expected = lst._IntegerList__data
        result = lst.get_data()

        self.assertEqual(expected, result)

    def test_add_method_incorrect_data_raises(self):
        lst = IntegerList(1, 2, 3, 4, 'a', 'b')

        with self.assertRaises(ValueError) as ex:
            lst.add('c')
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_add_method_adding_element(self):
        lst = IntegerList(1, 2, 3, 4, 'a', 'b')
        self.assertEqual([1, 2, 3, 4], lst.get_data())

        lst.add(5)

        self.assertEqual([1, 2, 3, 4, 5], lst.get_data())

    def test_add_method_normal_return(self):
        lst = IntegerList(1, 2, 3, 4, 'a', 'b')
        self.assertEqual([1, 2, 3, 4], lst.get_data())

        expected = [1, 2, 3, 4, 1]
        result = lst.add(1)

        self.assertEqual(expected, result)

    def test_remove_index_method_raises(self):
        lst = IntegerList(1, 2, 3)
        self.assertEqual(3, len(lst.get_data()))

        with self.assertRaises(IndexError) as ex:
            lst.remove_index(4)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_remove_index_method_removing_element(self):
        lst = IntegerList(1, 2, 3)
        self.assertEqual(3, len(lst.get_data()))

        lst.remove_index(2)

        self.assertEqual([1, 2], lst.get_data())

    def test_remove_index_normal_return(self):
        lst = IntegerList(1, 2, 3)

        expected = 3
        result = lst.remove_index(2)

        self.assertEqual(expected, result)

    def test_get_method_raises(self):
        lst = IntegerList(1, 2, 3)

        with self.assertRaises(IndexError) as ex:
            lst.get(3)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_get_method_normal_return(self):
        lst = IntegerList(1, 2, 3)

        expected = 2
        result = lst.get(1)

        self.assertEqual(expected, result)

    def test_insert_method_wrong_index_raises(self):
        lst = IntegerList(1, 2, 3)

        with self.assertRaises(IndexError) as ex:
            lst.insert(10, 7)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_insert_method_wrong_type_raises(self):
        lst = IntegerList(1, 2, 3)

        with self.assertRaises(ValueError) as ex:
            lst.insert(2, 'z')
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_insert_method_inserting_element(self):
        lst = IntegerList(1, 2, 3)
        self.assertEqual(3, len(lst.get_data()))

        lst.insert(2, 15)

        self.assertEqual([1, 2, 15, 3], lst.get_data())

    def test_get_biggest_method(self):
        lst = IntegerList(1, 100, 3, -456, 99)

        expected = 100
        result = lst.get_biggest()

        self.assertEqual(expected, result)

    def test_get_index_method(self):
        lst = IntegerList(1, 2, 3)

        expected = 0
        result = lst.get_index(1)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
