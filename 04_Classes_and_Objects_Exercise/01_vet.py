# Exam: 01. Vet
# From: Classes and Objects - Exercise
# URL: https://judge.softuni.org/Contests/Compete/Index/1937#0

from typing import List


class Vet:
    animals = []
    space = 5

    def __init__(self, name: str):
        self.name = name
        self.animals: List[str] = []

    def register_animal(self, animal_name: str) -> str:
        if Vet.space == len(Vet.animals):
            return 'Not enough space'

        Vet.animals.append(animal_name)
        self.animals.append(animal_name)

        return f'{animal_name} registered in the clinic'

    def unregister_animal(self, animal_name: str) -> str:
        if animal_name in self.animals:
            Vet.animals.remove(animal_name)
            self.animals.remove(animal_name)

            return f'{animal_name} unregistered successfully'

        return f'{animal_name} not in the clinic'

    def info(self) -> str:
        return f'{self.name} has {len(self.animals)} animals. {Vet.space - len(Vet.animals)} space left in clinic'


# Test code
peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())

# My test codes
print(peter.animals)
print(george.animals)
print(Vet.animals)
