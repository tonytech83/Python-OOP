from typing import List


class Vet:
    animals = []
    SPACE = 5

    def __init__(self, name: str):
        self.name = name
        self.animals: List[str] = []

    def register_animal(self, animal_name: str) -> str:
        if Vet.SPACE == len(Vet.animals):
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
        return f'{self.name} has {len(self.animals)} animals. {Vet.SPACE - len(Vet.animals)} space left in clinic'
