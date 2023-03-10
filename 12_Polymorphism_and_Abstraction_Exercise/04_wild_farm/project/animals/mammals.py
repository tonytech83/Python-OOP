from project.animals.animal import Mammal


class Mouse(Mammal):
    ALLOWED_FOODS = ['Vegetable', 'Fruit']
    WEIGHT_INCREASE = 0.1

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Squeak'


class Dog(Mammal):
    ALLOWED_FOODS = ['Meat']
    WEIGHT_INCREASE = 0.4

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Woof!'


class Cat(Mammal):
    ALLOWED_FOODS = ['Meat', 'Vegetable']
    WEIGHT_INCREASE = 0.3

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Meow'


class Tiger(Mammal):
    ALLOWED_FOODS = ['Meat']
    WEIGHT_INCREASE = 1

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'ROAR!!!'
