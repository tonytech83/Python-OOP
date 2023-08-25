from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    @property
    def valid_vehicle_types(self):
        return {
            "PassengerCar": PassengerCar,
            "CargoVan": CargoVan,
        }

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        if self.__find_object(driving_license_number, "driving_license_number", self.users) is not None:
            return f"{driving_license_number} has already been registered to our platform."

        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)

        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.valid_vehicle_types:
            return f"Vehicle type {vehicle_type} is inaccessible."

        if self.__find_object(license_plate_number, "license_plate_number", self.vehicles) is not None:
            return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = self.valid_vehicle_types[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)

        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length == length:
                return f"{start_point}/{end_point} - {length} km had already been added to our platform."
            if route.start_point == start_point and route.end_point == end_point and route.length < length:
                return f"{start_point}/{end_point} shorter route had already been added to our platform."
            if route.start_point == start_point and route.end_point == end_point and route.length > length:
                route.is_locked = True

        route_id = len(self.routes) + 1
        new_route = Route(start_point, end_point, length, route_id)
        self.routes.append(new_route)

        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,
                  is_accident_happened: bool):
        user = self.__find_object(driving_license_number, "driving_license_number", self.users)
        vehicle = self.__find_object(license_plate_number, "license_plate_number", self.vehicles)
        route = self.__find_object(route_id, "route_id", self.routes)

        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)

        if is_accident_happened:
            vehicle.change_status()
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        count_of_repaired_vehicles = 0
        sorted_vehicles = sorted(self.__find_damaged_vehicles(), key=lambda v: (v.brand, v.model))

        for vehicle in sorted_vehicles:
            if count_of_repaired_vehicles == count:
                break

            vehicle.is_damaged = False
            vehicle.battery_level = 100
            count_of_repaired_vehicles += 1

        return f"{count_of_repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self):
        result = ["*** E-Drive-Rent ***"]

        for user in sorted(self.users, key=lambda u: -u.rating):
            result.append(str(user))

        return "\n".join(result)

    def __find_damaged_vehicles(self):
        return [v for v in self.vehicles if v.is_damaged]

    @staticmethod
    def __find_object(value, attr, container):
        for obj in container:
            if getattr(obj, attr) == value:
                return obj
        else:
            return None
