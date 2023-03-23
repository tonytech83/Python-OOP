# Exam: 03. Bold, Italic, Underline
# From: Decorators - Exercise
# URL: https://judge.softuni.org/Contests/Compete/Index/1947#2


def make_bold(func_ref):
    def wrapper(*args):
        func_result = func_ref(*args)

        return f'<b>{func_result}</b>'

    return wrapper


def make_italic(func_ref):
    def wrapper(*args):
        func_result = func_ref(*args)

        return f'<i>{func_result}</i>'

    return wrapper


def make_underline(func_ref):
    def wrapper(*args):
        func_result = func_ref(*args)

        return f'<u>{func_result}</u>'

    return wrapper


# Test code 1
@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


# Test code 2
@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
