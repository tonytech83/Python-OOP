# Exam: 02. Vehicle
# From: Testing - Exercise
# URL: https://judge.softuni.org/Contests/Compete/Index/1949#1

from unittest import TestCase, main
from project.vehicle import Vehicle


class VehicleTests(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(45, 125)

    def test_class_attribute_default_value(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_vehicle_constructor(self):
        fuel = 100
        horse_power = 150
        vehicle = Vehicle(100, 150)

        self.assertEqual(fuel, vehicle.fuel)
        self.assertEqual(fuel, vehicle.capacity)
        self.assertEqual(horse_power, vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, vehicle.fuel_consumption)

    def test_drive_method_with_insufficient_fuel_for_distance_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(200)

        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_drive_method_with_more_fuel_than_distance(self):
        self.vehicle.drive(20)

        expected = 45 - 20 * 1.25
        actual = self.vehicle.fuel

        self.assertEqual(expected, actual)

    def test_drive_method_with_equal_fuel_as_distance(self):
        distance = 36
        burned_fuel = distance * self.vehicle.fuel_consumption

        expected = self.vehicle.fuel - burned_fuel
        self.vehicle.drive(distance)
        actual = self.vehicle.fuel

        self.assertEqual(expected, actual)

    def test_refuel_method_with_more_fuel_than_capacity_raises(self):
        self.vehicle.drive(20)

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(45)

        self.assertEqual('Too much fuel', str(ex.exception))

    def test_test_refuel_method_with_equal_fuel_than_capacity(self):
        self.vehicle.drive(20)
        self.vehicle.refuel(25)

        self.assertEqual(45, self.vehicle.fuel)

    def test_test_refuel_method_with_less_fuel_than_capacity(self):
        self.vehicle.drive(20)
        self.vehicle.refuel(20)

        self.assertEqual(40, self.vehicle.fuel)

    def test_str_method_proper_output_string(self):
        expected = f"The vehicle has {self.vehicle.horse_power} " \
                   f"horse power with {self.vehicle.fuel}" \
                   f" fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        actual = str(self.vehicle)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
