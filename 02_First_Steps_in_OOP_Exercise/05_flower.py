# Exam: 05. Flower
# From: First Steps in OOP - Exercise
# URL: https://judge.softuni.org/Contests/Practice/Index/1935#4

class Flower:
    def __init__(self, name: str, water_requirements: int):
        self.name = name
        self.water_requirements = water_requirements
        self.is_happy = False

    def water(self, quantity: int) -> None:
        self.is_happy = quantity >= self.water_requirements

    def status(self) -> str:
        return f'{self.name} {"is" if self.is_happy else "is not"} happy'


# Test code
flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())
