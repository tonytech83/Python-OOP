from project.robot import Robot

from unittest import TestCase, main


class RobotTests(TestCase):

    def test_constructor(self):
        self.robot = Robot("123", "Military", 10, 120.12)

        self.assertEqual(self.robot.robot_id, "123")
        self.assertEqual(self.robot.category, "Military")
        self.assertEqual(self.robot.available_capacity, 10)
        self.assertEqual(self.robot.price, 120.12)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

    def test_negative_price_raise_error(self):
        with self.assertRaises(ValueError) as err:
            self.robot = Robot("123", "Military", 1, -1)

        self.assertEqual(str(err.exception), "Price cannot be negative!")

    def test_wrong_category_raise_error(self):
        with self.assertRaises(ValueError) as err:
            self.robot = Robot("123", "Something", 10, 120.12)

        self.assertEqual(str(err.exception),
                         "Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'")

    def test_upgrade(self):
        self.robot = Robot("123", "Entertainment", 2, 100)
        result = self.robot.upgrade('part1', 100)
        self.assertEqual(self.robot.hardware_upgrades, ['part1'])
        self.assertEqual(self.robot.price, 250)
        self.assertEqual(result, "Robot 123 was upgraded with part1.")

        self.robot.upgrade('part2', 100)
        self.assertEqual(self.robot.hardware_upgrades, ['part1', 'part2'])
        self.assertEqual(self.robot.price, 400)

    def test_upgrade_with_existing_part(self):
        self.robot = Robot("123", "Entertainment", 2, 100)
        self.robot.upgrade('part1', 100)
        self.assertEqual(self.robot.hardware_upgrades, ['part1'])
        self.assertEqual(self.robot.price, 250)

        result = self.robot.upgrade('part1', 50)
        self.assertEqual(result, "Robot 123 was not upgraded.")
        self.assertEqual(self.robot.hardware_upgrades, ['part1'])
        self.assertEqual(self.robot.price, 250)

    def test_update_to_new_version(self):
        self.robot = Robot("123", "Humanoids", 130, 100)
        self.robot.update(1.01, 100)
        self.assertEqual(self.robot.software_updates, [1.01])
        self.assertEqual(self.robot.available_capacity, 30)

        result = self.robot.update(1.11, 20)
        self.assertEqual(self.robot.software_updates, [1.01, 1.11])
        self.assertEqual(self.robot.available_capacity, 10)
        self.assertEqual(result, "Robot 123 was updated to version 1.11.")

    def test_update_to_same_version(self):
        self.robot = Robot("123", "Humanoids", 130, 100)
        self.robot.update(1.01, 100)
        self.assertEqual(self.robot.software_updates, [1.01])

        result = self.robot.update(1.01, 10)
        self.assertEqual(self.robot.software_updates, [1.01])
        self.assertEqual(self.robot.available_capacity, 30)
        self.assertEqual(result, "Robot 123 was not updated.")

    def test_update_to_lower_version(self):
        self.robot = Robot("123", "Humanoids", 130, 100)
        self.robot.update(1.01, 100)
        self.assertEqual(self.robot.software_updates, [1.01])
        result = self.robot.update(1.00, 100)
        self.assertEqual(self.robot.software_updates, [1.01])
        self.assertEqual(self.robot.available_capacity, 30)
        self.assertEqual(result, "Robot 123 was not updated.")

    def test_robots_price_comparison(self):
        self.robot = Robot("123", "Humanoids", 130, 100)
        self.new_robot = Robot("456", "Military", 100, 99.99)

        result = self.robot > self.new_robot
        self.assertEqual(result, "Robot with ID 123 is more expensive than Robot with ID 456.")

        self.new_robot.price = 101
        result = self.robot > self.new_robot
        self.assertEqual(result, "Robot with ID 123 is cheaper than Robot with ID 456.")

        self.new_robot.price = 100
        result = self.robot > self.new_robot
        self.assertEqual(result, "Robot with ID 123 costs equal to Robot with ID 456.")


if main == "__main__":
    main()
