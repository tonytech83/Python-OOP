# Exam: 04. Type Check
# From: Decorators - Exercise
# URL: https://judge.softuni.org/Contests/Compete/Index/1947#3


def type_check(argument_type):
    def decorator(func_ref):
        def wrapper(argument):
            if not isinstance(argument, argument_type):
                return 'Bad Type'

            return func_ref(argument)

        return wrapper

    return decorator


# Test code 1
@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))


# Test code 2
@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
