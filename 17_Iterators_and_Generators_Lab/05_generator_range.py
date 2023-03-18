# Exam: 05. Generator Range
# From: Iterators and Generators - Lab
# https://judge.softuni.org/Contests/Practice/Index/1944#4


def genrange(start: int, end: int):
    i = start

    while i <= end:
        yield i
        i += 1


# Test code
print(list(genrange(1, 10)))
