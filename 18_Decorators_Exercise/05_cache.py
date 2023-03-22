# Exam: 05. Cache
# From: Decorators - Exercise
# URL: https://judge.softuni.org/Contests/Compete/Index/1947#4

def cache(func_ref):
    log = {}

    def wrapper(number):
        if number in log:
            return log[number]

        result = func_ref(number)
        log[number] = result

        return result

    wrapper.log = log
    return wrapper


@cache
def fibonacci(n):
    if n < 2:

        return n

    else:

        return fibonacci(n - 1) + fibonacci(n - 2)


# Test code 1
fibonacci(3)
print(fibonacci.log)

# Test code 2
fibonacci(51)
print(fibonacci.log)
