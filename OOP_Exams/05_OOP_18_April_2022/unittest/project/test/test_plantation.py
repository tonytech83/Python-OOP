from project.plantation import Plantation
from unittest import TestCase, main


class PlantationTests(TestCase):
    def setUp(self) -> None:
        self.p = Plantation(10)

    def test_constructor(self):
        self.assertEqual(10, self.p.size)
        self.assertEqual({}, self.p.plants)
        self.assertEqual([], self.p.workers)

    def test_size_setter_with_negative_value_raises(self):
        with self.assertRaises(ValueError) as er:
            Plantation(-1)

        self.assertEqual("Size must be positive number!", str(er.exception))

    def test_hire_worker_with_already_hired_worker(self):
        worker = 'Ivan'
        self.p.hire_worker(worker)
        self.assertEqual('Ivan', self.p.workers[0])

        with self.assertRaises(ValueError) as er:
            self.p.hire_worker('Ivan')

        self.assertEqual("Worker already hired!", str(er.exception))

    def test_hire_worker_which_not_is_in_workers_list(self):
        worker_1 = 'Ivan'
        worker_2 = 'Stoqn'

        self.p.hire_worker(worker_1)
        self.assertEqual(['Ivan'], self.p.workers)
        actual_return = self.p.hire_worker(worker_2)
        self.assertEqual(['Ivan', 'Stoqn'], self.p.workers)
        self.assertEqual(2, len(self.p.workers))
        self.assertEqual("Stoqn successfully hired.", actual_return)

    def test_len_dunder(self):
        self.assertEqual(0, self.p.__len__())

        worker_1 = 'Ivan'
        worker_2 = 'Stoqn'
        plant_1 = 'A'
        plant_2 = 'B'
        plant_3 = 'C'
        plant_4 = 'D'

        self.p.hire_worker(worker_1)
        self.p.hire_worker(worker_2)
        self.p.planting(worker_1, plant_1)
        self.assertEqual(1, self.p.__len__())

        self.p.planting(worker_1, plant_2)
        self.p.planting(worker_2, plant_3)
        self.assertEqual(3, self.p.__len__())

        self.p.planting(worker_2, plant_4)
        self.assertEqual(4, self.p.__len__())

    def test_planting_with_when_worker_not_in_workers_list_raises(self):
        with self.assertRaises(ValueError) as er:
            self.p.planting('Ivan', 'A')

        self.assertEqual("Worker with name Ivan is not hired!", str(er.exception))

        self.p.hire_worker('Stoqn')
        with self.assertRaises(ValueError) as er:
            self.p.planting('Ivan', 'A')

        self.assertEqual("Worker with name Ivan is not hired!", str(er.exception))

    def test_planting_when_quantity_is_equal_to_size_raises(self):
        p = Plantation(1)
        p.hire_worker('Ivan')
        p.planting('Ivan', 'A')
        self.assertEqual(1, len(p))

        with self.assertRaises(ValueError) as er:
            p.planting('Ivan', 'B')

        self.assertEqual("The plantation is full!", str(er.exception))

    def test_planting_when_quantity_is_bigger_than_size_raises(self):
        p = Plantation(2)
        p.hire_worker('Ivan')
        p.planting('Ivan', 'A')
        p.planting('Ivan', 'B')
        p.size = 1

        with self.assertRaises(ValueError) as er:
            p.planting('Ivan', 'C')

        self.assertEqual("The plantation is full!", str(er.exception))

    def test_planting_when_worker_is_in_plants(self):
        self.p.hire_worker('Ivan')
        self.p.planting('Ivan', 'A')
        actual_result = self.p.planting('Ivan', 'B')

        self.assertEqual(['A', 'B'], self.p.plants['Ivan'])
        self.assertEqual("Ivan planted B.", actual_result)

    def test_planting_when_worker_not_in_plants(self):
        self.p.hire_worker('Ivan')
        actual_result = self.p.planting('Ivan', 'A')

        self.assertEqual(['A'], self.p.plants['Ivan'])
        self.assertEqual("Ivan planted it's first A.", actual_result)

    def test_str_dunder(self):
        self.p.hire_worker('Ivan')
        self.p.hire_worker('Stoqn')
        self.p.planting('Ivan', 'A')
        self.p.planting('Ivan', 'B')

        expected_result = '\n'.join([
            "Plantation size: 10",
            'Ivan, Stoqn',
            'Ivan planted: A, B'
        ])

        actual_result = str(self.p)

        self.assertEqual(expected_result, actual_result)

    def test_repr_dunder(self):
        self.p.hire_worker('Ivan')
        self.p.hire_worker('Stoqn')

        expected_result = "Size: 10\nWorkers: Ivan, Stoqn"
        actual_result = repr(self.p)

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()
