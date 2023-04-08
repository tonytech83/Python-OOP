from abc import ABC, abstractmethod
from typing import List

from project.robots.base_robot import BaseRobot


class BaseService(ABC):

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.robots: List[BaseRobot] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Service name cannot be empty!")

        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value: int):
        if value <= 0:
            raise ValueError("Service capacity cannot be less than or equal to 0!")

        self.__capacity = value

    @property
    @abstractmethod
    def service_type(self):
        pass

    def details(self):
        robots_names = ' '.join([r.name for r in self.robots]) if self.robots else "none"

        return f"{self.name} {self.service_type} Service:\nRobots: {robots_names}"
