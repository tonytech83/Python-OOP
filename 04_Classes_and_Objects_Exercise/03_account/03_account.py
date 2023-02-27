# Exam: 03. Account
# From: Classes and Objects - Exercise
# URL: https://judge.softuni.org/Contests/Compete/Index/1937#2

from project.account import Account

# Test code 1
account = Account(1234, "George", 1000)
print(account.credit(500))
print(account.debit(1500))
print(account.info())

# Test code 2
account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())
