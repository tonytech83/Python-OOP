from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals: list = []
        self.workers: list = []

    def add_animal(self, animal: Animal, price: int):
        if self.__budget < price:
            return 'Not enough budget'

        if self.__animal_capacity == len(self.animals):
            return 'Not enough space for animal'

        self.__budget -= price
        self.animals.append(animal)

        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity == len(self.workers):
            return 'Not enough space for worker'

        self.workers.append(worker)

        return f'{worker.name} the {worker.__class__.__name__} hired successfully'

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)

                return f'{worker_name} fired successfully'

        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        needed_money = sum(worker.salary for worker in self.workers)

        if needed_money <= self.__budget:
            self.__budget -= needed_money

            return f'You payed your workers. They are happy. Budget left: {self.__budget}'

        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        needed_money = sum(animal.money_for_care for animal in self.animals)

        if needed_money <= self.__budget:
            self.__budget -= needed_money

            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f'You have {len(self.animals)} animals'

        result += self.__build_str(self.animals, 'Lion')
        result += self.__build_str(self.animals, 'Tiger')
        result += self.__build_str(self.animals, 'Cheetah')

        return result

    def workers_status(self):
        result = f'You have {len(self.workers)} workers'

        result += self.__build_str(self.workers, 'Keeper')
        result += self.__build_str(self.workers, 'Caretaker')
        result += self.__build_str(self.workers, 'Vet')

        return result

    @staticmethod
    def __build_str(entities, item_type: str):
        lts = []

        for entity in entities:
            if entity.__class__.__name__ == item_type:
                lts.append(entity)

        result = f'\n----- {len(lts)} {item_type}s:\n'
        result += '\n'.join(animal.__repr__() for animal in lts)

        return result
