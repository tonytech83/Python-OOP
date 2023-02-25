# Exam: 05. Smartphone
# From: Classes and Objects - Lab
# URL: https://judge.softuni.org/Contests/Practice/Index/1936#4
from typing import List


class Smartphone:
    def __init__(self, memory: int):
        self.memory = memory
        self.apps: List[str] = []
        self.is_on: bool = False

    def install(self, app: str, app_memory: int) -> str:
        if self.memory >= app_memory:
            if self.is_on:
                self.memory -= app_memory
                self.apps.append(app)
                return f'Installing {app}'

            return f'Turn on your phone to install {app}'

        return f'Not enough memory to install {app}'

    def power(self) -> None:
        self.is_on = not self.is_on

    def status(self) -> str:
        return f'Total apps: {len(self.apps)}. Memory left: {self.memory}'


# Test code
smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
