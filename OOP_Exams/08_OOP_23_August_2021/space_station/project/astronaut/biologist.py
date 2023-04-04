from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    OXYGEN = 70

    def __init__(self, name: str):
        super().__init__(name, Biologist.OXYGEN)

    @property
    def breathe_units(self):
        return 5
