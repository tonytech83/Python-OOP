from project.computer_types.computer import Computer
from math import sqrt


class Laptop(Computer):
    MAX_RAM = 64

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    @property
    def available_processors(self):
        return {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200,
        }

    @property
    def ram_sizes(self):
        return {2 ** p: p * 100 for p in range(1, int(sqrt(Laptop.MAX_RAM))) if 2 ** p <= Laptop.MAX_RAM}

    @property
    def computer_type(self):
        return 'laptop'
