from project.car.car import Car


class MuscleCar(Car):

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)

    @property
    def type_speed_limit_range(self):
        return range(250, 451)


# print(MuscleCar('Audi', 250))
