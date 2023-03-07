# Exam: 01. Vehicles
# From: Polymorphism and Abstraction - Exercise
# https: https://judge.softuni.org/Contests/Compete/Index/1943#0

from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

    @staticmethod
    def _is_drive_possible(air_conditioner, fuel_quantity, fuel_consumption, distance) -> float:
        possible_distance = fuel_quantity / (fuel_consumption + air_conditioner)
        if possible_distance >= distance:
            fuel_quantity -= distance * (fuel_consumption + air_conditioner)

        return fuel_quantity


class Car(Vehicle):
    AIR_CONDITIONER_CONSUMPTION = 0.9

    def drive(self, distance):
        self.fuel_quantity = self._is_drive_possible(
            Car.AIR_CONDITIONER_CONSUMPTION,
            self.fuel_quantity,
            self.fuel_consumption,
            distance
        )

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AIR_CONDITIONER_CONSUMPTION = 1.6

    def drive(self, distance):
        self.fuel_quantity = self._is_drive_possible(
            Truck.AIR_CONDITIONER_CONSUMPTION,
            self.fuel_quantity,
            self.fuel_consumption,
            distance
        )

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


# Test code 1
car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

# Test code 2
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
