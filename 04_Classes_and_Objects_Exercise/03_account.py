# Exam: 03. Account
# From: Classes and Objects - Exercise
# URL: https://judge.softuni.org/Contests/Compete/Index/1937#2

class Account:
    def __init__(self, account_id: int, name: str, balance: int = 0):
        self.id = account_id
        self.name = name
        self.balance = balance

    def credit(self, amount: int) -> int:
        self.balance += amount

        return self.balance

    def debit(self, amount: int) -> int or str:
        if amount > self.balance:
            return 'Amount exceeded balance'

        self.balance -= amount

        return self.balance

    def info(self) -> str:
        return f'User {self.name} with account {self.id} has {self.balance} balance'


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
