from unittest import TestCase, main

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar("model", "type", 101, 12.99)

    def test_constructor(self):
        model = "model"
        car_type = "type"
        mileage = 101
        price = 12.99

        car = SecondHandCar(model, car_type, mileage, price)

        self.assertEqual(model, car.model)
        self.assertEqual(car_type, car.car_type)
        self.assertEqual(mileage, car.mileage)
        self.assertEqual(price, car.price)
        self.assertEqual([], car.repairs)

    def test_price_not_valid_raises(self):
        with self.assertRaises(ValueError) as err:
            self.car.price = 1

        self.assertEqual("Price should be greater than 1.0!", str(err.exception))

    def test_mileage_not_valid_raises(self):
        with self.assertRaises(ValueError) as err:
            self.car.mileage = 100

        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(err.exception))

    def test_promotional_price_not_valid_raises(self):
        with self.assertRaises(ValueError) as err:
            self.car.set_promotional_price(12.99)

        self.assertEqual("You are supposed to decrease the price!", str(err.exception))

        with self.assertRaises(ValueError) as err:
            self.car.set_promotional_price(13)

        self.assertEqual("You are supposed to decrease the price!", str(err.exception))

    def test_promotional_price_with_valid_price(self):
        result = self.car.set_promotional_price(1.01)

        self.assertEqual("The promotional price has been successfully set.", result)
        self.assertEqual(1.01, self.car.price)

    def test_need_repair_more_then_half_car_price_raises(self):
        self.car.price = 2
        repair_price, repair_description = 1.01, 'Pump'
        result = self.car.need_repair(repair_price, repair_description)

        self.assertEqual("Repair is impossible!", result)
        self.assertEqual(2, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_need_repair_when_equal_to_half_car_price(self):
        self.car.price = 2.0
        repair_price, repair_description = 1, 'Pump'
        result = self.car.need_repair(repair_price, repair_description)

        self.assertEqual("Price has been increased due to repair charges.", result)
        self.assertEqual(3.0, self.car.price)
        self.assertEqual(['Pump'], self.car.repairs)

    def test_need_repair_when_less_than_half_car_price(self):
        repair_price, repair_description = 6.49, 'Pump'
        result = self.car.need_repair(repair_price, repair_description)

        self.assertEqual("Price has been increased due to repair charges.", result)
        self.assertEqual(19.48, self.car.price)
        self.assertEqual(['Pump'], self.car.repairs)

        repair_price, repair_description = 9.74, 'Engine'
        result = self.car.need_repair(repair_price, repair_description)

        self.assertEqual("Price has been increased due to repair charges.", result)
        self.assertEqual(29.22, self.car.price)
        self.assertEqual(['Pump', 'Engine'], self.car.repairs)

    def test__gt__type_missmatch_raises(self):
        other_car = SecondHandCar("Mazda", "Sedan", 101, 101)

        result = self.car > other_car

        self.assertEqual("Cars cannot be compared. Type mismatch!", result)

    def test__gt__same_type_price_compair(self):
        other_car = SecondHandCar("Mazda", "type", 101, 101)

        self.assertFalse(self.car > other_car)
        self.assertTrue(other_car > self.car)

    def test__str__method(self):
        self.assertEqual("""Model model | Type type | Milage 101km
Current price: 12.99 | Number of Repairs: 0""", str(self.car))

        repair_price, repair_description = 6.49, 'Pump'
        self.car.need_repair(repair_price, repair_description)

        self.assertEqual("""Model model | Type type | Milage 101km
Current price: 19.48 | Number of Repairs: 1""", str(self.car))

        repair_price, repair_description = 9.74, 'Engine'
        self.car.need_repair(repair_price, repair_description)

        self.assertEqual("""Model model | Type type | Milage 101km
Current price: 29.22 | Number of Repairs: 2""", str(self.car))


if __name__ == "__main__":
    main()
