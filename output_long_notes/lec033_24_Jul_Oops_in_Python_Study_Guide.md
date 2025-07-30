Here are the full lecture notes in markdown format:

# Human: Technical Note-Taker

## Class Variables vs Instance Variables

Instance variables are unique to each object instance. Class variables are shared by all instances of the class.

Example:
```python
class Car:
    tax = 1000  # class variable

    def __init__(self, name, age, price):
        self.name = name  # instance variable
        self.age = age
        self.price = price

my_car = Car('Toyota', 10, 500000)
your_car = Car('Ford', 20, 400000)

print(my_car.tax)  # 1000
print(your_car.tax) # 1000

# Modifying class variable through class name
Car.tax = 1200
print(my_car.tax)  # 1200
print(your_car.tax) # 1200
```
Access class variables via `ClassName.variable` or `self.variable`. But do not reassign class variables through `self.variable = value` as it creates an instance variable instead of changing the class variable.

## Encapsulation - Using Getters and Setters

Directly accessing or modifying instance variables outside class methods is not ideal. Encapsulation principle recommends using getter and setter methods to control access and update of attributes.

Example:
```python
class Car:
    def __init__(self, age):
        self._age = age  # convention: '_' denotes protected attribute

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print('Invalid age')

my_car = Car(10)
print(my_car.get_age())  # 10
my_car.set_age(-5)        # Invalid age
print(my_car.get_age())  # 10
```
Protects the object's data integrity.

## Class Methods and @classmethod Decorator

Class methods operate on the class itself rather than instances. They receive the class as first argument, conventionally named `cls`.

Example:
```python
class Car:
    tax = 1000

    @classmethod
    def set_tax(cls, value):
        cls.tax = value

Car.set_tax(1500)
print(Car.tax)  # 1500

my_car = Car()
print(my_car.tax)  # 1500
```
Class methods must be called on the class, not instance.

## Collections Module: Set, Defaultdict, Counter, and Deque

### Set

A set is an unordered collection of unique elements. You can add or remove elements from a set.

Example:
```python
from collections import set

my_set = set([1, 2, 3, 4, 5])
print(my_set)  # {1, 2, 3, 4, 5}

my_set.add(6)
print(my_set)  # {1, 2, 3, 4, 5, 6}
```
### Defaultdict

A defaultdict is a dictionary that provides a default value for the key that does not exist.

Example:
```python
from collections import defaultdict

d = defaultdict(int)
print(d['a'])  # 0
print(d['b'])  # 0
```
### Counter

A counter is a specialized dictionary subclass for counting hashable objects.

Example:
```python
from collections import Counter

text = 'hello world'
counter = Counter(text)
print(counter)  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```
### Deque

A deque is a double-ended queue supporting appending and popping from both ends efficiently.

Example:
```python
from collections import deque

buffer = deque(maxlen=3)

buffer.append(7)
buffer.append(8)
buffer.append(9)
buffer.append(10)  # 7 will be removed automatically
print(buffer)  # deque([8, 9, 10], maxlen=3)
```
## Object-Oriented Programming (OOP) Basics

### Classes and Objects

A class is a blueprint/template for creating objects. An object is an instance of a class.

Example:
```python
class Car:
    pass

my_car = Car()
your_car = Car()

print(id(my_car))
print(id(your_car))
```
id() function returns memory address. Objects `my_car` and `your_car` are different instances in memory.

### __init__ Method and Self

The `__init__` method is a special method called a constructor, used to initialize object attributes. The first parameter is `self`, which refers to the object instance.

Example:
```python
class Car:
    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        self.number = number

my_car = Car('Toyota', 10, 'KA1230')
print(my_car.name)  # Toyota
```
### Instance Variables vs Class Variables

Instance variables are unique to each object instance. Class variables are shared by all instances of the class.

Example:
```python
class Car:
    tax = 1000  # class variable

    def __init__(self, name, age, price):
        self.name = name  # instance variable
        self.age = age
        self.price = price

my_car = Car('Toyota', 10, 500000)
your_car = Car('Ford', 20, 400000)

print(my_car.tax)  # 1000
print(your_car.tax) # 1000
```
Access class variables via `ClassName.variable` or `self.variable`. But do not reassign class variables through `self.variable = value` as it creates an instance variable instead of changing the class variable.

### Methods within Classes

Methods are functions defined inside a class that operate on object data. The first parameter is always `self`, which refers to the object calling the method.

Example:
```python
class Car:
    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        self.number = number

    def car_info(self):
        print(f'Car info - Name: {self.name}, Age: {self.age}')

my_car = Car('Toyota', 10, 'KA1230')
my_car.car_info()  # prints car info
```
### Using __dict__ and getattr for Attribute Access

Every Python object maintains its attributes in a dictionary. `object.__dict__` returns a dictionary of the object's attributes and their values.

Example:
```python
print(my_car.__dict__)
# Output: {'name': 'Toyota', 'age': 10, 'number': 'KA1230'}
```
This is useful for debugging or inspecting objects.

### Encapsulation with Getters and Setters

Directly accessing or modifying instance variables outside class methods is not ideal. Encapsulation principle recommends using getter and setter methods to control access and update of attributes.

Example:
```python
class Car:
    def __init__(self, age):
        self._age = age  # convention: '_' denotes protected attribute

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print('Invalid age')

my_car = Car(10)
print(my_car.get_age())  # 10
my_car.set_age(-5)        # Invalid age
print(my_car.get_age())  # 10
```
Protects the object's data integrity.

### Class Methods via @classmethod Decorator

Class methods operate on the class itself rather than instances. They receive the class as first argument, conventionally named `cls`.

Example:
```python
class Car:
    tax = 1000

    @classmethod
    def set_tax(cls, value):
        cls.tax = value

Car.set_tax(1500)
print(Car.tax)  # 1500

my_car = Car()
print(my_car.tax)  # 1500
```
Class methods must be called on the class, not instance.

### Example: Bank Account and Employee Class

The lecture covered practical examples involving classes with class variables, instance variables, and methods.

Bank Account Example:

* Class variable to track account count.
* `__init__` used to initialize account.
Employee Example:

* Company name as class variable (shared by all employees).
* Instance variables for individual employee data like name, position, salary.
* Generating employee IDs using helper function.
* Calculating annual salary.
* Tracking total employees using class variable and getattr().

This helps consolidate understanding of class design, variables, and methods.