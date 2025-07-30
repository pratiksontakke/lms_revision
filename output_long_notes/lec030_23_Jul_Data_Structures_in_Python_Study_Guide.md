Here are the full lecture notes in markdown format:

**Human: Technical Note-Taker**
=============================

### Introduction

* World-class technical note-taker trained to convert full lectures into complete notes
* Focus on understanding and summarizing key concepts, formulas, and ideas

### Lists in Python

#### Creating Lists

* `[]` syntax for creating lists
* Example: `fruits = ['apple', 'banana', 'cherry']`

#### Accessing List Elements

* Indexing: `fruits[0]` returns `'apple'`
* Negative indexing: `fruits[-1]` returns `'cherry'`
* Slicing: `fruits[1:3]` returns `['banana', 'cherry']`

#### Adding and Updating Elements

* `append()` method for adding elements at the end
* `extend()` method for adding multiple elements from another list
* Example: `shopping_cart = ['milk', 'bread']; shopping_cart.append('eggs'); shopping_cart.extend(['butter', 'cheese'])`

#### Removing Elements

* `remove(value)` method for removing an element by value
* `pop()` method for removing the last element or element at a specific index
* Example: `inventory = ['apple', 'banana', 'cherry']; inventory.pop('banana'); del inventory[0]`

### Tuples in Python

#### Creating Tuples

* `()` syntax for creating tuples
* Example: `point = (10, 20)`

#### Accessing Tuple Elements

* Indexing: `point[0]` returns `10`
* Negative indexing: `point[-1]` returns `20`
* Slicing: `point[1:]` returns `(20,)`

#### Tuple Unpacking

* Example: `data = (1, 2, 3, 4, 5); first, *middle, last = data; print(first)   # 1; print(middle)  # [2, 3, 4]; print(last)    # 5`

### Dictionaries in Python

#### Creating Dictionaries

* `{}` syntax for creating dictionaries
* Example: `person = {'name': 'Raj', 'age': 20}; mixed_dict = {1: 'one', 'two': 2, (3, 4): 'tuple key'}`

#### Accessing Dictionary Elements

* Key indexing: `person['name']` returns `'Raj'`
* Get method: `person.get('age')` returns `20; person.get('gender')` returns `None`
* Example: `inventory = {'apple': 50, 'banana': 30}; print(inventory['apple'])          # 50`

#### Adding and Updating Elements

* `update()` method for bulk updating
* Example: `inventory.update({'apple': 60, 'pear': 10})`

#### Removing Elements

* `pop()` method for removing the last inserted item (Python 3.7+)
* Example: `inventory.pop('banana')`
* `del` statement for deleting a key-value pair
* Example: `del inventory['apple']`

### Dictionary Views

* `keys()`: Returns keys as a view
* `values()`: Returns values
* `items()`: Returns key-value pairs as tuples
* Example: `print(list(inventory.keys())); print(list(inventory.values())); print(list(inventory.items()))`

### Iterating Over Dictionaries

* For loop with `keys()` or `items()` method
* Example: `for key in inventory: print(key, inventory[key])`
* Or using dictionary comprehension
* Example: `{k: v for k, v in inventory.items()}`

### Useful Built-in Functions: enumerate and zip

#### enumerate(iterable)

* Adds a counter to an iterable and returns it as an enumerate object
* Example: `fruits = ['apple', 'banana', 'cherry']; for index, fruit in enumerate(fruits): print(index, fruit)`

#### zip(*iterables)

* Aggregates elements from multiple iterables and returns an iterator of tuples
* Example: `names = ['Alice', 'Bob', 'Charlie']; ages = [25, 30, 35]; cities = ['NY', 'LA', 'Chicago']; for name, age, city in zip(names, ages, cities): print(name, age, city)`

### Unpacking Arguments with * and **

#### Tuple Unpacking

* Example: `def greet(name, age, city): print(f"Hello {name}, you are {age} years old from {city}."); person = ('Alice', 30, 'LA'); greet(*person)   # Equivalent to greet('Alice', 30, 'LA')`

#### Dictionary Unpacking

* Example: `def greet(**person_data): print(f"Hello {person_data['name']}, you are {person_data['age']} years old from {person_data['city']}."); person_data = {'name': 'Bob', 'age': 25, 'city': 'NY'}; greet(**person_data)`

Note: For dictionary unpacking, parameter names in function should match the dictionary keys.