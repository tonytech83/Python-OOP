# Exam: 01. Test Worker
# From: Testing - Lab
# URL: https://judge.softuni.org/Contests/Practice/Index/1948#0

class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):

    def test_worker_initialized_correct(self):
        # Arrange

        # Act
        worker = Worker('Test', 100, 10)

        # Assert
        self.assertEqual('Test', worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_energy_incremented_after_rest(self):
        # Arrange
        worker = Worker('Test', 100, 10)

        # Act
        worker.rest()

        # Assert
        self.assertEqual(11, worker.energy)

        # Act
        worker.rest()

        # Assert
        self.assertEqual(12, worker.energy)

    def test_worker_work_with_zero_energy_raises(self):
        # Arrange
        worker = Worker('Test', 100, 0)

        # Act, Assert
        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))
        self.assertEqual(0, worker.money)

    def test_worker_work_with_negative_energy_raises(self):
        # Arrange
        worker = Worker('Test', 100, -1)

        # Act, Assert
        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))
        self.assertEqual(0, worker.money)

    def test_worker_money_increases_after_work(self):
        # Arrange
        worker = Worker('Test', 100, 10)
        self.assertEqual(0, worker.money)

        # Act
        worker.work()

        # Assert
        self.assertEqual(100, worker.money)

        # Act
        worker.work()

        # Assert
        self.assertEqual(200, worker.money)

    def test_worker_energy_decreases_after_work(self):
        # Arrange
        worker = Worker('Test', 100, 10)
        self.assertEqual(10, worker.energy)

        # Act
        worker.work()

        # Assert
        self.assertEqual(9, worker.energy)

        # Act
        worker.work()

        # Assert
        self.assertEqual(8, worker.energy)

    def test_get_info(self):
        # Arrange
        worker = Worker('Test', 100, 10)
        expected = 'Test has saved 0 money.'
        result = worker.get_info()

        # Assert
        self.assertEqual(expected, result)

        # Act
        worker.work()
        expected = 'Test has saved 100 money.'
        result = worker.get_info()
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
