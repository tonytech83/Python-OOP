# Exam: 02. Vowel Filter
# From: Decorators - Lab
# URL: https://judge.softuni.org/Contests/Practice/Index/1946#1

def vowel_filter(function):
    def wrapper():
        return [ch for ch in function() if ch.lower() in 'aeiou']

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
