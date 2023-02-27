# Exam: 01. Vet
# From: Classes and Objects - Exercise
# URL: https://judge.softuni.org/Contests/Compete/Index/1937#0

from project.vet import Vet

# Test code
peter = Vet("Peter")
george = Vet("George")
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
print(peter.info())
print(george.info())

# My test codes
print(peter.animals)
print(george.animals)
print(Vet.animals)
