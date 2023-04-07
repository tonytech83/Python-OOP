from typing import List

from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        new_power_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(new_power_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        new_heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(new_heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.__find_object(hardware_name, 'name', System._hardware)
        if not hardware:
            return "Hardware does not exist"

        new_express_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(new_express_software)
        System._software.append(new_express_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.__find_object(hardware_name, 'name', System._hardware)
        if not hardware:
            return "Hardware does not exist"

        new_light_software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(new_light_software)
        System._software.append(new_light_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.__find_object(hardware_name, 'name', System._hardware)
        software = System.__find_object(software_name, 'name', System._software)

        if not hardware or not software:
            return "Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        return "System Analysis\n" \
               f"Hardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {System.__total_usage('memory_consumption', System._software)} " \
               f"/ {System.__total_usage('memory', System._hardware)}\n" \
               f"Total Capacity Taken: {System.__total_usage('capacity_consumption', System._software)} " \
               f"/ {System.__total_usage('capacity', System._hardware)}"

    @staticmethod
    def system_split():
        result_str = []

        for hardware in System._hardware:
            result_str.append(
                f"Hardware Component - {hardware.name}\n"
                f"Express Software Components: {System.__count_components(hardware, 'Express')}\n"
                f"Light Software Components: {System.__count_components(hardware, 'Light')}\n"
                f"Memory Usage: {System.__usage(hardware, 'memory_consumption')} / {hardware.memory}\n"
                f"Capacity Usage: {System.__usage(hardware, 'capacity_consumption')} / {hardware.capacity}\n"
                f"Type: {hardware.hardware_type}\n"
                f"Software Components: {', '.join(System.__software_names(hardware))}"
            )

        return '\n'.join(result_str)

    @staticmethod
    def __total_usage(attr, container):
        return sum([getattr(s, attr) for s in container])

    @staticmethod
    def __software_names(hardware):
        return [s.name for s in hardware.software_components] if hardware.software_components else "None"

    @staticmethod
    def __usage(hardware, attr):
        return sum([getattr(s, attr) for s in hardware.software_components])

    @staticmethod
    def __find_object(value, attr, container):
        for obj in container:
            if getattr(obj, attr) == value:
                return obj

    @staticmethod
    def __count_components(hardware, searched_type):
        return len([s for s in hardware.software_components if s.software_type == searched_type])
