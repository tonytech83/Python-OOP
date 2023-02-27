# Exam: 05. Shop
# From: Inheritance - Exercise
# URL: https://judge.softuni.org/Contests/Compete/Index/1941#4

from project.drink import Drink
from project.food import Food
from project.product_repository import ProductRepository

# Test code
food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)
