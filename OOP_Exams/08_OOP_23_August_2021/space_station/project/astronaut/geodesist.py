from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    OXYGEN = 50

    def __init__(self, name: str):
        super().__init__(name, Geodesist.OXYGEN)

    @property
    def breathe_units(self):
        return 10
