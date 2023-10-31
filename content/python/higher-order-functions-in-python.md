Title: Higher Order Functions In Python
Date: 2023-02-21
category: python
tags: python, functional programming, higher-order functions
status: published

Higher order functions are functions that can be passed as an argument to a function or returned from a function as a value. It is a functional programming approach to solving problems. Python is a multi-paradigm language, meaning you can code it in different styles, from functional to object-oriented and even procedural. In this article, I will be explaining higher order functions and their applications in python.

To sum all integers in a given range we loop through it and sum each number at a time. This is an imperative method of solving the problem.

```python
counter = 0
total = 0
while counter < 5:
  total += counter
  counter += 1
print(total) # 10
```
A lot is going on, just to sum numbers in a range. When you look at the code at a glance you may not be able to determine what it does. Using a higher order function will make your code short. 

```python
total = sum(range(0, 5))
print(total) # 10
```
The `range` function is passed as an argument to the `sum` function. With this, we can understand that the `sum` function is a higher order function. When we compare the two examples above, you can tell that the one with the higher-order function has far less code. This is one of the benefits of higher order functions, they make your code straightforward and understandable. When a function is called it runs a series of steps in the background that is not visible to us. This is called abstraction. Abstraction hides the complex steps a function takes to solve a problem.


Higher order functions allow us to write dynamic code because we can abstract and change functions dynamically like values. Consider this problem, double, triple, and quadruple any given number.

```python
def multiply_by(n):
  def inner(weight):
    return weight * n
  return inner

double    = multiply_by(2)
triple    = multiply_by(3)
quadruple = multiply_by(4)

print(double(5)) # 10
print(triple(5)) # 15
print(quadruple(5)) # 20
```

The `multiply_by` function returns a function as a value, this allows us to dynamically change the number we want to multiply by.

Higher order functions are great for data processing. We will look at three major higher-order functions for handling data. With these functions, you don't have to write for-loops for an iterable.

- map
- filter
- reduce

### map

We can transform a list of elements using the map built-in function. The map operates on a list and returns a copy of the transformed list. The map function comes with the python interpreter but for education, we will implement our map function.

```python
def do_map(data_list, modify):
  copy = []
  for data in data_list:
    copy.append(modify(data))
  return copy

country_codes = ['usd', 'ngn', 'gbp', 'jny']
print(do_map(country_codes, str.upper)) # ['USD', 'NGN', 'GBP', 'JNY']
```

The `do_map` function takes an iterable and a function as an argument. In the example above I am making use of the `str.upper` function to transform all the elements in the list to upper case. You can also create your custom functions and it is not necessary to use python's built-in function.


### filter

When we filter a list we are selecting out elements that meet certain conditions to form a new list. For example, If you have a website along with a list of users' ages, You may want to only allow users above a certain age access to some exclusive content on your website. This problem can be solved elegantly using higher order functions.

```python
def do_filter(data_list, condition):
  copy = []
  for data in data_list:
    if condition(data):
      copy.append(data)
  return copy

def condition(data):
  if data < 18:
    return False
  return True

ages = [10, 11, 14, 22, 65, 18, 25, 44, 16]
print(do_filter(ages, condition)) # [22, 65, 18, 25, 44]
```

> The `map` and `filter` functions are built-in functions in the python interpreter.

### reduce

The reduce function operates on an iterable and returns a single value. It applies a function cumulatively to items inside of an iterable.

```python
def reduce(data_list, combine, start=0):
    current = start
    for data in data_list:
        current = combine(current, data)
    return current

def add(a, b):
    return a + b

print(reduce([1, 2, 3, 4], add)) # 10
```

### Lambda Functions

These are functions that are declared inline using the `lambda` keyword. They are referred to as anonymous functions because they do not have a name unlike functions created with the `def` keyword. Lambda functions allow us to write shorter code because we can just define the function we want to pass as an argument inside the function call. The examples above of map, filter, and reduce could be re-written using lambda functions

```python
from functools import reduce

country_codes = ['ngn', 'usd', 'gbp', 'jny']
ages = [22, 18, 14, 12, 19, 11]

map(lambda text: text.upper(), country_codes)

filter(lambda n: n < 18, ages)

reduce(lambda a, b: a + b, [1, 2, 3, 4])
```

The built-in map and filter functions will return an iterator object so to get the generated list we have to use the `list` function to convert it back to a list.

```python
list(map(lambda text: text.upper(), country_codes)) # ['NGN', 'USD', 'GBP', 'JNY']

list(filter(lambda n: n < 18, ages)) # [14, 12, 11]
```

If you have not started using higher order functions to write short and expressive code. I am inviting you to use them. If you want to learn more about functional programming in python you can visit the official python docs <a href="https://docs.python.org/3/howto/functional.html" target="_blank">here</a>.