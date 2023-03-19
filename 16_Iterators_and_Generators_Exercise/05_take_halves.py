# Exam: 05. Take Halves
# From: Iterators and Generators - Exercise
# https://judge.softuni.org/Contests/Compete/Index/1945#4

def solution():
    def integers():
        number = 1
        while True:
            yield number
            number += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        result = []

        for _ in range(n):
            result.append(next(seq))

        return result

    return (take, halves, integers)


# Test code 1
take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

# Test code 2
take = solution()[0]
halves = solution()[1]
print(take(0, halves()))
