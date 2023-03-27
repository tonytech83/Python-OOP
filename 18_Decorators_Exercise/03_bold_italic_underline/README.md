<p align="center">
<strong>
03. Bold, Italic, Underline
</strong>
</p>

________________________________________________________

<p align="left">

Create **three decorators: make_bold, make_italic, make_underline**, which will have to **wrap** a **text** returned from a function in **<b></b>, <i></i>** and **<u></u> respectively**.
</p>

_____________________________________________________________

<h4 align="center">Test Code 1</h4>

```Python
@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))
```

<h4 align="center">Output 1</h4>

```
<b><i><u>Hello, Peter</u></i></b>
```
<h4 align="center">Test Code 2</h4>

```Python
@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))
```

<h4 align="center">Output 2</h4>

```
<b><i><u>Hello, Peter, George</u></i></b>
```
