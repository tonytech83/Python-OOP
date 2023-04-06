from typing import List

from project.rooms.room import Room


class Everland:

    def __init__(self):
        self.rooms: List[Room] = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = sum([room.expenses + room.room_cost for room in self.rooms])

        return f"Monthly consumptions: {total_consumption:.2f}$."

    def pay(self):
        result_str = []

        for room in self.rooms:
            room_consumption = room.expenses + room.room_cost

            if room_consumption <= room.budget:
                room.budget -= room_consumption
                result_str.append(f"{room.family_name} paid {room_consumption:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                result_str.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)

        return '\n'.join(result_str)

    def status(self):
        all_people_in_the_hotel = sum([r.members_count for r in self.rooms])

        result_str = [f'Total population: {all_people_in_the_hotel}']
        for room in self.rooms:
            result_str.append(room.room_info())

        return '\n'.join(result_str)
