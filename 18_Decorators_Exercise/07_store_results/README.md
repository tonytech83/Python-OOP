<p align="center">
<strong>
07. *Store Result
</strong>
</p>

________________________________________________________

<p align="left">

Create a **class** called **store_results**. It should be used as a **decorator** and **store** **information** about
the executed functions in a **file** called **results.txt** in the format: **"Function {func_name} was called. Result:
{func_result}"**

_**Note: The solutions to this problem cannot be submitted in the judge system**_
</p>

_____________________________________________________________

<h4 align="center">Test Code</h4>

```Python
@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


add(2, 2)
mult(6, 4)
```

<h4 align="center">Output</h4>

```
Function 'add' was called. Result: 4
Function 'mult' was called. Result: 24
```

