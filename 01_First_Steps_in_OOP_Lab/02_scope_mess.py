# Exam: 02. Scope Mess
# From: First Steps in OOP - Lab
# URL: https://judge.softuni.org/Contests/Practice/Index/1934#1

x = "global"


def outer():
    x = "local"

    def inner():
        # added "nonlocal x" to change variable "x" in Enclosure scope
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        # added "global x" to change variable "x" in Global scope
        global x
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)

# --- Change output form: ---
# global
# outer: local
# inner: nonlocal
# outer: local
# global

# --- to: ---
# global
# outer: local
# inner: nonlocal
# outer: nonlocal
# global: changed!

