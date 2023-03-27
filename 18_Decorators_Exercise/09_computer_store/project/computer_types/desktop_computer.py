from project.computer_types.computer import Computer
from math import sqrt


class DesktopComputer(Computer):
    MAX_RAM = 128

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    @property
    def available_processors(self):
        return {
            "AMD Ryzen 7 5700G": 500,
            "Intel Core i5-12600K": 600,
            "Apple M1 Max": 1800,
        }

    @property
    def ram_sizes(self):
        return {2 ** p: p * 100 for p in range(1, int(sqrt(DesktopComputer.MAX_RAM))) if
                2 ** p <= DesktopComputer.MAX_RAM}

    @property
    def computer_type(self):
        return 'desktop computer'
