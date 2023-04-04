from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    OXYGEN = 90

    def __init__(self, name: str):
        super().__init__(name, Meteorologist.OXYGEN)

    @property
    def breathe_units(self):
        return 15
