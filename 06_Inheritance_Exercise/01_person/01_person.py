# Exam: 01. Person
# From: Inheritance - Exercise
# URL: https://judge.softuni.org/Contests/Compete/Index/1941#0

from project.person import Person
from project.child import Child

# Test code
person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(person.name)
print(person.age)
print(child.__class__.__bases__[0].__name__)
