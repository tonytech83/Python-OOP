# Exam: 04. Car Manager
# From: Testing - Lab
# URL: https://judge.softuni.org/Contests/Practice/Index/1948#3

class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


car = Car("a", "b", 1, 4)
# car.make = ""
print(car)

from unittest import TestCase, main


class CarTests(TestCase):

    def test_constructor(self):
        test_car = Car('Audi', 'A3', 6.5, 45)

        self.assertEqual('Audi', test_car.make)
        self.assertEqual('A3', test_car.model)
        self.assertEqual(6.5, test_car.fuel_consumption)
        self.assertEqual(45, test_car.fuel_capacity)
        self.assertEqual(0, test_car.fuel_amount)

    def test_make_property(self):
        test_car = Car('Audi', 'A3', 6.5, 45)

        expected = 'Audi'
        result = test_car.make

        self.assertEqual(expected, result)

    def test_make_setter_with_empty_or_null_data_raises(self):
        test_car = Car('Audi', 'A3', 6.5, 45)

        with self.assertRaises(Exception) as ex:
            test_car.make = ''
        self.assertEqual('Make cannot be null or empty!', str(ex.exception))

    def test_make_setter_with_correct_data(self):
        test_car = Car('Audi', 'A3', 6.5, 45)
        self.assertEqual('Audi', test_car.make)

        test_car.make = 'BMW'

        self.assertEqual('BMW', test_car.make)

    def test_model_property(self):
        test_car = Car('Audi', 'A3', 6.5, 45)

        expected = 'A3'
        result = test_car.model

        self.assertEqual(expected, result)

    def test_model_setter_with_empty_or_null_data_raises(self):
        test_car = Car('Audi', 'A3', 6.5, 45)

        with self.assertRaises(Exception) as ex:
            test_car.model = ''

        self.assertEqual('Model cannot be null or empty!', str(ex.exception))

    def test_model_setter_with_correct_data(self):
        test_car = Car('Audi', 'A3', 6.5, 45)
        self.assertEqual('A3', test_car.model)

        test_car.model = 'A8'

        self.assertEqual('A8', test_car.model)

    def test_fuel_consumption_property(self):
        test_car = Car('Audi', 'A3', 6.5, 45)

        expected = 6.5
        result = test_car.fuel_consumption

        self.assertEqual(expected, result)

    def test_fuel_consumption_set_to_zero_raises(self):
        test_car = Car('Audi', 'A3', 6.5, 45)

        with self.assertRaises(Exception) as ex:
            test_car.fuel_consumption = 0

        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

    def test_fuel_consumption_set_to_negative_raises(self):
        test_car = Car('Audi', 'A3', 6.5, 45)

        with self.assertRaises(Exception) as ex:
            test_car.fuel_consumption = -1

        self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

    def test__fuel_consumption_with_correct_data(self):
        test_car = Car('Audi', 'A3', 6.5, 45)

        test_car.fuel_consumption = 0.1

        self.assertEqual(0.1, test_car.fuel_consumption)

    def test_fuel_capacity_property(self):
        test_car = Car('Audi', 'A3', 6.5, 45)

        expected = 45
        result = test_car.fuel_capacity

        self.assertEqual(expected, result)

    def test_fuel_capacity_set_to_zero_raises(self):
        test_car = Car('Audi', 'A3', 6.5, 45)
        self.assertEqual(45, test_car.fuel_capacity)

        with self.assertRaises(Exception) as ex:
            test_car.fuel_capacity = 0

        self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))

    def test_fuel_capacity_set_to_negative_raises(self):
        test_car = Car('Audi', 'A3', 6.5, 45)
        self.assertEqual(45, test_car.fuel_capacity)

        with self.assertRaises(Exception) as ex:
            test_car.fuel_capacity = -1

        self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))

    def test_fuel_amount_property(self):
        test_car = Car('Audi', 'A3', 6.5, 45)

        expected = 40
        test_car.fuel_amount = 40
        result = test_car.fuel_amount

        self.assertEqual(expected, result)

    def test_fuel_amount_set_negative_raises(self):
        test_car = Car('Audi', 'A3', 6.5, 45)

        with self.assertRaises(Exception) as ex:
            test_car.fuel_amount = -1

        self.assertEqual('Fuel amount cannot be negative!', str(ex.exception))

    def test_fuel_amount_with_correct_data(self):
        test_car = Car('Audi', 'A3', 6.5, 45)

        expected = 10
        test_car.fuel_amount = 10
        result = test_car.fuel_amount

        self.assertEqual(expected, result)

    def test_refuel_method_set_zero_fuel_raises(self):
        test_car = Car('Audi', 'A3', 6.5, 45)

        with self.assertRaises(Exception) as ex:
            test_car.refuel(0)

        self.assertEqual('Fuel amount cannot be zero or negative!', str(ex.exception))

    def test_refuel_method_set_negative_fuel_raises(self):
        test_car = Car('Audi', 'A3', 6.5, 45)

        with self.assertRaises(Exception) as ex:
            test_car.refuel(-1)

        self.assertEqual('Fuel amount cannot be zero or negative!', str(ex.exception))

    def test_refuel_method_with_correct_data_less_or_equal_to_tank_capacity(self):
        test_car = Car('Audi', 'A3', 6.5, 45)
        self.assertEqual(45, test_car.fuel_capacity)

        expected = 45
        test_car.refuel(45)

        self.assertEqual(expected, test_car.fuel_amount)

        expected = 10
        test_car.refuel(10)

        self.assertEqual(expected, test_car.fuel_amount)

    def test_refuel_method_with_correct_data_more_than_tank_capacity(self):
        test_car = Car('Audi', 'A3', 6.5, 45)
        self.assertEqual(45, test_car.fuel_capacity)

        expected = 45
        test_car.refuel(70)

        self.assertEqual(expected, test_car.fuel_amount)

    def test_drive_method_with_distance_more_than_fuel_amount_raises(self):
        test_car = Car('Audi', 'A3', 6.5, 45)

        test_car.fuel_amount = 4

        with self.assertRaises(Exception) as ex:
            test_car.drive(120)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_method_with_distance_equal_to_fuel_amount(self):
        test_car = Car('Audi', 'A3', 6.5, 45)

        test_car.fuel_amount = 6.5

        test_car.drive(100)

        self.assertEqual(0, test_car.fuel_amount)

    def test_drive_method_fuel_amount_after_successful_drive(self):
        test_car = Car('Audi', 'A3', 6.5, 45)

        test_car.fuel_amount = 45

        test_car.drive(100)
        expected = 38.5
        result = test_car.fuel_amount

        self.assertEqual(expected, result)

        test_car.drive(100)
        expected = 32
        result = test_car.fuel_amount

        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
