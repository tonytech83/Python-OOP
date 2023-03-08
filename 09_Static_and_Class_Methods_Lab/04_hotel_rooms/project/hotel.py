from typing import List
from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []

    @property
    def guests(self) -> int:
        return sum([room.guests for room in self.rooms])

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> str or None:
        return self.__found_room(room_number).take_room(people)

    def free_room(self, room_number: int) -> str or None:
        return self.__found_room(room_number).free_room()

    def __found_room(self, room_number: int) -> Room:
        return [room for room in self.rooms if room.number == room_number][0]

    def status(self) -> str:
        result = f'Hotel {self.name} has {self.guests} total guests\n' \
                 f'Free rooms: {", ".join([str(room.number) for room in self.rooms if not room.is_taken])}\n' \
                 f'Taken rooms: {", ".join([str(room.number) for room in self.rooms if room.is_taken])}'

        return result
