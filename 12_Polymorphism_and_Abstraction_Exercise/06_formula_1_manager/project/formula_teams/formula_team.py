from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    EXPENSES_PER_RACE = 0
    sponsors = {}

    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1000000:
            raise ValueError('F1 is an expensive sport, find more sponsors!')

        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        first_reward = max(
            [self.sponsors['first_sponsor'][p] if race_pos <= p else 0 for p in self.sponsors['first_sponsor']])
        second_reward = max(
            [self.sponsors['second_sponsor'][p] if race_pos <= p else 0 for p in self.sponsors['second_sponsor']])

        revenue = (first_reward + second_reward) - self.EXPENSES_PER_RACE
        self.budget += revenue

        return f'The revenue after the race is {revenue}$. Current budget {self.budget}$'
