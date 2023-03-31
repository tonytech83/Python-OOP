from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    @property
    def valid_horse_types(self):
        return {
            "Appaloosa": Appaloosa,
            "Thoroughbred": Thoroughbred
        }

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.valid_horse_types:
            return

        if self.__find_horse_by_name(horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")

        new_horse = self.valid_horse_types[horse_type](horse_name, horse_speed)
        self.horses.append(new_horse)

        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        if self.__find_jockey_by_name(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)

        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if self.__find_race_by_type(race_type):
            raise Exception(f"Race {race_type} has been already created!")

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)

        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.__find_jockey_by_name(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horses_by_type = self.__find_horse_by_type(horse_type)
        try:
            horse = [h for h in horses_by_type if h.is_taken is False][-1]
        except IndexError:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        horse.is_taken = True
        jockey.horse = horse

        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.__find_race_by_type(race_type)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self.__find_jockey_by_name(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if self.__find_jockey_name_in_race(jockey, race):
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)

        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self.__find_race_by_type(race_type)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        highest_speed = max([j.horse.speed for j in race.jockeys])
        winner = [j for j in race.jockeys if j.horse.speed == highest_speed][0]
        horse = [j.horse for j in race.jockeys if j.horse.speed == highest_speed][0]

        return f"The winner of the {race_type} race," \
               f" with a speed of {highest_speed}km/h is {winner.name}!" \
               f" Winner's horse: {horse.name}."

    @staticmethod
    def __find_jockey_name_in_race(jockey, race):
        for race_jockey in race.jockeys:
            if race_jockey.name == jockey.name:
                return True

        return False

    def __find_horse_by_type(self, horse_type):
        return [h for h in self.horses if h.__class__.__name__ == horse_type]

    def __find_race_by_type(self, race_type):
        return next((r for r in self.horse_races if r.race_type == race_type), False)

    def __find_jockey_by_name(self, jockey_name):
        return next((j for j in self.jockeys if j.name == jockey_name), False)

    def __find_horse_by_name(self, horse_name):
        return next((h for h in self.horses if h.name == horse_name), False)
