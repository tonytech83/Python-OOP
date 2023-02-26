# Exam: 03. Players and Monsters
# From: Inheritance - Exercise
# URL: https://judge.softuni.org/Contests/Compete/Index/1941#2

from project.elf import Elf
from project.hero import Hero

# Test code
hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)

