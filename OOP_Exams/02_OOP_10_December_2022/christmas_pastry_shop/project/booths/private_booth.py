from project.booths.booth import Booth


class PrivateBooth(Booth):

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    @property
    def price_per_person(self):
        return 3.5
