from abc import ABC, abstractmethod


class Horse(ABC):

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")

        self.__name = value

    @property
    @abstractmethod
    def max_speed(self):
        pass

    @property
    @abstractmethod
    def increase_max_speed_with(self):
        pass

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.max_speed:
            raise ValueError("Horse speed is too high!")

        self.__speed = value

    def train(self):
        speed = self.speed + self.increase_max_speed_with

        if speed > self.max_speed:
            self.speed = self.max_speed
        else:
            self.speed += self.increase_max_speed_with
