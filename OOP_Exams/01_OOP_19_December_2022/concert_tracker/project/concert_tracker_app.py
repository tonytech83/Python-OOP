from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    @property
    def valid_musician_types(self):
        return {
            'Guitarist': Guitarist,
            'Drummer': Drummer,
            'Singer': Singer
        }

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.valid_musician_types:
            raise ValueError('Invalid musician type!')

        if self.__find_musician_by_name(name):
            raise Exception(f'{name} is already a musician!')

        new_musician = self.valid_musician_types[musician_type](name, age)
        self.musicians.append(new_musician)

        return f'{name} is now a {musician_type}.'

    def create_band(self, name: str):
        if self.__find_band_by_name(name):
            raise Exception(f'{name} band is already created!')

        new_band = Band(name)
        self.bands.append(new_band)

        return f'{name} was created.'

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self.__find_concert_by_place(place)
        if concert:
            raise Exception(f'{place} is already registered for {concert.genre} concert!')

        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)

        return f'{genre} concert in {place} was added.'

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.__find_musician_by_name(musician_name)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        band = self.__find_band_by_name(band_name)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.add_member(musician)

        return f'{musician_name} was added to {band_name}.'

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.__find_band_by_name(band_name)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        try:
            musician = [m for m in band.members if m.name == musician_name][0]
        except IndexError:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.remove_member(musician)

        return f'{musician_name} was removed from {band_name}.'

    def start_concert(self, concert_place: str, band_name: str):
        band = self.__find_band_by_name(band_name)
        concert, concert_type = self.__check_concert_place(concert_place)

        if not self.__check_band_composition(band.name):
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if not self.__concert_type_play(band_name, concert_type):
            raise Exception(f'The {band_name} band is not ready to play at the concert!')

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f'{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}.'

    @staticmethod
    def rock_concert_needed_skills():
        return {
            'play the drums with drumsticks': 0,
            'sing high pitch notes': 0,
            'play rock': 0
        }

    @staticmethod
    def metal_concert_needed_skills():
        return {
            'play the drums with drumsticks': 0,
            'sing low pitch notes': 0,
            'play metal': 0
        }

    @staticmethod
    def jazz_concert__needed_skills():
        return {
            'play the drums with drum brushes': 0,
            'sing high pitch notes': 0,
            'sing low pitch notes': 0,
            'play jazz': 0
        }

    def __concert_type_play(self, band_name, concert_type):
        band = self.__find_band_by_name(band_name)

        if concert_type == 'Metal':
            skills = self.metal_concert_needed_skills()
        elif concert_type == 'Rock':
            skills = self.rock_concert_needed_skills()
        else:
            skills = self.jazz_concert__needed_skills()

        needed_skills = 0
        for member in band.members:
            for skill in member.skills:
                if skill in skills:
                    needed_skills += 1

        if len(skills) == needed_skills:
            return True

        return False

    def __check_concert_place(self, place):
        return next((c, c.genre) for c in self.concerts if c.place == place)

    def __check_band_composition(self, band_name):
        band = self.__find_band_by_name(band_name)
        composition = set(m.__class__.__name__ for m in band.members)

        if len(composition) > 2:
            return True

        return False

    def __find_concert_by_place(self, place):
        place = [p for p in self.concerts if p.place == place]
        if place:
            return place[0]

        return False

    def __find_band_by_name(self, band_name):
        band = [b for b in self.bands if b.name == band_name]
        if band:
            return band[0]

        return False

    def __find_musician_by_name(self, name):
        musician = [m for m in self.musicians if m.name == name]
        if musician:
            return musician[0]
        return False
