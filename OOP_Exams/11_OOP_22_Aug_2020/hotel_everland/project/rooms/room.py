from typing import List

from project.appliances.appliance import Appliance
from project.people.child import Child


class Room:

    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children: List[Child] = []
        self.expenses = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")

        self.__expenses = value

    def calculate_expenses(self, *args):
        total_expenses = 0

        for list_obj in args:
            for obj in list_obj:
                if isinstance(obj, Appliance):
                    total_expenses += obj.get_monthly_expense()
                else:
                    total_expenses += obj.cost * 30

        self.expenses = total_expenses

    def room_info(self):
        result_str = [
            f"{self.family_name} with {self.members_count} members."
            f" Budget: {self.budget:.2f}$, Expenses: {self.expenses:.2f}$"]

        for idx, child in enumerate(self.children):
            result_str.append(f"--- Child {idx + 1} monthly cost: {(child.cost * 30):.2f}$")

        if hasattr(self, 'appliances'):
            appliances_monthly_cost = sum([a.get_monthly_expense() for a in self.appliances])
            result_str.append(f"--- Appliances monthly cost: {appliances_monthly_cost:.2f}$")

        return '\n'.join(result_str)
