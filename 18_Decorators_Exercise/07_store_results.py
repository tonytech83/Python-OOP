# Exam: 07.	*Store Results
# From: Decorators - Exercise
# URL: N/A

class store_results:

    def __init__(self, func_ref):
        self.func_ref = func_ref

    def __call__(self, *args):
        func_result = self.func_ref(*args)

        with open('results.txt', 'a') as file:
            file.write(f"Function '{self.func_ref.__name__}' was called. Result: {func_result}\n")


# Test code
@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 3)
mult(6, 4)
