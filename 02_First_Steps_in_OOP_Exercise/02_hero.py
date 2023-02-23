# Exam: 02. Hero
# From: First Steps in OOP - Exercise
# URL: https://judge.softuni.org/Contests/Practice/Index/1935#1

class Hero:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, damage: int):
        self.health = max(self.health - damage, 0)

        return f'{self.name} was defeated' if self.health <= 0 else None

    def heal(self, amount: int):
        self.health += amount


# Test code
hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
