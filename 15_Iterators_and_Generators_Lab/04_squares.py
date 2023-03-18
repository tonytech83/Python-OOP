# Exam: 04. Squares
# From: Iterators and Generators - Lab
# https://judge.softuni.org/Contests/Practice/Index/1944#3

def squares(number):
    current_number = 1

    while current_number <= number:
        yield current_number ** 2
        current_number += 1


# Test code
print(list(squares(5)))
