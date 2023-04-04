from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.completed_missions: int = 0
        self.not_completed_missions: int = 0

    @property
    def valid_astronaut_types(self):
        return {
            'Biologist': Biologist,
            'Geodesist': Geodesist,
            'Meteorologist': Meteorologist,
        }

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self.valid_astronaut_types:
            raise Exception("Astronaut type is not valid!")

        if self.__find_astronaut_by_name(name):
            return f"{name} is already added."

        new_astronaut = self.valid_astronaut_types[astronaut_type](name)
        self.astronaut_repository.astronauts.append(new_astronaut)

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self.__find_planet_by_name(name):
            return f"{name} is already added."

        planet_items = items.split(', ')
        new_planet = Planet(name)
        new_planet.items.extend(planet_items)
        self.planet_repository.planets.append(new_planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.__find_astronaut_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.astronauts.remove(astronaut)

        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name: str):
        planet = self.__find_planet_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")

        best_astronauts = self.__find_astronauts_for_mission()
        if not best_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        astronauts_participated = 0
        for astronaut in best_astronauts:
            astronaut.land_on_planet(planet)
            astronauts_participated += 1
            if not planet.items:
                self.completed_missions += 1
                return f"Planet: {planet_name} was explored." \
                       f" {astronauts_participated} astronauts participated in collecting items."

        self.not_completed_missions += 1

        return "Mission is not completed."

    def report(self):
        result = [
            f"{self.completed_missions} successful missions!",
            f"{self.not_completed_missions} missions were not completed!",
            "Astronauts' info:"
        ]
        for astronaut in self.astronaut_repository.astronauts:
            result.append(astronaut.info())

        return '\n'.join(result)

    def __find_astronauts_for_mission(self):
        best_astronauts = []
        suitable_astronauts = [a for a in self.astronaut_repository.astronauts if a.oxygen > 30]
        for astronaut in sorted(suitable_astronauts, key=lambda x: -x.oxygen):
            if len(best_astronauts) == 5:
                break
            best_astronauts.append(astronaut)

        return best_astronauts

    def __find_planet_by_name(self, name):
        return next((p for p in self.planet_repository.planets if p.name == name), None)

    def __find_astronaut_by_name(self, name):
        return next((a for a in self.astronaut_repository.astronauts if a.name == name), None)
