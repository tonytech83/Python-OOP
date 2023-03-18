# Exam: 01. Take Skip
# From: Iterators and Generators - Exercise
# https://judge.softuni.org/Contests/Compete/Index/1945#0

class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.iterations = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.count:
            raise StopIteration

        current_number = self.iterations * self.step
        self.iterations += 1

        return current_number


# Test code 1
numbers = take_skip(2, 6)
for number in numbers:
    print(number)

# Test code 2
numbers = take_skip(10, 5)
for number in numbers:
    print(number)
