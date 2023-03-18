# Exam: 02. Dictionary Iterator
# From: Iterators and Generators - Exercise
# https://judge.softuni.org/Contests/Compete/Index/1945#1

class dictionary_iter:

    def __init__(self, data: dict):
        self.data = list(data.items())
        self.idx = 0
        self.end = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == self.end:
            raise StopIteration

        current_kvp = self.data[self.idx]
        self.idx += 1

        return current_kvp


# Test code 1
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

# Test code 2
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
