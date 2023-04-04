from abc import ABC, abstractmethod

from project.planet.planet import Planet


class Astronaut(ABC):

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")

        self.__name = value

    @property
    @abstractmethod
    def breathe_units(self):
        pass

    def breathe(self):
        self.oxygen -= self.breathe_units

    def increase_oxygen(self, amount: int):
        self.oxygen += amount

    def land_on_planet(self, planet: Planet):
        while self.oxygen > 0 and planet.items:
            item = planet.items.pop()
            self.backpack.append(item)
            self.breathe()

    def info(self):
        backpack = ", ".join(self.backpack) if self.backpack else "none"
        astronaut_info = [
            f'Name: {self.name}',
            f'Oxygen: {self.oxygen}',
            f'Backpack items: {backpack}'

        ]
        return '\n'.join(astronaut_info)
