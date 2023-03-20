# Exam: 01. Number Increment
# From: Decorators - Lab
# URL: https://judge.softuni.org/Contests/Practice/Index/1946#0


def number_increment(numbers):
    def increase():
        return [x + 1 for x in numbers]

    return increase()


# Test code
print(number_increment([1, 2, 3]))
