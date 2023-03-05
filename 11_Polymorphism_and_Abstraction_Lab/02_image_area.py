# Exam: 02. Image Area
# From: Polymorphism and Abstraction - Lab
# https://judge.softuni.org/Contests/Practice/Index/1942#0

class ImageArea:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    # works for 'greater than' and 'less than'
    def __gt__(self, other):
        return self.get_area() > other.get_area()

    # works for 'greater or equal' and 'less or equal'
    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    # works for 'equal' and 'not equal'
    def __eq__(self, other):
        return self.get_area() == other.get_area()


# Test code 1
a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a2)
print(a1 != a3)

# Test code 2
a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 != a2)
print(a1 >= a3)

# Test code 3
a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 <= a2)
print(a1 < a3)
