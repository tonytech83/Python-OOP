<p align="center">
<strong>
02. Even Parameters
</strong>
</p>

________________________________________________________

<p align="left">

Create a decorator function called **even_parameters**. It should check if **all parameters** passed to a function are **even numbers** and only then **execute** the function and **return** the result. Otherwise, **don't execute** the function and return **"Please use only even numbers!"**
</p>

_____________________________________________________________

<h4 align="center">Test Code 1</h4>

```Python
@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))
```

<h4 align="center">Output 1</h4>

```
6
Please use only even numbers!
```
<h4 align="center">Test Code 2</h4>

```Python
@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
```

<h4 align="center">Output 2</h4>

```
384
Please use only even numbers!
```
