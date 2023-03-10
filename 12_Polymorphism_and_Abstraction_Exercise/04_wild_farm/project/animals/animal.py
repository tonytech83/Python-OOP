from abc import ABC, abstractmethod
from project.food import Food


class Animal(ABC):
    ALLOWED_FOODS = []
    WEIGHT_INCREASE = 0

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten: int = 0

    @abstractmethod
    def make_sound(self):
        pass

    def feed(self, food: Food):
        food_type = food.__class__.__name__

        if food_type not in self.ALLOWED_FOODS:
            return f'{self.__class__.__name__} does not eat {food_type}!'

        self.food_eaten += food.quantity
        self.weight += food.quantity * self.WEIGHT_INCREASE


class Bird(Animal, ABC):
    @abstractmethod
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]'


class Mammal(Animal, ABC):
    @abstractmethod
    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]'
