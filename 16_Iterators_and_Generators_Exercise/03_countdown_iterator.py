# Exam: 03. Countdown Iterator
# From: Iterators and Generators - Exercise
# https://judge.softuni.org/Contests/Compete/Index/1945#2

class countdown_iterator:

    def __init__(self, count: int):
        self.count = count
        self.iterator = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterator > self.count:
            raise StopIteration

        current_numer = self.count - self.iterator
        self.iterator += 1

        return current_numer


# Test code 1
iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

# Test code 2
iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
