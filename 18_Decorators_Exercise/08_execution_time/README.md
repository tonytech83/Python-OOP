<p align="center">
<strong>
08. Execution Time
</strong>
</p>

________________________________________________________

<p align="left">

Import the **time** module. Create a decorator called **exec_time**. It should calculate how much **time** a function needs to be **executed**. See the examples for more clarification.

_**Note: You might have different results from the given ones. The solutions to this problem cannot be submitted in the judge system.**_
</p>

_____________________________________________________________

<h4 align="center">Test Code 1</h4>

```Python
@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 10000000))
```

<h4 align="center">Output 1</h4>

```
0.8342537879943848
```
<h4 align="center">Test Code 2</h4>

```Python
@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result
print(concatenate(["a" for i in range(1000000)]))
```

<h4 align="center">Output 2</h4>

```
0.14537858963012695
```
<h4 align="center">Test Code 3</h4>

```Python
@exec_time
def loop():
    count = 0
    for i in range(1, 9999999):
        count += 1
print(loop())
```

<h4 align="center">Output 3</h4>

```
0.4199554920196533
```