Here are the full lecture notes in markdown format:

**Python Programming**

### Decorators

* A decorator is a function that takes another function as an argument and returns a new function that adds some kind of functionality.
* Example:
```python
def make_bold(func):
    def wrapper():
        result = func()
        return f"**{result}**"
    return wrapper

@make_bold
def greet():
    return "Hello World"

print(greet())  # Output: **Hello World**
```
### Property Decorators (Getters and Setters)

* `@property` decorator lets you define a method that you can access like an attribute (getter).
* `@<property name>.setter` decorator lets you define the setter method to set an attribute.
* Example:
```python
class House:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width

    @area.setter
    def area(self, value):
        # For example, set length to twice the input area
        self.length = 2 * value

house = House(10, 5)
print(house.area)  # Output: 50
house.area = 60
print(house.length)  # Output: 120
```
### Class Variables vs Instance Variables

* Class variables are shared across all instances of a class.
* Instance variables are unique to each instance.
* Example:
```python
class Student:
    school_name = "Python Academy"  # Class variable
    passing_grade = 60  # Class variable
    total_students = 0  # Class variable

    def __init__(self, name, age, grade):
        self.name = name  # Instance variable
        self.age = age  # Instance variable
        self.grade = grade  # Instance variable
        Student.total_students += 1  # Update class variable

s1 = Student("Alice", 15, 70)
s2 = Student("Bob", 16, 80)

print(Student.school_name)  # Access class variable
print(s1.name)  # Access instance variable
print(Student.total_students)  # Output: 2
```
### Static Methods

* Static methods define utility functions inside a class that don't depend on instance (self) or class data (cls).
* Example:
```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0

print(MathUtils.add(2, 3))  # Output: 5
print(MathUtils.is_even(4))  # Output: True
```
### Class Methods

* Class methods work with the class itself rather than instance objects.
* Example:
```python
class Employee:
    company_name = "Masai School"
    total_employees = 0

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        Employee.total_employees += 1

    @classmethod
    def from_string(cls, emp_str):
        name, position, salary = emp_str.split('-')
        return cls(name, position, int(salary))

    @classmethod
    def get_company_info(cls):
        return f"Company: {cls.company_name}, Total Employees: {cls.total_employees}"

# Creating object using alternate constructor
emp1 = Employee.from_string("John-Developer-70000")
print(emp1.name)  # Output: John
print(Employee.get_company_info())  # Output: Company: Masai School, Total Employees: 1
```
### Inheritance

* Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class).
* Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):  # Inheriting Person
    def __init__(self, name, age, course):
        super().__init__(name, age)  # Call parent constructor
        self.course = course

student = Student("Alice", 21, "Math")
print(student.name)  # Output: Alice
print(student.course)  # Output: Math
```
### Method Overriding

* Method overriding occurs when a child class defines a method with the same name as a method in the parent class.
* Example:
```python
class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"


# Usage
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())
# Output:
# Bark
# Meow
# Some generic sound
```
### Multiple Inheritance and Method Resolution Order (MRO)

* Multiple inheritance allows a class to inherit from more than one parent class.
* Python uses the Method Resolution Order (MRO) to determine the order of method calls when multiple parent classes define the same method.
* Example:
```python
class Flyable:
    def move(self):
        return "Flying"

class Swimmable:
    def move(self):
        return "Swimming"

class Duck(Flyable, Swimmable):
    pass

duck = Duck()
print(duck.move())  # Output: Flying (because Flyable is first parent)

print(Duck.__mro__)
```
I hope this helps! Let me know if you have any questions or need further clarification.