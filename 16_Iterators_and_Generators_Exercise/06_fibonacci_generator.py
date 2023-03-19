# Exam: 06. Fibonacci Generator
# From: Iterators and Generators - Exercise
# https://judge.softuni.org/Contests/Compete/Index/1945#5

def fibonacci():
    fib0 = 0
    fib1 = 1

    yield fib0
    yield fib1

    while True:
        next_number = fib0 + fib1
        yield next_number

        fib0 = fib1
        fib1 = next_number


# Test code 1
generator = fibonacci()
for i in range(10):
    print(next(generator))

print()

# Test code 2
generator = fibonacci()
for i in range(1):
    print(next(generator))
