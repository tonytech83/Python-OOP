from project.car.car import Car


class Driver:

    def __init__(self, name: str):
        self.name = name
        self.car = None
        self.number_of_wins: int = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Name should contain at least one character!")

        self.__name = value

    def change_car(self, new_car: Car):
        old_car_model = self.car.model
        self.car.is_taken = False

        self.car = new_car
        self.car.is_taken = True
        new_car.driver = self

        return f"Driver {self.name} changed his car from {old_car_model} to {new_car.model}."


# d = Driver(' ')
