from typing import List

from project.software.software import Software


class Hardware:

    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components: List[Software] = []

    def install(self, software: Software):
        soft_capacity = software.capacity_consumption
        soft_memory = software.memory_consumption

        if self.capacity < soft_capacity or self.memory < soft_memory:
            raise Exception("Software cannot be installed")

        self.software_components.append(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)
