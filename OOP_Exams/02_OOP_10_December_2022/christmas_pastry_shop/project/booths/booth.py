from abc import ABC, abstractmethod
from typing import List
from project.delicacies.delicacy import Delicacy


class Booth(ABC):

    def __init__(self, booth_number: int, capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders: List[Delicacy] = []
        self.price_for_reservation: float = 0
        self.is_reserved: bool = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity cannot be a negative number!")

        self.__capacity = value

    @property
    @abstractmethod
    def price_per_person(self):
        ...

    def reserve(self, number_of_people: int):
        reservation_price = self.price_per_person * number_of_people

        self.price_for_reservation = reservation_price
        self.is_reserved = True

    def release(self):
        self.price_for_reservation = 0
        self.delicacy_orders = []
        self.is_reserved = False
