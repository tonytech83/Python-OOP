from project.car import Car


class SportsCar(Car):
    @staticmethod
    def race():
        return 'racing...'


# ----- Test -----
# car = SportsCar
# print(car.move())
# print(car.drive())
# print(car.race())
