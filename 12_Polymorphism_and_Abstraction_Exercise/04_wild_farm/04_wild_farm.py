# Exam: 04. Wild Farm
# From: Polymorphism and Abstraction - Exercise
# https: https://judge.softuni.org/Contests/Compete/Index/1943#3

# Test code 1
from project.animals.birds import Owl, Hen
from project.food import Meat, Vegetable, Fruit

owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)

# Test code 2
hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)
