# Exam: 09. Possible permutations
# From: Iterators and Generators - Exercise
# https://judge.softuni.org/Contests/Compete/Index/1945#8

from itertools import permutations


def possible_permutations(elements):
    result = permutations(elements)

    for perm in result:
        yield list(perm)


# Test code 1
[print(n) for n in possible_permutations([1, 2, 3])]

# print()

# Test code 2
[print(n) for n in possible_permutations([1])]
