Title: Understanding Variables and Data Types in Python
Date: 2022-10-14 11:36
Modified: 2022-10-19 23:36
Category: python
tags: python

Python is a general purpose, interpreted computer programing language. Programs written in python have zero compile time because the code are executed or interpreted at the program runtime. When you install python on your computer it comes with a software called the python interpreter. The python interpreter runs python code like a command line interface. We can write python code in a python interpreter and it would run the code.

```python
>>> 5
5
>>> "Ade"
'Ade'
```

The interpreter takes a value 5 and 'Ade' and returns them back without throwing any errors signifying that the code is correct and it was executed. Yes, `5` is a value and `'Ade'` is also a python value. A value in python is a useful information that the interpreter understands. Writing out the values literally make them useful just once. But most of the time, when writing code we often want to make use of values that we previously declared at later points in our code. This is where variables comes in.

A variable is a location in memory that stores a value. variables associates a name to a memory address where the value is stored. In python we assign variables with the assignment operator `=`. The left side of the operator is the name of the variable and the right side of it is it's value. Lets look at our example again.

```python
>>> num = 5 # assign the value 5 to the variable num
>>> num # get the value of the num variable
5
>>> name = 'Ade' # assign the value 'Ade' to the variable name
>>> name # get the value of the name variable
'Ade'
```

There are some rules to follow when naming variables, they are:

1. You must not use any of python reserved keyword to name a variable.
2. Variables in python cannot start with a number but may contain it.
3. Variables must not contain special character except for underscore.
4. Variables are case-sensitive (ball, Ball, BALL are different).

The interpreter will not just accept any kind of value you type in it, The class of data that can be input to the interpreter is known as data type. There are four primitive data types in python which are:

1. String
2. Integer
3. Boolean
4. Float

These are the four basic data types in python. All values in python are one of these for types.

### String
A string is a sequence of letters, numbers or special characters contained in a single or double quote. the string type support different kinds of operations which falls under the topic of string manipulation. The string type is immutable, that means that once created it cannot be modified. In the example above `name = 'Ade'` is a string type. Lets look at one more.

```python
text = 'my name John and I am 13 years old'
type(text) # <class 'str'>
```

Even though that looks like an integer because it has quotes python will always read it as a string.


### Integer
An integer includes all numbers on a number line, which are all positive and negative whole numbers. Integers support the four arithmetic operations which include addition, subtraction, multiplication and division. It also support the power operation (**) and the modulus operation (%).

```python
type(1000) # <class 'int'>
```

### Float
The float type support all the operations an integer support, the only difference is that they are fractional numbers. The are a separate types because the computer perform mathematical operations on them differently.

```python
type(165.35) # <class 'float'>
```

### Boolean
The boolean data type represents one of two value, `True` or `False`. The result of a comparison operation is a boolean value.

```python
type(True) # <class 'bool'>
type(False) # <class 'bool'>
```


The different types support different operations. When you try to perform an integer operation on a string it will raise a *TypeError*. It is important to know the different types and how to rightly use them in your code. A *NameError* occurs when you try to type a value that does not belong to any of the four data types above.

```python
>>> hello
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'hello' is not defined. Did you mean: 'help'?
```

Apart from the four primitive types there are other data types. The primitive data types can only store a single value in a variable. The collection data types can store multiple values in a single variable:

1. Lists
2. Dictionaries
3. Set
4. Tuple


### Lists
A python list is a sequence of values that can either be any of the four primitive type. A list is created or initialized with square brackets. Items in a list are separated by a comma.

```python
fruits = ['orange', 10, 'banana', 5]
```

The variable `fruits` has four items in it. These four items are numbered with index 0 to the length of fruits minus one `(len(fruits) - 1)`. A list of four items is numbered from 0 to 3. To access any element we make use of the index.

```python
>>> fruits[0] # get the first element using index 0
'orange'
>>> fruits[3] # get the last element with index 3
5
```

### Dictionaries
Dictionaries store items in key-value pairs. Like a list you can store multiple values in a python dictionary. Values have keys that are used to access them later on. The keys are similar indexes in lists, the only differences is they are created by the programmer and they can be any of python primitive types.

```python
person = {
    'name': 'Olamilekan',
    'age': 23,
    'date_of_birth': '1999-05-20'
}
```

The keys in the dictionary are on the left side of the colon (:) while the values are on the right side. The key is used to get a value just the way index is used to get an item in a list.

```python
>>> person['name']
'Olamilekan'
>>> person['age']
23
>>> person['date_of_birth']
'1999-05-20'
```
### Tuple 
A tuple is a list that cannot be modified. A tuple is created using brackets instead of square brackets like lists. A tuple is immutable. The values in it cannot be changed.

```python
friuts = ('apple', 20, 'orange')
```
Python will raise a *TypeError* when you attempt to change a tuple value. This does not occur in dictionaries and list.

```python
>>> fruits[0] = 'banana'
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
```

### Set
A python set is a list of items that cannot not be changed. Items in a set are not the same. Items can be removed from a set and added to the set but the item itself cannot be changed. A set is initialized with curly braces.

```python
fruits = {'apple', 'banana', 'orange'}
fruits.pop() # remove the first item from the set
fruits # ['banana', 'orange']
```

These are all the data types in python. Understanding the class of data in python and the operations they support will give you a deeper understanding of python programing language.