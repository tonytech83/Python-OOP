<p align="center">
<strong>
04. Type Check
</strong>
</p>

________________________________________________________

<p align="left">

Create a decorator called **type_check**. It should receive a type (**int/float/str/…**), and it should check if the parameter passed to the decorated function is of the **type** given to the decorator. If it is, **execute** the function and **return the result**, otherwise **return "Bad Type"**.
</p>

_____________________________________________________________

<h4 align="center">Test Code 1</h4>

```Python
@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
```

<h4 align="center">Output 1</h4>

```
4
Bad Type
```
<h4 align="center">Test Code 2</h4>

```Python
@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
```

<h4 align="center">Output 2</h4>

```
H
Bad Type
```
