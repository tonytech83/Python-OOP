from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    COMPUTER_VALID_TYPES = {
        "Laptop": Laptop,
        "Desktop Computer": DesktopComputer
    }

    def __init__(self):
        self.warehouse: list = []
        self.profits: int = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in ComputerStoreApp.COMPUTER_VALID_TYPES:
            raise ValueError(f'{type_computer} is not a valid type computer!')

        new_computer = ComputerStoreApp.COMPUTER_VALID_TYPES[type_computer](manufacturer, model)
        new_computer_configuration = new_computer.configure_computer(processor, ram)
        self.warehouse.append(new_computer)

        return new_computer_configuration

    def find_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        for computer in self.warehouse:
            if computer.price <= client_budget and computer.ram >= wanted_ram and wanted_processor == computer.processor:
                return computer

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        computer_to_sell = self.find_computer(client_budget, wanted_processor, wanted_ram)

        if not computer_to_sell:
            raise Exception("Sorry, we don't have a computer for you.")

        self.profits += client_budget - computer_to_sell.price
        self.warehouse.remove(computer_to_sell)

        return f'{computer_to_sell} sold for {client_budget}$.'
