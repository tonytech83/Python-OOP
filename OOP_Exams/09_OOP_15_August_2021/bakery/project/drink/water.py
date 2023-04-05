from project.drink.drink import Drink


class Water(Drink):
    PRICE = 1.50

    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, Water.PRICE, brand)

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {Water.PRICE:.2f}lv"
