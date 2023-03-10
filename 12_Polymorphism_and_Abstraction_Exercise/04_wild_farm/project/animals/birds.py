from project.animals.animal import Bird


class Owl(Bird):
    ALLOWED_FOODS = ['Meat']
    WEIGHT_INCREASE = 0.25

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Hoot Hoot'


class Hen(Bird):
    ALLOWED_FOODS = ['Vegetable', 'Fruit', 'Meat', 'Seed']
    WEIGHT_INCREASE = 0.35

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Cluck'
