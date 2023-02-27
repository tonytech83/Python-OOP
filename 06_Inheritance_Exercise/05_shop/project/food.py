from project.product import Product


class Food(Product):
    def __init__(self, name: str):
        super().__init__(name, 15)
