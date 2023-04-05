from project.drink.drink import Drink


class Tea(Drink):
    PRICE = 2.50

    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, Tea.PRICE, brand)

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {Tea.PRICE:.2f}lv"
