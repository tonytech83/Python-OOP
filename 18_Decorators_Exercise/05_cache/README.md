<p align="center">
<strong>
05. Cache
</strong>
</p>

________________________________________________________

<p align="left">

Create a decorator called **cache**. It should store all the returned values of the **recursive function fibonacci**. You are provided with this code:
```Python
def cache(func):


# TODO: Implement


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

You need to create a **dictionary** called **log** that will store all the **n**'s (**keys**) and the **returned results** (**values**) and **attach** that dictionary to the **fibonacci** function as a variable called **log**, so when you call it, it returns that dictionary. For more clarification, see the examples
</p>

_____________________________________________________________

<h4 align="center">Test Code 1</h4>

```Python
fibonacci(3)
print(fibonacci.log)
```

<h4 align="center">Output 1</h4>

```
{1: 1, 0: 0, 2: 1, 3: 2}
```
<h4 align="center">Test Code 2</h4>

```Python
fibonacci(4)
print(fibonacci.log)
```

<h4 align="center">Output 2</h4>

```
{1: 1, 0: 0, 2: 1, 3: 2, 4: 3}
```
