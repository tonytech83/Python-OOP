from typing import List

from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: List[Customer] = []
        self.trainers: List[Trainer] = []
        self.equipment: List[Equipment] = []
        self.plans: List[ExercisePlan] = []
        self.subscriptions: List[Subscription] = []

    def add_customer(self, customer: Customer):
        new_customer = self.__find_object_by_id(self.customers, customer.id)

        if new_customer is None:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        new_trainer = self.__find_object_by_id(self.trainers, trainer.id)

        if new_trainer is None:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        new_equipment = self.__find_object_by_id(self.equipment, equipment.id)

        if new_equipment is None:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        new_plan = self.__find_object_by_id(self.plans, plan.id)

        if new_plan is None:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        new_subscription = self.__find_object_by_id(self.subscriptions, subscription.id)

        if new_subscription is None:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = self.__find_object_by_id(self.subscriptions, subscription_id)
        customer = self.__find_object_by_id(self.customers, subscription.customer_id)
        trainer = self.__find_object_by_id(self.trainers, subscription.trainer_id)
        plan = self.__find_object_by_id(self.plans, subscription.exercise_id)
        equipment = self.__find_object_by_id(self.equipment, plan.equipment_id)

        return repr(subscription) + '\n' + \
            repr(customer) + '\n' + \
            repr(trainer) + '\n' + \
            repr(equipment) + '\n' + \
            repr(plan)

    @staticmethod
    def __find_object_by_id(collection, id):
        try:
            return [x for x in collection if x.id == id][0]
        except IndexError:
            return None
