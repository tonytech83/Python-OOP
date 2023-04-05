from typing import List

from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:

    def __init__(self, name: str):
        self.name = name
        self.food_menu: List[BakedFood] = []
        self.drinks_menu: List[Drink] = []
        self.tables_repository: List[Table] = []
        self.total_income: float = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")

        self.__name = value

    @property
    def __valid_food_types(self):
        return {
            "Bread": Bread,
            "Cake": Cake,
        }

    @property
    def __valid_drink_types(self):
        return {
            "Tea": Tea,
            "Water": Water,
        }

    @property
    def __valid_table_types(self):
        return {
            "InsideTable": InsideTable,
            "OutsideTable": OutsideTable,
        }

    def add_food(self, food_type: str, name: str, price: float):
        if food_type in self.__valid_food_types:
            if self.__find_object(name, 'name', self.food_menu):
                raise Exception(f"{food_type} {name} is already in the menu!")

            new_food = self.__valid_food_types[food_type](name, price)
            self.food_menu.append(new_food)

            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if drink_type in self.__valid_drink_types:
            if self.__find_object(name, 'name', self.drinks_menu):
                raise Exception(f"{drink_type} {name} is already in the menu!")

            new_drink = self.__valid_drink_types[drink_type](name, portion, brand)
            self.drinks_menu.append(new_drink)

            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type in self.__valid_table_types:
            if self.__find_object(table_number, 'table_number', self.tables_repository):
                raise Exception(f"Table {table_number} is already in the bakery!")

            new_table = self.__valid_table_types[table_type](table_number, capacity)
            self.tables_repository.append(new_table)

            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table = self.__find_free_table(number_of_people)
        if not table:
            return f"No available table for {number_of_people} people"

        table.reserve(number_of_people)

        return f"Table {table.table_number} has been reserved for {number_of_people} people"

    def order_food(self, table_number: int, *order):
        table = self.__find_object(table_number, 'table_number', self.tables_repository)
        if not table:
            return f"Could not find table {table_number}"

        in_menu = []
        not_in_menu = []

        for food_name in order:
            food = self.__find_object(food_name, 'name', self.food_menu)
            if food:
                table.order_food(food)
                in_menu.append(repr(food))
            else:
                not_in_menu.append(food_name)

        result_str = [f'Table {table.table_number} ordered:']
        result_str.extend(in_menu)
        result_str.append(f"{self.name} does not have in the menu:")
        result_str.extend(not_in_menu)

        return '\n'.join(result_str)

    def order_drink(self, table_number: int, *order):
        table = self.__find_object(table_number, 'table_number', self.tables_repository)
        if not table:
            return f"Could not find table {table_number}"

        in_menu = []
        not_in_menu = []

        for drink_name in order:
            drink = self.__find_object(drink_name, 'name', self.drinks_menu)
            if drink:
                table.order_drink(drink)
                in_menu.append(repr(drink))
            else:
                not_in_menu.append(drink_name)

        result_str = [f'Table {table.table_number} ordered:']
        result_str.extend(in_menu)
        result_str.append(f"{self.name} does not have in the menu:")
        result_str.extend(not_in_menu)

        return '\n'.join(result_str)

    def leave_table(self, table_number: int):
        table = self.__find_object(table_number, 'table_number', self.tables_repository)
        if table:
            self.total_income += table.get_bill()

            return table.clear()

    def get_free_tables_info(self):
        free_tables = []
        for table in filter(lambda x: x.is_reserved is False, self.tables_repository):
            free_tables.append(table.free_table_info())

        return '\n'.join(free_tables)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    @staticmethod
    def __find_object(value, attribute, data):
        for obj in data:
            if getattr(obj, attribute) == value:
                return obj

    def __find_free_table(self, number_of_people):
        for table in self.tables_repository:
            if number_of_people <= table.capacity and not table.is_reserved:
                return table
