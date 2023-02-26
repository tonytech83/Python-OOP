from project.food import Food


class Fruit(Food):
    def __init__(self, name: str, expiration_date: str):
        super().__init__(expiration_date)
        self.name = name

# ------- Test code -------
# fruit = Fruit('apple', '10-12-2023')
#
# print(fruit.name)
# print(fruit.expiration_date)
