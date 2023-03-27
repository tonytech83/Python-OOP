<p align="center">
<strong>
06. HTML Tags
</strong>
</p>

________________________________________________________

<p align="left">

Create a decorator called **tags**. It should receive an HTML **tag** as a parameter, **wrap** the result of a function with the given tag and **return the new result**. For more clarification, see the examples below
</p>

_____________________________________________________________

<h4 align="center">Test Code 1</h4>

```Python
@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
```

<h4 align="center">Output 1</h4>

```
<p>Hello you!</p>
```
<h4 align="center">Test Code 2</h4>

```Python
@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
```

<h4 align="center">Output 2</h4>

```
<h1>HELLO</h1>
```
