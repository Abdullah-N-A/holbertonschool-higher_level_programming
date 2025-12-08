Python Projects Overview
| # | Folder                         | Objective                                | Concepts Covered                                                                                                                        | Example                                                                                        |
| - | ------------------------------ | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| 1 | python-hello_world             | Learn Python basics and script execution | `print()`, comments, basic I/O                                                                                                          | `print("Hello, World!")`                                                                       |
| 2 | python-if_else_loops_functions | Learn control flow and functions         | `if`, `else`, `elif`, `for`, `while`, function definition, return values                                                                | `def add(a, b): return a + b`                                                                  |
| 3 | python-import_modules          | Learn modules and imports                | Importing standard and custom modules, `from ... import ...`                                                                            | `import math; print(math.sqrt(16))`                                                            |
| 4 | python-data_structures         | Work with basic Python data structures   | Lists, tuples, sets, dictionaries, indexing, slicing, iteration                                                                         | `my_list = [1, 2, 3]; print(my_list[0])`                                                       |
| 5 | python-more_data_structures    | Advanced data structures                 | Nested lists/dicts, comprehensions, set operations                                                                                      | `squared = [x**2 for x in range(5)]`                                                           |
| 6 | python-exceptions              | Handle errors gracefully                 | `try`, `except`, `finally`, `raise`, custom exceptions                                                                                  | `try: 1/0 except ZeroDivisionError: print("Error")`                                            |
| 7 | python-test_driven_development | Learn Test-Driven Development (TDD)      | `unittest` framework, writing tests before code                                                                                         | `import unittest`                                                                              |
| 8 | python-classes                 | Learn basic Object-Oriented Programming  | Classes, objects, instance/class attributes, methods, `__init__`, `self`                                                                | `class Square: pass; s = Square(); print(type(s))`                                             |
| 9 | python-more_classes            | Advanced OOP concepts                    | Inheritance, private/protected attributes, class vs instance variables, method overriding, decorators (`@classmethod`, `@staticmethod`) | `class Robot: population=0; def __init__(self, name): self.name = name; Robot.population += 1` |

✅ Notes:

The repository is structured from beginner to advanced topics, starting with basic Python scripts and ending with advanced Object-Oriented Programming.

python-classes and python-more_classes are the last modules and focus on applying OOP in real projects.

Each folder contains multiple small exercises or scripts to practice the concepts.
