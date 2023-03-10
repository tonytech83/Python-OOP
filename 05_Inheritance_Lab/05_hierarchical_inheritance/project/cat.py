from project.animals.animal import Animal


class Cat(Animal):
    @staticmethod
    def meow():
        return 'meowing...'
