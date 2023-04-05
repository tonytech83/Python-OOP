from abc import ABC, abstractmethod
from typing import List

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):

    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders: List[BakedFood] = []
        self.drink_orders: List[Drink] = []
        self.number_of_people: int = 0
        self.is_reserved: bool = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value: int):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")

        self.__capacity = value

    @property
    @abstractmethod
    def number_range(self):
        pass

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value: int):
        if value not in self.number_range:
            table_type = self.__class__.__name__.replace("Table", "")
            raise ValueError(f"{table_type} table's number must be between"
                             f" {min(self.number_range)} and {max(self.number_range)} inclusive!")

        self.__table_number = value

    @property
    @abstractmethod
    def table_type(self):
        pass

    def reserve(self, number_of_people: int):
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        foods = sum([f.price for f in self.food_orders])
        drinks = sum([d.price for d in self.drink_orders])

        return foods + drinks

    def clear(self):
        bill = self.get_bill()
        self.number_of_people = 0
        self.is_reserved = False
        self.food_orders.clear()
        self.drink_orders.clear()

        return '\n'.join([f"Table: {self.table_number}", f"Bill: {bill:.2f}"])

    def free_table_info(self):
        if not self.is_reserved:
            info = [
                f"Table: {self.table_number}",
                f"Type: {self.table_type}",
                f"Capacity: {self.capacity}"
            ]

            return '\n'.join(info)

    # @staticmethod
    # def ordered_foods_info(data):
    #     ordered_foods = []
    #     for food in data:
    #         ordered_foods.append(repr(food))
    #
    #     return ordered_foods
