# Exam: 02. Point
# From: Classes and Objects - Lab
# URL: https://judge.softuni.org/Contests/Practice/Index/1936#1

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def set_x(self, new_x: int) -> None:
        self.x = new_x

    def set_y(self, new_y: int) -> None:
        self.y = new_y

    def __str__(self) -> str:
        return f'The point has coordinates ({self.x},{self.y})'


# Test code
p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)
