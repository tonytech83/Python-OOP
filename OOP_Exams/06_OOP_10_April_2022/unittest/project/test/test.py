from project.movie import Movie
from unittest import TestCase, main


class MovieTests(TestCase):
    def setUp(self) -> None:
        self.movie = Movie('A', 2000, 10)
        self.other_movie = Movie('B', 2000, 9)

    def test_constructor(self):
        name = 'A'
        year = 1888
        rating = 10

        m = Movie(name, year, rating)

        self.assertEqual(name, m.name)
        self.assertEqual(year, m.year)
        self.assertEqual(rating, m.rating)
        self.assertEqual([], m.actors)

    def test_name_setter_with_not_valid_name_raises(self):
        with self.assertRaises(ValueError) as er:
            m = Movie('', 2000, 10)

        self.assertEqual("Name cannot be an empty string!", str(er.exception))

    def test_year_setter_with_not_value_year_raises(self):
        with self.assertRaises(ValueError) as er:
            m = Movie('A', 1886, 10)

        self.assertEqual("Year is not valid!", str(er.exception))

    def test_add_actor_if_name_not_in_actors(self):
        self.assertEqual([], self.movie.actors)

        self.movie.add_actor('Ivan')

        self.assertEqual(['Ivan'], self.movie.actors)

    def test_add_actor_if_name_is_in_actors(self):
        self.movie.add_actor('Ivan')
        self.assertEqual(['Ivan'], self.movie.actors)

        actual_result = self.movie.add_actor('Ivan')

        self.assertEqual("Ivan is already added in the list of actors!", actual_result)
        self.assertEqual(['Ivan'], self.movie.actors)

    def test_gt_dunder_when_self_bigger_than_other_true(self):
        actual_result = self.movie > self.other_movie

        self.assertEqual('"A" is better than "B"', actual_result)

    def test_gt_dunder_when_self_equal_than_other_false(self):
        other_movie = Movie('B', 2000, 10)
        actual_result = self.movie > other_movie

        self.assertEqual('"B" is better than "A"', actual_result)

    def test_gt_dunder_when_self_low_than_other_false(self):
        other_movie = Movie('B', 2000, 11)
        actual_result = self.movie > other_movie

        self.assertEqual('"B" is better than "A"', actual_result)

    def test_repr_method(self):
        expected_result = f"Name: A\n" \
                          f"Year of Release: 2000\n" \
                          f"Rating: 10.00\n" \
                          f"Cast: "

        self.assertEqual(expected_result, repr(self.movie))

        self.movie.add_actor("Ivan")
        self.movie.add_actor('Stoqn')

        expected_result = f"Name: A\n" \
                          f"Year of Release: 2000\n" \
                          f"Rating: 10.00\n" \
                          f"Cast: Ivan, Stoqn"

        self.assertEqual(expected_result, repr(self.movie))


if __name__ == '__main__':
    main()
