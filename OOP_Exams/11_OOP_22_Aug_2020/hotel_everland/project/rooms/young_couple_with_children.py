from typing import List

from project.appliances.appliance import Appliance
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):

    def __init__(self, name: str, salary_one: float, salary_two: float, *children):
        super().__init__(name, budget=salary_one + salary_two, members_count=(2 + len(children)))
        self.room_cost = 30
        self.children: List[Child] = list(children)
        self.appliances: List[Appliance] = [TV(), Fridge(), Laptop()] * (2 + len(children))
        self.calculate_expenses(self.appliances, self.children)
