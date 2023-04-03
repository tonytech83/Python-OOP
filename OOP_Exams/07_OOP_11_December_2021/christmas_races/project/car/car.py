from abc import ABC, abstractmethod


class Car(ABC):

    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken: bool = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value: str):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")

        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value: int):
        if value not in self.type_speed_limit_range:
            raise ValueError(
                f"Invalid speed limit! Must be between {min(self.type_speed_limit_range)}"
                f" and {max(self.type_speed_limit_range)}!")

        self.__speed_limit = value

    @property
    @abstractmethod
    def type_speed_limit_range(self):
        pass

    def __str__(self):
        return f"{self.model} -> {self.speed_limit}"
