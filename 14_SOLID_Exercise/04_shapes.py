import math
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):

    def __init__(self, base, height):
        self.side = base
        self.height = height

    def area(self):
        return (self.height * self.side) / 2


class Circle(Shape):
    PI = math.pi

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * self.radius ** 2


class AreaCalculator:

    def __init__(self, shapes):
        self.shapes = shapes

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        assert isinstance(value, list), "`shapes` should be of type `list`."
        self.__shapes = value

    @property
    def total_area(self):
        total = 0

        for shape in self.shapes:
            total += shape.area()

        return total


# Test code before
shapes = [Rectangle(2, 3), Rectangle(1, 6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)

# Test code after
shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)
