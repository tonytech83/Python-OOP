# Exam: 04. Multiply
# From: Decorators - Lab
# URL: https://judge.softuni.org/Contests/Practice/Index/1946#3

def multiply(times):
    def decorator(function):
        def wrapper(number):
            return function(number) * times

        return wrapper

    return decorator


# Test code 1
@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))


# Test code 2
@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))
