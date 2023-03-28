from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TruckDriverTests(TestCase):

    def setUp(self) -> None:
        self.driver = TruckDriver('Ivan', 10)

    def test_constructor(self):
        name = 'Ivan'
        money_per_mile = 5.5

        driver = TruckDriver(name, money_per_mile)

        self.assertEqual(name, driver.name)
        self.assertEqual(money_per_mile, driver.money_per_mile)
        self.assertEqual({}, driver.available_cargos)
        self.assertEqual(0, driver.earned_money)
        self.assertEqual(0, driver.miles)

    def test_earned_money_property(self):
        self.driver.earned_money = 1

        expected = 1
        actual = self.driver.earned_money

        self.assertEqual(expected, actual)

    def test_earned_money_setter_with_negative_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.driver.earned_money = -1

        self.assertEqual(f"Ivan went bankrupt.", str(ex.exception))

    def test_earned_money_setter_with_correct_input(self):
        self.driver.earned_money = 1

        self.assertEqual(1, self.driver.earned_money)

    # TESTS for add_cargo_offer method
    def test_bankrupt(self):
        self.driver.money_per_mile = 0.01
        self.driver.add_cargo_offer("California", 2000)

        with self.assertRaises(ValueError) as ve:
            self.driver.drive_best_cargo_offer()

        self.assertEqual(f"{self.driver.name} went bankrupt.", str(ve.exception))

    def test_add_cargo_offer_when_cargo_location_is_already_added_raises(self):
        self.driver.add_cargo_offer('Sofia', 100)

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer('Sofia', 50)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_when_cargo_location_not_in_available_cargos(self):
        location = 'Sofia'
        actual = self.driver.add_cargo_offer(location, 100)

        self.assertEqual(f"Cargo for 100 to {location} was added as an offer.", actual)

    def test_add_cargo_offer_added_location_in_available_cargos(self):
        location = 'Sofia'
        self.driver.add_cargo_offer(location, 100)

        expected_miles = 100
        actual_miles = self.driver.available_cargos['Sofia']

        self.assertEqual({'Sofia': 100}, self.driver.available_cargos)
        self.assertEqual(expected_miles, actual_miles)

    # TESTS for drive_best_cargo_offer method
    def test_drive_best_cargo_offer_when_no_cargos_in_available_cargos_raises(self):
        actual = self.driver.drive_best_cargo_offer()

        self.assertEqual("There are no offers available.", actual)

    def test_drive_best_cargo_offer_when_have_cargo_in_available_cargos(self):
        self.driver.money_per_mile = 1
        self.driver.add_cargo_offer('Varna', 100)
        self.driver.add_cargo_offer('Sofia', 1000)

        actual = self.driver.drive_best_cargo_offer()

        self.assertEqual(f'Ivan is driving 1000 to Sofia.', actual)
        self.assertEqual(1000, self.driver.miles)
        self.assertEqual(875 * 1, self.driver.earned_money)

    # TESTS for check_for_activities method
    def test_check_for_activities_eat_method_call(self):
        self.driver.money_per_mile = 10
        self.driver.add_cargo_offer('Sofia', 250)
        self.driver.drive_best_cargo_offer()

        self.assertEqual(2480, self.driver.earned_money)

    def test_check_for_activities_sleep_method_call(self):
        self.driver.money_per_mile = 10
        self.driver.add_cargo_offer('Sofia', 1000)
        self.driver.drive_best_cargo_offer()

        self.assertEqual(9875, self.driver.earned_money)

    def test_check_for_activities_pump_gas_method_call(self):
        self.driver.money_per_mile = 10
        self.driver.add_cargo_offer('Sofia', 1500)
        self.driver.drive_best_cargo_offer()

        self.assertEqual(14_335, self.driver.earned_money)

    def test__check_for_activities_repair_truck_method_call(self):
        miles = 20_000

        self.driver.money_per_mile = 10
        self.driver.add_cargo_offer('Sofia', miles)
        self.driver.drive_best_cargo_offer()

        expenses = sum([
            (miles // 250) * 20,
            (miles // 1000) * 45,
            (miles // 1500) * 500,
            (miles // 10_000) * 7500
        ])

        expected = miles * 10 - expenses

        self.assertEqual(expected, self.driver.earned_money)

    def test_repr_method(self):
        self.assertEqual('Ivan has 0 miles behind his back.', repr(self.driver))


if __name__ == '__main__':
    main()
