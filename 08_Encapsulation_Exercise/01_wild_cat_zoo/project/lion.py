from project.animals.animal import Animal


class Lion(Animal):
    LION_NEEDS = 50

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, self.LION_NEEDS)
