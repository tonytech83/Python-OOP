from project.delicacies.delicacy import Delicacy


class Stolen(Delicacy):
    GRAMS = 250

    def __init__(self, name: str, price: float):
        super().__init__(name, Stolen.GRAMS, price)

    @property
    def type_delicacy(self):
        return 'Stolen'
