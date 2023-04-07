from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class PaintFactoryTests(TestCase):

    def setUp(self) -> None:
        self.pf = PaintFactory('PF', 10)

    def test_constructor(self):
        name = 'PF'
        capacity = 10
        valid_ingredients = ["white", "yellow", "blue", "green", "red"]
        ingredients = {}

        pf = PaintFactory(name, capacity)

        self.assertEqual(name, pf.name)
        self.assertEqual(capacity, pf.capacity)
        self.assertEqual(valid_ingredients, pf.valid_ingredients)
        self.assertEqual(ingredients, pf.ingredients)

    def test_add_ingredient_when_not_enough_space_raises(self):
        self.pf.add_ingredient('white', 10)
        self.assertEqual({'white': 10}, self.pf.ingredients)

        with self.assertRaises(ValueError) as er:
            self.pf.add_ingredient('white', 1)

        self.assertEqual("Not enough space in factory", str(er.exception))

    def test_add_ingredient_when_name_is_not_valid_raises(self):
        with self.assertRaises(TypeError) as er:
            self.pf.add_ingredient('blabla', 1)

        self.assertEqual("Ingredient of type blabla not allowed in PaintFactory", str(er.exception))

    def test_add_ingredient(self):
        self.assertEqual({}, self.pf.ingredients)

        self.pf.add_ingredient('blue', 1)
        self.assertEqual({'blue': 1}, self.pf.ingredients)

        self.pf.add_ingredient('blue', 2)
        self.pf.add_ingredient('red', 3)
        self.assertEqual({'blue': 3, 'red': 3}, self.pf.ingredients)

    def test_remove_ingredient_when_ingredient_not_exists_raises(self):
        self.pf.add_ingredient('blue', 1)
        self.assertEqual({'blue': 1}, self.pf.ingredients)

        with self.assertRaises(KeyError) as er:
            self.pf.remove_ingredient('red', 1)

        self.assertEqual("'No such ingredient in the factory'", str(er.exception))

    def test_remove_ingredient_when_quantity_not_valid_raises(self):
        self.pf.add_ingredient('blue', 1)

        with self.assertRaises(ValueError) as er:
            self.pf.remove_ingredient('blue', 2)

        self.assertEqual("Ingredients quantity cannot be less than zero", str(er.exception))

    def test_test_remove_ingredient(self):
        self.pf.add_ingredient('blue', 2)
        self.pf.add_ingredient('red', 2)
        self.assertEqual({'blue': 2, 'red': 2}, self.pf.ingredients)

        self.pf.remove_ingredient('blue', 2)
        self.pf.remove_ingredient('red', 1)

        self.assertEqual({'blue': 0, 'red': 1}, self.pf.ingredients)

    def test_products_property(self):
        self.assertEqual({}, self.pf.products)
        self.pf.add_ingredient('red', 2)

        self.assertEqual({'red': 2}, self.pf.products)


if __name__ == '__main__':
    main()
