from typing import List

from project.meals.meal import Meal


class Client:

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart: List[Meal] = []
        self.bill: float = 0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if not all([
            int(value[0]) == 0,
            len(value) == 10,
            self.__is_phone_contains_only_numbers(value)
        ]):
            raise ValueError("Invalid phone number!")

        self.__phone_number = value

    @staticmethod
    def __is_phone_contains_only_numbers(number):
        try:
            for ch in number:
                n = int(ch)
            return True
        except ValueError:
            return False

    def clean_shopping_card(self):
        self.shopping_cart = []

    def reset_bill(self):
        self.bill = 0
