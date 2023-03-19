# Exam: 08. Prime Numbers
# From: Iterators and Generators - Exercise
# https://judge.softuni.org/Contests/Compete/Index/1945#7

from math import ceil, sqrt


def is_prime(number):
    if number <= 1:
        return False

    # reduce the iterations for bigger numbers
    end = ceil(sqrt(number)) if number > 10 else number

    for i in range(2, end):
        if number % i == 0:
            return False

    return True


def get_primes(numbers):
    for num in numbers:
        if is_prime(num):
            yield num


# Test code 1
print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 8, 0, 11, 13, 12])))

# Test code 2
print(list(get_primes([-2, 0, 0, 1, 1, 0])))

# Test code 3
print(list(get_primes([111, 1231])))
