from abc import ABC, abstractmethod


class Meal(ABC):

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be an empty string!")

        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Invalid price!")

        self.__price = value

    @property
    @abstractmethod
    def meal_type(self):
        ...

    def details(self):
        return f"{self.meal_type} {self.name}: {self.price:.2f}lv/piece"
