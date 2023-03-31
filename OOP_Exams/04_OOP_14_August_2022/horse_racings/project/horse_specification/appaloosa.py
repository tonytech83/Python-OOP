from project.horse_specification.horse import Horse


class Appaloosa(Horse):

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    @property
    def max_speed(self):
        return 120

    @property
    def increase_max_speed_with(self):
        return 2
