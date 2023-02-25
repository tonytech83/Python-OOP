# Exam: 04. Glass
# From: Classes and Objects - Lab
# URL: https://judge.softuni.org/Contests/Practice/Index/1936#3

class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml: int) -> str:
        if Glass.capacity - self.content >= ml:
            self.content += ml
            return f'Glass filled with {ml} ml'

        return f'Cannot add {ml} ml'

    def empty(self) -> str:
        self.content = 0
        return f'Glass is now empty'

    def info(self) -> str:
        return f'{Glass.capacity - self.content} ml left'


# Test code
glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
