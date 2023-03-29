from abc import ABC, abstractmethod


class Delicacy(ABC):

    def __init__(self, name: str, portion: int, price: float):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be null or whitespace!")

        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price cannot be less or equal to zero!")

        self.__price = value

    @property
    @abstractmethod
    def type_delicacy(self):
        ...

    def details(self):
        return f"{self.type_delicacy} {self.name}: {self.portion}g - {self.price:.2f}lv."
