from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class ShoppingCartTests(TestCase):

    def setUp(self) -> None:
        self.shopping_cart = ShoppingCart('Shop', 1000)
        self.other_shopping_card = ShoppingCart('NewShop', 1000)
        self.test_shopping_cart = ShoppingCart('Test', 98)

    def test_constructor(self):
        shop_name = "Shop"
        budget = 1000.50
        shopping_cart = ShoppingCart(shop_name, budget)

        self.assertEqual(shop_name, shopping_cart.shop_name)
        self.assertEqual(budget, shopping_cart.budget)
        self.assertEqual({}, shopping_cart.products)

    def test_shop_name_attribute_setter_with_first_lower_letter_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.shop_name = 'shop'

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ex.exception))

    def test_shop_name_attribute_setter_with_number_letter_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.shop_name = 'Shop3'

        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ex.exception))

    def test_add_to_cart_when_product_price_is_more_than_one_hundred_raises(self):
        product_name = 'laptop'
        product_price = 101

        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.add_to_cart(product_name, product_price)

        self.assertEqual("Product laptop cost too much!", str(ex.exception))

    def test_add_to_cart_when_product_price_is_equal_than_one_hundred_raises(self):
        product_name = 'laptop'
        product_price = 100

        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.add_to_cart(product_name, product_price)

        self.assertEqual("Product laptop cost too much!", str(ex.exception))

    def test_add_to_cart_when_product_price_is_valid(self):
        product_name = 'laptop'
        product_price = 99

        actual_return = self.shopping_cart.add_to_cart(product_name, product_price)
        expected_result = {'laptop': 99}

        self.assertEqual(expected_result, self.shopping_cart.products)
        self.assertEqual("laptop product was successfully added to the cart!", actual_return)

    def test_remove_from_cart_with_not_valid_product_name_raises(self):
        self.shopping_cart.add_to_cart('laptop', 99)
        self.shopping_cart.add_to_cart('keyboard', 99)

        with self.assertRaises(ValueError) as ex:
            self.shopping_cart.remove_from_cart('monitor')

        self.assertEqual("No product with name monitor in the cart!", str(ex.exception))

    def test_remove_from_cart_with_valid_product_name_(self):
        self.shopping_cart.add_to_cart('laptop', 99)
        self.shopping_cart.add_to_cart('keyboard', 99)

        actual_return = self.shopping_cart.remove_from_cart('laptop')
        expected_return = "Product laptop was successfully removed from the cart!"

        self.assertEqual(expected_return, actual_return)
        self.assertEqual({'keyboard': 99}, self.shopping_cart.products)

    def test_add_dunder_method_(self):
        self.shopping_cart.add_to_cart('laptop', 99)
        self.other_shopping_card.add_to_cart('keyboard', 99)
        new_shopping_cart = self.shopping_cart.__add__(self.other_shopping_card)

        self.assertEqual('ShopNewShop', new_shopping_cart.shop_name)
        self.assertEqual(2000, new_shopping_cart.budget)
        self.assertEqual({'laptop': 99, 'keyboard': 99}, new_shopping_cart.products)

    def test_buy_products_when_total_is_bigger_than_budget_raises(self):
        self.test_shopping_cart.add_to_cart('laptop', 99)
        with self.assertRaises(ValueError) as err:
            self.test_shopping_cart.buy_products()

        self.assertEqual("Not enough money to buy the products! Over budget with 1.00lv!", str(err.exception))

    def test_buy_products_with_valid_total(self):
        self.test_shopping_cart.add_to_cart('laptop', 49)
        self.test_shopping_cart.add_to_cart('keyboard', 49)

        expected_return = 'Products were successfully bought! Total cost: 98.00lv.'
        actual_return = self.test_shopping_cart.buy_products()

        self.assertEqual(expected_return, actual_return)


if __name__ == '__main__':
    main()
