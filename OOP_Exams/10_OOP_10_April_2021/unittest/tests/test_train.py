from unittest import TestCase, main

from project.train.train import Train


class TrainTests(TestCase):

    def setUp(self) -> None:
        self.train = Train('A', 10)

    def test_constructor(self):
        name = 'A'
        capacity = 120

        t = Train(name, capacity)

        self.assertEqual(name, t.name)
        self.assertEqual(capacity, t.capacity)
        self.assertEqual([], t.passengers)
        self.assertEqual("Train is full", t.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", t.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", t.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", t.PASSENGER_ADD)
        self.assertEqual("Removed {}", t.PASSENGER_REMOVED)
        self.assertEqual(0, t.ZERO_CAPACITY)

    def test_add_method_when_train_is_full_raises(self):
        for i in range(10):
            self.train.add(f'passenger_{i}')

        with self.assertRaises(ValueError) as er:
            self.train.add('passenger_10')

        self.assertEqual("Train is full", str(er.exception))
        self.assertEqual(10, len(self.train.passengers))

    def test_add_method_when_name_exists_raises(self):
        self.train.add('passenger_1')
        self.assertEqual(['passenger_1'], self.train.passengers)

        with self.assertRaises(ValueError) as er:
            self.train.add('passenger_1')

        self.assertEqual("Passenger passenger_1 Exists", str(er.exception))

    def test_add_method_with_valid_data(self):
        actual_return = self.train.add('passenger_1')

        self.assertEqual(['passenger_1'], self.train.passengers)
        self.assertEqual("Added passenger passenger_1", actual_return)

    def test_remove_method_when_name_missing_raises(self):
        self.train.add('p_1')
        self.assertEqual(['p_1'], self.train.passengers)

        with self.assertRaises(ValueError) as er:
            self.train.remove('p_2')

        self.assertEqual("Passenger Not Found", str(er.exception))

    def test_remove_method_with_valid_data(self):
        self.train.add('p_1')
        self.train.add('p_2')
        self.assertEqual(['p_1', 'p_2'], self.train.passengers)

        actual_return = self.train.remove('p_1')

        self.assertEqual(['p_2'], self.train.passengers)
        self.assertEqual("Removed p_1", actual_return)


if __name__ == '__main__':
    main()
