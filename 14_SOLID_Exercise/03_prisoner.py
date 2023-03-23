from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, position):
        self.position = position

    @abstractmethod
    def person_statute(self):
        pass

    def walk_north(self, dist):
        if self.person_statute():
            self.position[0] += dist
        else:
            raise AttributeError

    def walk_east(self, dist):
        if self.person_statute():
            self.position[1] += dist
        else:
            raise AttributeError


class Prison:

    def __init__(self):
        self.north = 3
        self.east = 3

    @property
    def location(self):
        return self.north, self.east


class FreePerson(Person):

    def __init__(self, position):
        super().__init__(position)
        self.is_free = True
        self.type = "free person"

    def person_statute(self):
        return self.is_free


class Prisoner(Person):

    def __init__(self, position):
        super().__init__(position)
        self.is_free = False
        self.type = "prisoner"

    def person_statute(self):
        return self.is_free


# Test code
prison = Prison()
person_1 = Prisoner(prison.location)
person_2 = FreePerson([0, 0])

print('=' * 20 + ' Enter direction ' + '=' * 20)
dist_north = int(input('Enter the north direction (integer): '))
dist_east = int(input("Enter the east direction (integer): "))

for person in [person_1, person_2]:
    print()
    print('=' * 20 + f' {person.__class__.__name__} ' + '=' * 20)
    print(f"The {person.type} trying to walk to north by {dist_north} and east by {dist_east}.")

    try:
        person.walk_north(dist_north)
        person.walk_east(dist_east)
    except AttributeError:
        print(f"The location of the prison: {prison.location}")
    finally:
        print(f"The current position of the {person.type}: {tuple(person.position)}")
