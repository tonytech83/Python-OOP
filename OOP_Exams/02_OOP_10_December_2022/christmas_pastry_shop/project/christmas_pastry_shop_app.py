from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0

    @property
    def valid_delicacy_types(self):
        return {
            'Gingerbread': Gingerbread,
            'Stolen': Stolen,
        }

    @property
    def valid_booth_types(self):
        return {
            'Open Booth': OpenBooth,
            'Private Booth': PrivateBooth,
        }

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if type_delicacy not in self.valid_delicacy_types:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        if self.__find_delicacy_by_name(name):
            raise Exception(f"{name} already exists!")

        new_delicacy = self.valid_delicacy_types[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        if self.__find_booth_by_number(booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.valid_booth_types:
            raise Exception(f"{type_booth} is not a valid booth!")

        new_booth = self.valid_booth_types[type_booth](booth_number, capacity)
        self.booths.append(new_booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        booth = self.__find_not_reserved_booth_with_enough_capacity(number_of_people)

        if not booth:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)

        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.__find_booth_by_number(booth_number)
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = self.__find_delicacy_by_name(delicacy_name)
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.__find_booth_by_number(booth_number)

        bill = booth.price_for_reservation + sum([x.price for x in booth.delicacy_orders])
        booth.release()
        self.income += bill

        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    def __find_not_reserved_booth_with_enough_capacity(self, number_of_people):
        potential_booths = [b for b in self.booths if b.is_reserved is False]
        for booth in potential_booths:
            if booth.capacity >= number_of_people:
                return booth

        return False

    def __find_booth_by_number(self, number):
        # for booth in self.booths:
        #     if booth.booth_number == number:
        #         return booth
        #
        # return False

        return next((b for b in self.booths if b.booth_number == number), False)

    def __find_delicacy_by_name(self, name):
        # for delicacy in self.delicacies:
        #     if delicacy.name == name:
        #         return delicacy
        #
        # return False

        return next((d for d in self.delicacies if d.name == name), False)
