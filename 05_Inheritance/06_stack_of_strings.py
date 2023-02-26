# Exam: 06. Stack of Strings
# From: Inheritance - Lab
# URL: https://judge.softuni.org/Contests/Practice/Index/1940#5

class Stack:
    def __init__(self):
        self.data: list = []

    def push(self, element: str):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[0]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return ', '.join(reversed(self.data))


# Test code
my_stack = Stack()

my_stack.push('a')
my_stack.push('b')
my_stack.push('c')
print(my_stack)
print(my_stack.top())
print(my_stack.is_empty())
print(my_stack.pop())
print(my_stack.is_empty())
print(my_stack)
