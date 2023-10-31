Title: Operators in Python
Date: 2022-10-15 10:14
Modified: 2022-10-19 23:22
Category: python
tags: python

Operators perform computer operations on one or more python values or expression. The value the operator is operating on is called an operand. There are three different category of operators in python. They are:

1. Arithmetic operators
2. Comparison operators
3. Logical operators

### Arithmetic operators
This operators include the four basic arithmetic operations which are addition, subtraction, multiplication and division. Python can be used as a simple calculator because of these maths operators. Other operators that may not  be common to us are the modulus operator and the exponent or power operator.

| Name           | Operator| Example |
|:---------------|:--------|:--------|
| Addition       | +       | x + y   |
| Subtraction    | -       | x - y   |
| Multiplication | *       | x * y   |
| Division       | /       | x / y   |
| Exponentiation | **      | x**y    |
| Modulus        | %       | x % y   |

Example arithmetic operations:

```python
5**2 # raise 5 to the power of 2, 25

5 % 2 # returns the remainder of 5 / 2, 1
```

### Comparison Operators 
This operator compares two values and returns a boolean (True/False). There are 7 of them. One thing to note that in python the `==` comparison operator is the equal-to we all know and love, not to be confused with the assignment operator `=` used for binding a variable name to a value. The result of a comparison operation is always going to be a boolean value.

| Name                     | Operator| Example |
|:-------------------------|:--------|:--------|
| Equal                    | ==      | x == y  |
| Not equal                | !=      | x != y  |
| Greater than             | >       | x > y   |
| Less than                | <       | x < y   |
| Greater than or equal to | >=      | x >= y  |
| Less than or equal to    | <=      | x <= y  |

Example comparison operations:

```python
'ball' == 'ball' # True

5 > 4 # 5 greater than 4, True

15 < 10 # 15 less than 10, False
```
### Logical Operators
There are only three logical operators in python. Logical operators are used conditionally join values and expression to form a more complex expression. An understanding of truth table will give us an idea of the result of logical operations.

| Operator   | Description                                     | Example              |
|:-----------|:------------------------------------------------|:---------------------|
| and        | Returns True only when both statements are true  | x == 5 and y == 10   |
| or         | Returns True if any of the statements is true    | x == 5 or y == 10    |
| not        | Opposite of the result, True gives False        | not (x == 5)         |


##### Truth Table
| condition X | condition Y | X and Y | X or Y | not X 
|:------------|:------------|:--------|:-------|:-----
| False       | False       | False   | False  | True
| False       | True        | False   | True   | True
| True        | False       | False   | True   | False
| True        | True        | True    | True   | False

Example of logical operations

```python
5 == 5 and 5 > 2 # 5 equals 5 (True) and 5 greater than 2 (True)

5 != 2 or 5 < 4 # 5 not equals 2 (True) or 5 less than 4 (False)

5 < 2 and 5 > 2 # 5 less than 2 (False) and 5 greater than 2 (True)

not 5 == 5 # not 5 equals 5 (True)
```

These are the classes of operators in python and their operations. Understanding them will help build the foundation for you to become an expert in python.