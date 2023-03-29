from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    GRAMS = 200

    def __init__(self, name: str, price: float):
        super().__init__(name, Gingerbread.GRAMS, price)

    @property
    def type_delicacy(self):
        return 'Gingerbread'
