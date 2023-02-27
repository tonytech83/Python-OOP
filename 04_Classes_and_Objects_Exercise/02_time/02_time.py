# Exam: 02. Time
# From: Classes and Objects - Exercise
# URL: https://judge.softuni.org/Contests/Compete/Index/1937#1
from project.time import Time

# Test codes
time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())

time = Time(23, 59, 20)
print(time.next_second())
