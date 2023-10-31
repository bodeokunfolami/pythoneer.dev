Title: Object Oriented Programming In Python: Part 2
Date: 2022-12-01 19:00
tags: python, oop
status: published

In the last article we looked act object oriented programming in python, I explained what objects, attributes and methods or functions are the fundamentals of OOP. In this article we will be looking at four important concepts of object-oriented programming.

1. Inheritance
2. Abstraction
3. Encapsulation
4. Polymorphism

### Inheritance
Inheritance involves two or more classes, The parent class and the child class. The child class has attributes and functions of the parent class because it 'inherits' from the parent class. For example, we have a parent class 'Foo' and child class 'Bar'.

```python
class Foo():
    def f1(self):
        return 'inside parent class'

class Bar(Foo):
    def f2(self):
        return 'inside child class'

bar = Bar()

bar.f1() # inside parent class
bar.f2() # inside child class
```
the function `f1()` was defined inside of the `Foo` class but since `Bar` inherits from `Foo` it has access to the methods defined in the parent class Bar.

### Abstraction
Abstract is a concept that enables you to use a technology without having to understand the complexity of its design and how it works. Abstraction is an interface that help use complex components without understanding it. Abstraction is everywhere, for example, a person can drive a car without understanding how the car was designed or what makes it move. In object-oriented programming we can easily apply the concept on abstraction were developers can use certain classes objects and method without understanding how it works internally. One of the main advantages of abstraction is makes building large applications less cumbersome. Django is a python web framework that heavily rely on this concept for rapid web development.

### Encapsulation
This is the process of wrapping data and functions that operates on the data into a single entity. It restricts access to some components of an object so users can not access attributes of a particular object. Encapsulation enables objects to be implemented with more flexibility.

```python
class Person:
    def __init__(self, name=''):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def __set_name(self, name):
        self.name = name
```
In the code above the `__set_name` method is restricted or private and cannot be accessed by users only the `get_name` is accessible.

### Polymorphism
This is the ability for an object, variable or function to exists in different forms. An advantage polymorphism is that allows the reuse of code once it has been written and tested. It also helps compose powerful abstractions from simpler ones.