# Exam: 02. Zoo
# From: Inheritance - Exercise
# URL: https://judge.softuni.org/Contests/Compete/Index/1941#0

from project.lizard import Lizard
from project.mammal import Mammal

# Test code
mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)  # provides the name of the inherited class
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.__class__.__mro__)  # provides Method Resolution Order
print(lizard.name)
