# Exam: 03. Circle
# From: Classes and Objects - Lab
# URL: https://judge.softuni.org/Contests/Practice/Index/1936#2

class Circle:
    pi = 3.14

    def __init__(self, radius: int):
        self.radius = radius

    def set_radius(self, new_radius: int):
        self.radius = new_radius

    def get_area(self) -> float:
        return Circle.pi * pow(self.radius, 2)

    def get_circumference(self) -> float:
        return 2 * Circle.pi * self.radius


# Test code
circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())
