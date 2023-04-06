from abc import ABC, abstractmethod
from typing import List

from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):

    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations: List[BaseDecoration] = []
        self.fish: List[BaseFish] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")

        self.__name = value

    def calculate_comfort(self):
        return sum([d.comfort for d in self.decorations])

    def add_fish(self, fish: BaseFish):
        if self.capacity <= len(self.fish):
            return "Not enough capacity."

        self.fish.append(fish)

        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish: BaseFish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        fish_names = " ".join([f.name for f in self.fish]) if self.fish else "none"

        result_str = [
            f"{self.name}:",
            f"Fish: {fish_names}",
            f"Decorations: {len(self.decorations)}",
            f"Comfort: {self.calculate_comfort()}"
        ]

        return '\n'.join(result_str)
