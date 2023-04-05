from project.pet_shop import PetShop

from unittest import TestCase, main


class PetShopTests(TestCase):
    def setUp(self) -> None:
        self.ps = PetShop('PS')

    def test_constructor(self):
        name = 'PS'

        ps = PetShop(name)

        self.assertEqual(name, ps.name)
        self.assertEqual({}, ps.food)
        self.assertEqual([], ps.pets)

    def test_add_food_with_not_valid_quantity_raises(self):
        expected_result = 'Quantity cannot be equal to or less than 0'

        with self.assertRaises(ValueError) as er:
            self.ps.add_food('food_1', 0)

        self.assertEqual(expected_result, str(er.exception))

        with self.assertRaises(ValueError) as er:
            self.ps.add_food('food_1', -1)

        self.assertEqual(expected_result, str(er.exception))

    def test_add_food_with_valid_quantity(self):
        self.assertEqual({}, self.ps.food)

        actual_return = self.ps.add_food('food_1', 1)

        self.assertEqual({'food_1': 1}, self.ps.food)
        self.assertEqual("Successfully added 1.00 grams of food_1.", actual_return)

        actual_return = self.ps.add_food('food_1', 3)

        self.assertEqual({'food_1': 4}, self.ps.food)
        self.assertEqual("Successfully added 3.00 grams of food_1.", actual_return)

        self.assertEqual({'food_1': 4}, self.ps.food)

    def test_add_pet_when_name_not_exists_raises(self):
        self.ps.add_pet('Rex')
        self.assertEqual(['Rex'], self.ps.pets)

        with self.assertRaises(Exception) as ex:
            self.ps.add_pet('Rex')

        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet(self):
        self.assertEqual([], self.ps.pets)
        actual_return = self.ps.add_pet('Rex')

        self.assertEqual(['Rex'], self.ps.pets)
        self.assertEqual("Successfully added Rex.", actual_return)

    def test_feed_pet_when_pet_name_missing_raises(self):
        self.assertEqual([], self.ps.pets)
        with self.assertRaises(Exception) as ex:
            self.ps.feed_pet('food_1', 'Rex')

        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet(self):
        self.ps.add_pet('Rex')
        self.ps.add_food('food_1', 1)

        expected_return = 'You do not have food_2'
        actual_return = self.ps.feed_pet('food_2', 'Rex')

        self.assertEqual(expected_return, actual_return)

        self.ps.add_food('food_1', 98)

        expected_return = "Adding food..."
        actual_return = self.ps.feed_pet('food_1', 'Rex')

        self.assertEqual(expected_return, actual_return)
        self.assertEqual({'food_1': 1099}, self.ps.food)

        expected_return = "Rex was successfully fed"
        actual_return = self.ps.feed_pet('food_1', 'Rex')

        self.assertEqual(expected_return, actual_return)
        self.assertEqual({'food_1': 999}, self.ps.food)

    def test_repr_dunder(self):
        self.ps.add_pet('Rex')
        self.ps.add_pet('Kotio')

        expected_return = f'Shop PS:\n' \
                          f'Pets: Rex, Kotio'
        actual_return = self.ps.__repr__()

        self.assertEqual(expected_return, actual_return)


if __name__ == '__main__':
    main()
