from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    @property
    def valid_service_types(self):
        return {
            "MainService": MainService,
            "SecondaryService": SecondaryService
        }

    @property
    def valid_robot_types(self):
        return {
            "MaleRobot": MaleRobot,
            "FemaleRobot": FemaleRobot
        }

    def add_service(self, service_type: str, name: str):
        if service_type not in self.valid_service_types:
            raise Exception("Invalid service type!")

        new_service = self.valid_service_types[service_type](name)
        self.services.append(new_service)

        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.valid_robot_types:
            raise Exception("Invalid robot type!")

        new_robot = self.valid_robot_types[robot_type](name, kind, price)
        self.robots.append(new_robot)

        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.__find_object(robot_name, "name", self.robots)
        service = self.__find_object(service_name, "name", self.services)

        if not self.__match(robot, service):
            return "Unsuitable service."

        if service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")

        service.robots.append(robot)
        self.robots.remove(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.__find_object(service_name, "name", self.services)
        robot = self.__find_object(robot_name, "name", service.robots)
        if not robot:
            raise Exception("No such robot in this service!")

        self.robots.append(robot)
        service.robots.remove(robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.__find_object(service_name, "name", self.services)

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = self.__find_object(service_name, "name", self.services)
        total_price = sum([r.price for r in service.robots])

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result_str = []

        for service in self.services:
            result_str.append(service.details())

        return '\n'.join(result_str)

    @staticmethod
    def __find_object(value, attr, container):
        for obj in container:
            if getattr(obj, attr) == value:
                return obj

    @staticmethod
    def __match(robot, service):
        if robot.__class__.__name__ == "MaleRobot" and service.service_type == 'Main':
            return True
        elif robot.__class__.__name__ == "FemaleRobot" and service.service_type == 'Secondary':
            return True
        else:
            return False
