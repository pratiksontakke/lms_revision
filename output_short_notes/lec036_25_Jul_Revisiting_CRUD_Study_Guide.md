 ### 🧾 Plain Summary
In this lecture, we covered essential concepts in object-oriented programming (OOP) such as inheritance, method overriding, class variables vs instance variables, static methods, class methods, property decorators, and more. Key takeaways include understanding how to use `super()` for parent class method calls, the difference between class and instance attributes, and how to effectively implement getter and setter properties using decorators. We also explored advanced OOP concepts like multiple inheritance and method resolution order (MRO).

### 📝 Improved Summary
# Object-Oriented Programming in Python

## Inheritance
Inheritance allows a subclass to inherit from a superclass, promoting code reuse and reducing redundancy. The `super()` function is used to call methods of the superclass within the subclass.

### Key Points:
1. **Single Inheritance**: A subclass inherits from one superclass.
2. **Multiple Inheritance**: A subclass can inherit from multiple superclasses, but this can lead to complex method resolution order (MRO).
3. **Method Overriding**: Subclasses can override methods of the superclass. Use `super()` to call superclass methods.

## Class Variables vs Instance Variables
- **Class Variables**: Shared among all instances of a class and defined within the class but outside any instance method.
- **Instance Variables**: Unique to each instance and defined in the constructor (`__init__`).

### Example:
```python
class Student:
    school_name = "Python Academy"  # Class variable
    passing_grade = 60  # Class variable
    
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age  # Instance variable
```

## Static Methods
Static methods are utility functions defined within a class and do not depend on instance or class data. They can be called via the class or an instance.

### Example:
```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
```

## Class Methods
Class methods work with the class itself and are defined using `@classmethod`. They can modify class state or act as alternative constructors.

### Example:
```python
class Employee:
    company_name = "Masai School"
    
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        
    @classmethod
    def from_string(cls, emp_str):
        name, position, salary = emp_str.split('-')
        return cls(name, position, int(salary))
```

## Property Decorators (Getters and Setters)
Property decorators provide a way to define methods that can be accessed like attributes.

### Example:
```python
class House:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    
    @property
    def area(self):
        return self._length * self._width
    
    @area.setter
    def area(self, value):
        self._length = 2 * value
```

## Important Concepts
- **Inheritance**: Subclasses can inherit from superclasses to reuse code.
- **Method Overriding**: Subclasses can override methods of the superclass.
- **Class Variables vs Instance Variables**: Class variables are shared among all instances, while instance variables are unique to each instance.
- **Static Methods**: Utility functions within a class that do not depend on instance or class data.
- **Class Methods**: Methods that work with the class itself and can modify class state.
- **Property Decorators**: Allow methods to be accessed like attributes through getter and setter methods.

### Interview Questions & Answers
1. What is inheritance in Python?
   - Inheritance allows a subclass to inherit from a superclass, promoting code reuse and reducing redundancy.
2. How do you call a method of the superclass within a subclass?
   - Use `super()` to call methods of the superclass.
3. Define class variables and instance variables.
   - Class variables are shared among all instances of a class, while instance variables are unique to each instance.
4. What is a static method in Python?
   - A static method is a utility function defined within a class that does not depend on instance or class data.
5. How do you define a getter and setter using property decorators?
   - Use `@property` for the getter and `@<property name>.setter` for the setter.

These concepts are fundamental to understanding object-oriented programming in Python and will be crucial for both interview preparation and practical application of OOP principles.