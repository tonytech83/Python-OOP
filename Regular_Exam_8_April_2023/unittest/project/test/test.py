from project.tennis_player import TennisPlayer

from unittest import TestCase, main


class TennisPlayerTests(TestCase):

    def setUp(self) -> None:
        self.tp = TennisPlayer("Ivan", 26, 12.3)
        self.other_tp = TennisPlayer("Stoqn", 26, 12.5)

    def test_constructor(self):
        name = "Ivan"
        age = 26
        points = 12.3

        tp = TennisPlayer(name, age, points)

        self.assertEqual(name, tp.name)
        self.assertEqual(age, tp.age)
        self.assertEqual(points, tp.points)
        self.assertEqual([], tp.wins)

    def test_name_setter_when_value_under_two_symbols_raises(self):
        with self.assertRaises(ValueError) as er:
            self.tp.name = "A"

        self.assertEqual("Name should be more than 2 symbols!", str(er.exception))

    def test_name_setter_when_value_exactly_two_symbols_raises(self):
        with self.assertRaises(ValueError) as er:
            self.tp.name = "aa"

        self.assertEqual("Name should be more than 2 symbols!", str(er.exception))

    def test_name_setter_with_valid_data(self):
        self.assertEqual('Ivan', self.tp.name)

        self.tp.name = 'Stoqn'

        self.assertEqual('Stoqn', self.tp.name)

    def test_age_setter_when_value_under_eighteen_raises(self):
        with self.assertRaises(ValueError) as er:
            self.tp.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(er.exception))

    def test_age_setter_with_valid_data(self):
        self.assertEqual(26, self.tp.age)

        self.tp.age = 18

        self.assertEqual(18, self.tp.age)

    def test_add_new_win_method(self):
        self.assertEqual([], self.tp.wins)

        self.tp.add_new_win('A')
        self.assertEqual(['A'], self.tp.wins)

        self.tp.add_new_win('B')
        actual_return = self.tp.add_new_win('A')

        self.assertEqual("A has been already added to the list of wins!", actual_return)
        self.assertEqual(['A', 'B'], self.tp.wins)

    def test_lt_dunder(self):
        actual_result = self.tp < self.other_tp
        expected_result = "Stoqn is a top seeded player and he/she is better than Ivan"

        self.assertEqual(expected_result, actual_result)

        self.tp.points = 12.5
        actual_result = self.tp < self.other_tp
        expected_result = "Ivan is a better player than Stoqn"

        self.assertEqual(expected_result, actual_result)

        self.tp.points = 14.5
        actual_result = self.tp < self.other_tp
        expected_result = "Ivan is a better player than Stoqn"

        self.assertEqual(expected_result, actual_result)

    def test_str_dunder(self):
        self.tp.add_new_win('A')
        self.tp.add_new_win('BlaBla')

        actual_return = self.tp.__str__()
        expected_return = f"Tennis Player: Ivan\n" \
                          f"Age: 26\n" \
                          f"Points: 12.3\n" \
                          f"Tournaments won: A, BlaBla"

        self.assertEqual(expected_return, actual_return)


if __name__ == '__main__':
    main()
