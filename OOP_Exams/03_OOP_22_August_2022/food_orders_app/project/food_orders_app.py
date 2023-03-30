import copy
from typing import List
from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    RECEIPT_ID = 0

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    @property
    def __valid_meals(self):
        return [Starter, MainDish, Dessert]

    def register_client(self, client_phone_number: str):
        if self.__find_client_by_phone_number(client_phone_number):
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__ not in self.__valid_meals:
                continue
            self.menu.append(meal)

    def show_menu(self):
        result = []
        if self.__check_menu_readiness():
            for meal in self.menu:
                result.append(meal.details())

        return '\n'.join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):

        if self.__check_menu_readiness():

            client = self.__find_client_by_phone_number(client_phone_number)
            if not client:
                self.register_client(client_phone_number)
                client = self.__find_client_by_phone_number(client_phone_number)

            missing_name = self.__check_the_meals_names_in_order(**meal_names_and_quantities)
            if missing_name:
                raise Exception(f"{missing_name} is not on the menu!")

            meal_quantity_low = self.__check_the_meals_quantity_in_order(**meal_names_and_quantities)
            if meal_quantity_low:
                raise Exception(f"Not enough quantity of {meal_quantity_low.meal_type}: {meal_quantity_low.name}!")

            self.__make_order(client, **meal_names_and_quantities)
            ordered_meal_names = ', '.join([x.name for x in client.shopping_cart])

            return f"Client {client_phone_number} successfully ordered {ordered_meal_names} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.__find_client_by_phone_number(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        self.__restore_menu_quantities(client)
        client.clean_shopping_card()
        client.reset_bill()

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__find_client_by_phone_number(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        total_paid_money = client.bill
        FoodOrdersApp.RECEIPT_ID += 1
        client.clean_shopping_card()
        client.reset_bill()

        return f"Receipt #{FoodOrdersApp.RECEIPT_ID}" \
               f" with total amount of {total_paid_money:.2f}" \
               f" was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    def __restore_menu_quantities(self, client):
        for client_meal in client.shopping_cart:
            for menu_meal in self.menu:
                if client_meal.name == menu_meal.name:
                    menu_meal.quantity += client_meal.quantity

    def __make_order(self, client, **meal_names_and_quantities):
        for meal_name, quantity in meal_names_and_quantities.items():
            menu_meal = self.__find_meal_by_name(meal_name)
            client_meal = copy.copy(menu_meal)
            menu_meal.quantity -= quantity
            client_meal.quantity = quantity

            client.shopping_cart.append(client_meal)
            client.bill += client_meal.price * quantity

    def __check_the_meals_quantity_in_order(self, **meal_names_and_quantities):
        for meal in self.menu:
            for meal_name, quantity in meal_names_and_quantities.items():
                if meal.name == meal_name and meal.quantity < quantity:
                    return meal

    def __check_the_meals_names_in_order(self, **meal_names_and_quantities):
        for meal_name in meal_names_and_quantities:
            if meal_name not in [x.name for x in self.menu]:
                return meal_name

    def __check_menu_readiness(self):
        if len(self.menu) >= 5:
            return True

        raise Exception("The menu is not ready!")

    def __find_meal_by_name(self, meal_name):
        return [x for x in self.menu if x.name == meal_name][0]

    def __find_client_by_phone_number(self, phone_number):
        return next((x for x in self.clients_list if x.phone_number == phone_number), False)
