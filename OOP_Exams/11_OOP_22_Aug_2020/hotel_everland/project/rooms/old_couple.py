from typing import List

from project.appliances.appliance import Appliance
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):

    def __init__(self, name: str, pension_one: float, pension_two: float):
        super().__init__(name, budget=pension_one + pension_two, members_count=2)
        self.room_cost = 15
        self.appliances: List[Appliance] = [TV(), Fridge(), Stove()] * 2
        self.calculate_expenses(self.appliances)
