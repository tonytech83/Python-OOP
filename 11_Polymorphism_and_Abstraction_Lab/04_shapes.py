# Exam: 04. Shapes
# From: Polymorphism and Abstraction - Lab
# https://judge.softuni.org/Contests/Practice/Index/1942#2

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius: int):
        self._radius = radius

    def calculate_area(self):
        return math.pi * self._radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self._radius


class Rectangle(Shape):
    def __init__(self, height: int, width: int):
        self._height = height
        self._width = width

    def calculate_area(self):
        return self._width * self._height

    def calculate_perimeter(self):
        return 2 * (self._width + self._height)


# Test code 1
circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

# Test code 2
rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
