# Exam: 06. Reverse string
# From: Iterators and Generators - Lab
# https://judge.softuni.org/Contests/Practice/Index/1944#5

def reverse_text(test: str):
    i = len(test) - 1

    while i >= 0:
        yield test[i]
        i -= 1


# Test code
for char in reverse_text("step"):
    print(char, end='')
