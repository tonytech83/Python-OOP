from abc import ABC, abstractmethod
from math import sqrt


class Computer(ABC):

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price: int = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value.strip():
            raise ValueError('Manufacturer name cannot be empty.')

        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError('Model name cannot be empty.')

        self.__model = value

    @property
    @abstractmethod
    def available_processors(self):
        pass

    @property
    @abstractmethod
    def ram_sizes(self):
        pass

    @property
    @abstractmethod
    def computer_type(self):
        pass

    def configure_computer(self, processor: str, ram: int):

        if processor not in self.available_processors:
            raise ValueError(
                f'{processor} is not compatible with {self.computer_type} {self.manufacturer} {self.model}!')

        if ram not in self.ram_sizes:
            raise ValueError(
                f'{ram}GB RAM is not compatible with {self.computer_type} {self.manufacturer} {self.model}!')

        self.processor = processor
        self.ram = ram
        self.price = self.available_processors[processor] + self.ram_sizes[ram]

        return f'Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {self.price}$.'

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"
