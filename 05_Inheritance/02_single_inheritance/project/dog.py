from project.animal import Animal


class Dog(Animal):
    @staticmethod
    def bark():
        return 'barking...'


# ----- Test code -----
# dog = Dog()
# print(dog.eat())
# print(dog.bark())
