# Exam: 02. Even Parameters
# From: Decorators - Exercise
# URL: https://judge.softuni.org/Contests/Compete/Index/1947#1

# Test code 1
def even_parameters(func_ref):
    def wrapper(*args):
        for element in args:
            if not isinstance(element, int) or element % 2 != 0:
                return 'Please use only even numbers!'

        return func_ref(*args)

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


# Test code 2
@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
