# Exam: 09. Computer Store
# From: Decorators - Exercise
# URL: https://judge.softuni.org/Contests/Compete/Index/1947#6


from project.computer_store_app import ComputerStoreApp

computer_store = ComputerStoreApp()

print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))
print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))
print(computer_store.profits)

# # print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 6))
# # print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 256))
#
# print(computer_store.build_computer("Desktop Computer", "Dell", "PowerEdge", "Intel Core i5-12600K", 16))
# print(computer_store.sell_computer(800, "Intel Core i5-12600K", 16))

# print(computer_store.build_computer("Server", "Apple", "Macbook", "Apple M1 Pro", 64))

# print(computer_store.build_computer("Laptop", "", "A", "Apple M1 Pro", 64))

# print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Intel Core i5-12600K", 64))

# print(computer_store.build_computer("Desktop Computer", "Dell", "PowerEdge", "Apple M1 Pro", 16))

# print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))
# print(computer_store.sell_computer(10000, "AMD Ryzen 7 5700G", 64))
