# Exam: 07. Reader
# From: Iterators and Generators - Exercise
# https://judge.softuni.org/Contests/Compete/Index/1945#6

def read_next(*args):
    for sequence in args:
        for el in sequence:
            yield el


# Test code
for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

print()

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
