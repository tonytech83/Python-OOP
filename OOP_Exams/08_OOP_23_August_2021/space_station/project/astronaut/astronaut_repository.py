from typing import List

from project.astronaut.astronaut import Astronaut


class AstronautRepository:

    def __init__(self):
        self.astronauts: List[Astronaut] = []

    def add(self, astronaut: Astronaut):
        if astronaut not in self.astronauts:
            self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        if astronaut in self.astronauts:
            self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        return next((a for a in self.astronauts if a.name == name), None)
