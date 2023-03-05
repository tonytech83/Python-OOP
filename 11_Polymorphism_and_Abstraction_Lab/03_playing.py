# Exam: 03. Playing
# From: Polymorphism and Abstraction - Lab
# https://judge.softuni.org/Contests/Practice/Index/1942#1

# Example of duck typing

def start_playing(obj):
    return obj.play()


# Test code 1
class Guitar:
    def play(self):
        return "Playing the guitar"


guitar = Guitar()
print(start_playing(guitar))


# Test code 2
class Children:
    def play(self):
        return "Children are playing"


children = Children()
print(start_playing(children))
