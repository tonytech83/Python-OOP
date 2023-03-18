# Exam: 02. Reverse Iter
# From: Iterators and Generators - Lab
# https://judge.softuni.org/Contests/Practice/Index/1944#1

class reverse_iter:

    def __init__(self, iterable_obj):
        self.iterable_obj = iterable_obj

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                return self.iterable_obj.pop()
            except IndexError:
                raise StopIteration


# Test code
reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
