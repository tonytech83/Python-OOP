from project.animal import Animal


class Cheetah(Animal):
    CHEETAH_NEEDS = 60

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, self.CHEETAH_NEEDS)
