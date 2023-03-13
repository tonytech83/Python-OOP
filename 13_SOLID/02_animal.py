from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, species):
        self.species = species

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):

    def make_sound(self):
        return 'meow'


class Dog(Animal):

    def make_sound(self):
        return 'woof-woof'


class Chicken(Animal):

    def make_sound(self):
        return 'cluck-cluck'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Cat('cat'), Dog('dog')]
animal_sound(animals)


# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
