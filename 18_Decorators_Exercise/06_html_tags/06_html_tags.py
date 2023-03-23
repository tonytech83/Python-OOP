# Exam: 06. HTML Tags
# From: Decorators - Exercise
# URL: https://judge.softuni.org/Contests/Compete/Index/1947#5


# Test code 1
def tags(html_tag):
    def decorator(func_ref):
        def wrapper(*args):
            func_result = func_ref(*args)

            return f'<{html_tag}>{func_result}</{html_tag}>'

        return wrapper

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))


# Test code 2
@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))
