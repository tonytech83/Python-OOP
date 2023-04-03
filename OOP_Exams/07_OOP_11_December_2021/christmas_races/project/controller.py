from typing import List

from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    @property
    def valid_car_types(self):
        return {
            "MuscleCar": MuscleCar,
            "SportsCar": SportsCar,
        }

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.valid_car_types:
            return

        if self.__find_car_by_model(model):
            raise Exception(f"Car {model} is already created!")

        new_car = self.valid_car_types[car_type](model, speed_limit)
        self.cars.append(new_car)

        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self.__find_driver_by_name(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)

        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if self.__find_race_by_name(race_name):
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)

        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver_by_name(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        car = self.__find_available_car_by_type(car_type)
        if not car:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car:
            return driver.change_car(car)
        else:
            driver.car = car
            car.is_taken = True
            car.driver = driver
            return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__find_race_by_name(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        driver = self.__find_driver_by_name(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race.name} race."

        race.drivers.append(driver)

        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__find_race_by_name(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        return self.__fastest_three_cars(race)

    def __find_race_by_name(self, race_name):
        return next((r for r in self.races if r.name == race_name), False)

    def __find_driver_by_name(self, driver_name):
        return next((d for d in self.drivers if d.name == driver_name), False)

    def __find_car_by_model(self, model):
        return next((c for c in self.cars if c.model == model), False)

    def __find_available_car_by_type(self, car_type):
        for car in reversed(self.cars):
            if car.__class__.__name__ == car_type and car.is_taken is False:
                return car

    @staticmethod
    def __fastest_three_cars(race: Race):
        winners = []

        for idx, driver in enumerate(sorted(race.drivers, key=lambda d: -d.car.speed_limit)):
            if idx == 3:
                break
            driver.number_of_wins += 1
            winners.append(f"Driver {driver.name} wins the {race.name} race with a speed of {driver.car.speed_limit}.")

        return '\n'.join(winners)
