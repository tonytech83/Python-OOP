# Exam: 01. Mammal
# From: Testing - Exercise
# URL: https://judge.softuni.org/Contests/Compete/Index/1949#0


from project.mammal import Mammal
from unittest import TestCase, main


class MammalTests(TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal('Tom', 'cat', 'meow')

    def test_constructor(self):
        self.assertEqual('Tom', self.mammal.name)
        self.assertEqual('cat', self.mammal.type)
        self.assertEqual('meow', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound_method_returns_proper_string(self):
        expected_result = f'{self.mammal.name} makes {self.mammal.sound}'
        result = self.mammal.make_sound()

        self.assertEqual(expected_result, result)

    def test_get_kingdom_method_returns_proper_string(self):
        expected_result = 'animals'
        result = self.mammal.get_kingdom()

        self.assertEqual(expected_result, result)

    def test_info_method_returns_proper_string(self):
        expected_result = f'{self.mammal.name} is of type {self.mammal.type}'
        result = self.mammal.info()

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
