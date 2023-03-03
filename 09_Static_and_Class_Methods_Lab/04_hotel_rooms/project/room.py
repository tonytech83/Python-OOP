class Room:

    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests: int = 0
        self.is_taken: bool = False

    def take_room(self, people: int) -> str or None:
        if not self.is_taken and self.capacity >= people:
            self.guests += people
            self.is_taken = True
            return

        return f'Room number {self.number} cannot be taken'

    def free_room(self) -> str or None:
        if not self.is_taken:
            return f'Room number {self.number} is not taken'

        self.is_taken = False
        self.guests = 0
