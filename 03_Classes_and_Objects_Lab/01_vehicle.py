# Exam: 01. Vehicle
# From: Classes and Objects - Lab
# URL: https://judge.softuni.org/Contests/Practice/Index/1936#0

from typing import List


class Vehicle:
    def __init__(self, mileage: int, max_speed=150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets: List[str] = []


# Test code
car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)
