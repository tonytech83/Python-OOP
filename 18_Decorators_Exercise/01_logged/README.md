<p align="center">
<strong>
01. Logged
</strong>
</p>

________________________________________________________

<p align="left">

Create a decorator called **logged**. It should **return** the name of the function that is being called and its parameters. It should also return the **result of the execution** of the function being called. See the examples for more clarification.
</p>

_____________________________________________________________

<h4 align="center">Test Code 1</h4>

```Python
@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))
```

<h4 align="center">Output 1</h4>

```
you called func(4, 4, 4)
it returned 6
```
<h4 align="center">Test Code 2</h4>

```Python
@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))
```

<h4 align="center">Output 2</h4>

```
you called sum_func(1, 4)
it returned 5
```
