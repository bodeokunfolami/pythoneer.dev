Title: Object Oriented Programming In Python
Date: 2022-11-26 19:45
tags: python, oop

Object oriented programming is a popular programming paradigm or style were code is represented as objects or associated with an object. Although python supports other programming styles everything created in python is an object. If you have learnt about the data types in python, It would please you to know that every time you create a variable with any of the python data types they are still legally known as python objects. Before we look at python objects lets look at what an object is generally.

The concept of Object-oriented programming was gotten from the study of objects and how they relate to our surrounding. I believe that everybody reading this post knows what objects are. An object is anything with definite characteristics. For example, your smart phone is an object. The characteristics of your smart phone includes 5000mah battery capacity, 6.3 inch display screen, 4gb ram etc. Now that we have established the phone is an object and we've seen its characteristics, lets look at it's functionality. The functionality simply means what the phone can do, there are a number of things that a smart phone can do but we can list some of them as such, making phone call, browse internet, play game etc. Take note of the phone as an object, its characteristics and functionality. In summary The three main concept of objects:

1. Object
2. Characteristics or attributes
3. Functionality or methods or functions

### The Object
Now that we know what an object is and we can determine its characteristics as well as its functionality lets look at python objects. Python objects follow the same principle. To create an object in python we make use of `class` keyword.

```python
class SmartPhone:
    pass
```

The code aboves create a smart phone object. This object does not yet characteristics, In python characteristics are attributes while functionality are referred to as methods or functions. Notice that the first letter of each word in the class name is in capital letter this is known as pascal casing and it is the convention for naming python classes. 

### Characteristics or Attributes
To create some class attributes we do the following

```python
class SmartPhone:
    name = 'Samsung Galaxy A30s'
    display = '6.4inch'
    capacity = '5000mah'
    ram = '4gb'
    status = 'on'
```

This is how we represent a smart phone object with its characteristics or attributes. our object has three attributes, display, capacity and ram. We now have a smart phone object that we can use in our code. You can see that attributes are variables that are created inside of a class. These variables (attributes) belongs to the `SmartPhone` object.

### Functionality or Methods
Methods are functions that perform computer operations within objects. Our smart phone method would be to make phone calls.

> All methods takes a default argument `self`. `self` is the object  passed as an argument so the attributes of the object can be accessed at the function level.

```python
class SmartPhone:
    # ...
    status = 'on'

    def power(self):
        if self.status == 'on':
            self.status = 'off'
        else:
            self.status = 'on'

    def call(self, number):
        return f'calling {number}'
```
The method `call` is a specific functionality of our `SmartPhone` object, its function is to make phone calls to other numbers and it takes `number` as an argument. The `power` method function as a power button to toggle the smart phone state.

We have a smart phone object that can do two things, power on/off and make phone calls. Am guessing it should'nt be called a smart phone 😗, but we can add more features to our smart phone.

### Initializing

> To initialize simply means to create. When we initialize an object we create it and we bring it to life. The object will be created with the parameters determined by it's `class`.

We have created our smart phone object, time to initialize it in your python code and make use of it. We initialize an object using parentheses *()* after the class name.

```python
phone = SmartPhone() # creates a smart phone object at memory location xxxxxx
```

we can access the attributes of the smart phone object using dot notation.

```python
phone.name # 'Samsung galaxy A30s'
phone.ram # '4gb'
phone.status # 'on'
```

The methods are called like normal python functions

```python
phone.status # 'on'
phone.power()
phone.status # 'off'
```

The power method toggles the power state of the object. each item the method is called if the status is off it will turn off and vice versa.

```python
phone.call('030-456-78') # 'calling 030-456-78'
```
The call method takes an argument, the number to call.

### Constructor

To create different smart phone objects, like Iphone 14 pro max object or a Samsung galaxy S21 ultra, we use a constructor function. If we want to have different types of smart phone we make use of a `constructor`. In object-oriented programming a constructor is a function that is called upon to create the object. Instead of hard coding the attributes they can be passed as arguments to the constructor to create them. In python the constructor function is always named `__init__`. Lets re create the smart phone class.

```python
class SmartPhone:
    def __init__(self, name, display, capacity, ram, status='off'):
        self.name = name
        self.display = display
        self.capacity = capacity
        self.ram = ram
        self.status = status
    #...
```
The line `self.name = name` converts the name variable into a class attribute. Now lets create multiple smart phone objects with different attributes 

```python
samsung = SmartPhone('Samsung Galaxy S22 Ultra', '6.8inch', '5000mah', '12gb')
iphone = SmartPhone('Iphone 14 Pro Max', '6.7inch', '4323mah', '6gb')
```
We have created two smart phone objects, its like having two phones we can use them for different purposes.

```python
samsung.display # '6.8'
iphone.display # '6.7'
```
We can also use the `power` method in the iphone object to turn it on.

```python
iphone.power()
iphone.status # 'on'
samsung.status # 'off'
```

This is object-oriented programming in python. Its not that hard to understand because almost every one can relate with the concept easily. In the next article we will look at other concepts in OOP like inheritance, abstraction etc.
