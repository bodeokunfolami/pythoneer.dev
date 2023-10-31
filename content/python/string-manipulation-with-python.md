Title: Python String Manipulation
Date: 2022-10-26 15:33
Category: python
status: published
tags: python

String is one of the primitive types in python. Manipulating strings is useful in different aspects of programming. String has a data structure similar to that of lists. A string is stored as a character sequence in memory. The null pointer denotes the end of a string in memory.

<center>![python-string-alt]({static}/images/string.png)</center>

We can get a single character from a string using its index. to get the **r** in *"first"* we use its index 2. just like lists we can index string to access the individual character it consist of.

```python
lang = 'first'
lang[2] # gets 'r'
```

### String Methods

Methods are functions that are attributes of a python type or object.Strings in python support a handful of methods that can be used to perform operations on them. Python comes with a built-in function for finding the length of a string. you can also convert a string from lowercase to uppercase and vise versa. The capitalize method changes the first character in the word to uppercase.

```python
>>> len(lang)
5
>>> lang.upper()
'FIRST'
>>> lang.lower()
'first'
>>> lang.capitalize()
'First'
```

> Remember that the string type is immutable. Once a string is created it cannot be changed. The string methods *upper* and *lower* creates a new string entirely separate from the one previously declared.

The `replace` string method is used to replace a character or substring from a string. The replace method is very useful.

```python
obj = 'bed'
obj = obj.replace('d', 'g')
obj # 'beg'
```

The string 'bed' changed to 'beg' after replacing the 'd' with a 'g'. If you want to get rid of the trailing white spaces in a string the `strip()` method is used.

```python
>>> name = '  Adeyemi    '
>>> name.strip()
'Adeyemi' 
```

A string can been transformed to a list with the `split()` method that takes a separator as an argument.

```python
>>> sentence = 'I am a boy walking down the street'
>>> sentence.split(' ')
['I', 'am', 'a', 'boy', 'walking', 'down', 'the', 'street']
```

In the example above the separator is a whitespace, We can also use comma or any other type of punctuations.

```python
>>> items = 'bag,shoe,shirt'
>>> items.split(',')
['bag', 'shoe', 'shirt']
```

The above example is usefully when working with csv files.

Python comes with several other string methods that have their use cases. if you want to see a full list of the string method use the *dir* built-in function.

```python
dir(str) # prints a list of all the available string method
```

### String Concatenation
In python two or more strings can be joined together through the process of string concatenation. The simplest way to join python strings is using the addition (+) operator. The operator supports joining multiple strings together.

```python
>>> 'Hello' + 'World'
'HelloWorld'
```

A more modern approach is to use f-strings. F-strings eliminates the need for the addition operator. It is a cleaner way to join strings together in python.

```python
first_name = "John"
last_name = "Wick"
full_name = f"{first_name} {last_name}"
full_name # gets 'John Wick'
```

> Take note of the **f** before the quotes. The f converts a python string to a format string 

Variables can be directly placed inside of the string using curl brackets. This method is cleaner than using the addition operator.

### String Slicing
In python you can get a parts of a string, substrings using string slicing. String slicing can be used to extract text from a string.

String slicing format
```plaintext
string[start:end]
```

Just like indexing a list, we use square brackets. we specify a start index and an end index. The substring will include only the characters within the index specified. Python substring does not include the character of the end index. To get substring of the word *image.jpg*.

<center>![python-string2-alt]({static}/images/string2.png)</center>

```python
filename = 'image.jpg'
ext = filename[6:9]
ext # 'jpg'
name = filename[0:5]
name # 'image'
```

In the example above string slicing was use to separate the name of the file and its extension into different substrings. Since we are starting at the beginning of string to get the name of the file and stopping at the end to get the extension, in python you can exclude the start index if your substring is going to include the first character and you can exclude the end index if your substring will also contain the last character in the string. Lets rewrite the example above.

```python
filename = 'image.jpg'
ext = filename = [6:]
name = filename = [:5]
ext # 'jpg'
name # 'image'
```

Here is a quick example for you: Get the substring `'age'` from the `'image.jpg'` string. What is the start and end index. Try to solve it using the diagram above before you see the solution below.

The solution to the problem above is:

```python
filename = 'image.jpg'
sub = filename[2:5]
sub # 'age'
```

The start index is 2 and the end index is 5. the characters in the string will only contain index 2,3 and 4 which corresponds to `'age'`.

If you've gotten to the end of this post you now have the power to bend python strings to your will. You can show off your string manipulating skills to your friends and family now.