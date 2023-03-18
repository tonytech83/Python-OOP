# Exam: 04. Sequence Repeat
# From: Iterators and Generators - Exercise
# https://judge.softuni.org/Contests/Compete/Index/1945#3

class sequence_repeat:

    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.pointer = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer == self.number:
            raise StopIteration

        symbol = self.sequence[self.pointer % len(self.sequence)]
        self.pointer += 1

        return symbol


# Test code 1
result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

# Test code 2
result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
