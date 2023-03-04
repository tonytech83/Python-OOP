from typing import List
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = self.__find_customer_by_id(customer_id)
        dvd = self.__find_dvd_by_id(dvd_id)

        if dvd in customer.rented_dvds:
            return f'{customer.name} has already rented {dvd.name}'

        if dvd.is_rented:
            return 'DVD is already rented'

        if customer.age < dvd.age_restriction:
            return f'{customer.name} should be at least {dvd.age_restriction} to rent this movie'

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)

        return f'{customer.name} has successfully rented {dvd.name}'

    def return_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = self.__find_customer_by_id(customer_id)
        dvd = self.__find_dvd_by_id(dvd_id)

        if dvd not in customer.rented_dvds:
            return f'{customer.name} does not have that DVD'

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False

        return f'{customer.name} has successfully returned {dvd.name}'

    def __find_customer_by_id(self, customer_id):
        return [c for c in self.customers if c.id == customer_id][0]

    def __find_dvd_by_id(self, dvd_id):
        return [d for d in self.dvds if d.id == dvd_id][0]

    def __repr__(self):
        return '\n'.join([repr(x) for x in self.customers]) + '\n' + '\n'.join([repr(x) for x in self.dvds])
