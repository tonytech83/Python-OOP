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

    def __init__(self, shapes_data):
        self.shapes = shapes_data

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise TypeError("`shapes` should be of type `list`.")

        self.__shapes = value

    @property
    def total_area(self):
        total = 0

        for shape in self.shapes:
            total += shape.area()

        return total


class TypesInformation:

    def __init__(self, shapes_data):
        self.shapes = shapes_data
        self.shapes_types: dict = {}

    @property
    def shapes_per_type(self):
        for shape in self.shapes:
            if shape.__class__.__name__ not in self.shapes_types:
                self.shapes_types[shape.__class__.__name__] = 0
            self.shapes_types[shape.__class__.__name__] += 1

        return '\n'.join(f'{k} - {v}' for k, v in self.shapes_types.items())


# Test code after
shapes = [Rectangle(1, 6), Triangle(2, 3), Circle(5), Rectangle(2, 4)]
types = TypesInformation(shapes)
calculator = AreaCalculator(shapes)

print(f"You are trying to calculate total area of these shapes:\n{types.shapes_per_type}")
print()
print("The total area is: ", calculator.total_area)
