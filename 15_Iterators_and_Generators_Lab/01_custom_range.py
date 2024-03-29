# Exam: 01. Custom Range
# From: Iterators and Generators - Lab
# https://judge.softuni.org/Contests/Practice/Index/1944#0


class custom_range:

    def __init__(self, start: int, end: int):
        self.i = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.end:
            current_number = self.i
            self.i += 1

            return current_number
        else:
            raise StopIteration


# Test code
one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
