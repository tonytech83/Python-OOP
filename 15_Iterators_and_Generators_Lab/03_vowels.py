# Exam: 03. Vowels
# From: Iterators and Generators - Lab
# https://judge.softuni.org/Contests/Practice/Index/1944#2

class vowels:

    def __init__(self, text: str):
        self.text = text
        self.i = 0
        self.end = len(text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.i <= self.end:
            current_char = self.text[self.i]
            self.i += 1

            if current_char.lower() in ('a', 'e', 'i', 'o', 'u'):
                return current_char
        else:
            raise StopIteration


# Test code
my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
