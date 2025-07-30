Here are the full lecture notes in markdown format:

**Introduction to Python**
==========================

* Python was created by Guido van Rossum.
* Its name is inspired not from the snake, but from the BBC comedy series "Monty Python's Flying Circus".
* Python Characteristics:
	+ Dynamically typed: you do not explicitly declare variable types.
	+ This makes Python syntax simpler and faster to write but can make Python slower than statically typed languages due to runtime type checking.

**Variables and Data Types in Python**
=====================================

* Dynamic Typing and Variables:
	+ Variables can be assigned without specifying type.
	+ Python infers type based on value.
* Determining Variable Type: Use `type()` function to know the type of variable.
* Example:
```python
x = 10
print(type(x))  # Output: <class 'int'>
y = "Hello"
print(type(y))  # Output: <class 'str'>
```
* Typecasting in Python:
	+ Use `int()`, `float()`, `str()`, and `bool()` to cast types explicitly.
	+ Example:
```python
x = int(10.5)  # converts 10.5 to 10
print(x)
val = "123"
num = int(val)  # converts '123' string to integer 123
print(num)
```
* Input and Typecasting: `input()` returns a string by default, use typecasting on input value.
* Example:
```python
age = int(input("Enter your age: "))
print(f"Age: {age}, Type: {type(age)}")
```

**Printing in Python**
=====================

* Printing Syntax: Use `print()` function. No semicolons needed. Comma `,` in print inserts space between items.
* Concatenation with `+` requires all operands to be strings.
* Example:
```python
x = 10
print(x, "is a number")  # Output: 10 is a number
```
* String Formatting: Use f-strings, `format()`, or concatenation for printing multiple variables.
* Examples:
```python
name = "Manoj"
age = 30
address = "Raj Nagar"
pincode = "123456"

print(f"Name: {name}, Age: {age}, Address: {address}, Pincode: {pincode}")
print("Name: {}, Age: {}, Address: {}, Pincode: {}".format(name, age, address, pincode))
```

**Comments in Python**
=====================

* Single-line comment: Use `#` at the beginning of the line.
* Multi-line comment: Use triple quotes `'''` or `"""` to enclose multiple lines.
* Example:
```python
# This is a single-line comment

'''
This is a
multi-line comment
'''
```

**Basic Operators and Expressions**
=====================================

* Operators:
	+ Addition: `+`
	+ Subtraction: `-`
	+ Multiplication: `*`
	+ Division: `/` (results float)
	+ Floor Division: `//` (results integer quotient)
	+ Modulus: `%` (remainder)
	+ Power: `**`
* Example:
```python
x, y = 20, 5
print(x + y)   # 25
print(x - y)   # 15
print(x * y)   # 100
print(x / y)   # 4.0
print(x // y)  # 4
print(x % y)   # 0
print(x ** y)  # 3200000 (20^5)
```

**Conditional Statements**
=====================

* Syntax in Python: No parentheses needed around conditions.
* Use `if`, `elif`, and `else` for conditions.
* Example:
```python
gender = "male"
age = 22
if gender == "male" and age >= 21:
    print("Can marry")
elif gender == "female" and age >= 18:
    print("Can marry")
else:
    print("Cannot marry")
```

**Logical Operators**
=====================

* Logical Operators in Python: `and`, `or`, `not`
* Example:
```python
if gender == "male" and age >= 21:
    print("Eligible")
if gender == "female" or age >= 18:
    print("Check further")
```

**Loops**
=====

* While Loop: Runs as long as condition is true. No `i++` or `i--` syntax, use `i += 1` or `i -= 1`.
* Example:
```python
i = 1
while i <= 10:
    print(i)
    i += 1
```
* For Loop using range(): Generates sequence with `range()`. Stop is exclusive.
* Example:
```python
for i in range(1, 11):
    print(i)

for i in range(10, 0, -1):  # reverse loop
    print(i)
```

**Functions**
==========

* Defining Functions: Use `def` keyword. No need to declare return type or parameter types explicitly.
* Example:
```python
def add(x, y):
    return x + y

print(add(4, 5))  # Output: 9
```
* Functions with Conditional Logic: Use `if-elif-else` chains instead of traditional switch-case.
* Example:
```python
value = 2
if value == 1:
    print("One")
elif value == 2:
    print("Two")
else:
    print("Other")
```

**Lambda Functions**
==================

* What is Lambda?: Anonymous one-line functions. Often used for small, throwaway functions.
* Syntax: `lambda parameters: expression`
* Examples:
```python
add = lambda x, y: x + y
print(add(2, 3))  # 5

square = lambda x: x ** 2
print(square(4))  # 16

is_even = lambda x: x % 2 == 0
print(is_even(6))  # True
```

**Shorthand Conditional (Ternary) Operator**
=====================================

* Conditional expression in one line.
* Example:
```python
max_num = lambda a, b: a if a > b else b
print(max_num(10, 5))  # 10
```

**Truthiness in Python**
=====================

* What Python Considers True and False:
	+ Values considered False: `False`, `None`, numeric zero of all types (0, 0.0), empty sequences or collections (`''`, `[]`, `{}`).
	+ All other values are considered True, including negative numbers and non-empty strings.
* Example:
```python
if 1:
    print("1 is True")
if -1:
    print("-1 is True")
if 0:
    print("0 is True")  # This won't print
if None:
    print("None is True")  # This won't print
```

**Exception Handling in Python**
=====================

* Try Except Blocks: Python uses `try`, `except` to handle exceptions.
* Example:
```python
try:
    x = 10 / 0
except Exception as e:
    print("Something went wrong:", e)
```
* Finally Block: Code inside finally always executes after try-except. Useful for cleanup activities like closing files or releasing resources.
* Example:
```python
try:
    x = 10 / 2
except Exception as e:
    print("Error:", e)
finally:
    print("Execution complete")
```

**Python Switch Case / Match Case**
=====================================

* Python does not have a traditional switch-case like other languages.
* Use `if-elif-else` chains instead.
* Example of if-elif-else:
```python
value = 2
if value == 1:
    print("One")
elif value == 2:
    print("Two")
else:
    print("Other")
```
* Python 3.10+ introduces match-case statement for pattern matching.
* Example of match-case (Python 3.10+):
```python
value = 2
match value:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other")
```

I hope this helps! Let me know if you have any questions or need further clarification on any of these topics.