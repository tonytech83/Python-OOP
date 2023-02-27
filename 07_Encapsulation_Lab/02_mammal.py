# Exam: 02. Mammal
# From: Encapsulation - Lab
# URL: https://judge.softuni.org/Contests/Practice/Index/1938#1

class Mammal:
    __kingdom = 'animals'

    def __init__(self, name: str, type: str, sound: str):
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        return f'{self.name} makes {self.sound}'

    @staticmethod
    def get_kingdom():
        return Mammal.__kingdom

    def info(self):
        return f'{self.name} is of type {self.type}'


# Test code
mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())
