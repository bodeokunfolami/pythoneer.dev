Title: Build a Password Generator CLI With Python
Date: 2022-11-25 20:16
tags: python, cli
status: published

To build a password generator command line interface (cli) with python, first create a virtual environment and install click. click is a python package for creating command line utility applications. A command line interface application is a software that is run as a command on terminal or command prompt that performs computer operations.

Install click package with pip
```bash
$ pip install click
```

### Command line utility
To create the command line interface create a file in your project folder called main.py and type the following code

```python
import click

@click.command()
@click.argument('name')
def main(name):
    click.echo(f'Hello {name}')

if __name__ == '__main__':
    main()
```

This code above is a basic usage of click. The two decorators above changes an ordinary python function to command line utility that receives argument and outputs it to console.

```python
@click.command()
```
The python decorator above turns the function into a command line utility that can be invoked with terminal or command prompt.

```python
@click.argument('name')
```
The `@click.argument` decorator takes in a variable `name` as argument. arguments are values passed when the command is invoked in terminal.

```bash
$ python main.py Ade
Hello Ade
```
The argument is 'Ade' which is the name parameter in the main function. The next feature of a command line utility is the ability to pass flags or options. The presence of options in a CLI modify the output of a command. In our `main.py` rewrite the main function to include the following.

```python
import click

@click.command()
@click.option('--length', default=8, help='length of password')
@click.option('--digit/--no-digit', default=False, help='include numbers in password')
def main(length, digit):
    click.echo(length)
    click.echo(digit)

if __name__ == '__main__':
    main()
```

Run the program with the option
```bash
$ python main.py --length 10 --digit
10
True
```
This will output 10 and in case the option is not given the default will be used. The second option is a boolean flag that defaults to `False` if it was not used in the command.

```python
@click.option('--length', default=8, help='length of password')
```
The above decorator allows the command to be invoked with options. Options are parameters of a cli that can change based on the user input. the decorator takes *'--length'* as an option, with a default value of 8. The default value is used if the option is not specified in the command line.

```python
@click.option('--digit/--no-digit', default=False, help='include numbers in password')
```
This is a boolean option or flag to include numbers or exclude them when generating our password.

### Generating password
Now that we have our command line interface working lets create a function to that will generate a random string of characters. in your main.py add

```python
import random
import string
import click

def generate_password(length, is_digit):
    '''This function returns randomly generated string'''
    seed = string.ascii_letters
    if is_digit: # if the number flag was raised add numbers to the seed
        seed += string.digits

    return str('').join([random.choice(seed) for i in range(length)])
# ...
```

`generate_password` takes length as an argument and uses it to generate a string of random letters with length of the length variable. To use the function in our cli we just simply call the function passing length as argument.

```python
[random.choice(string.ascii_letters) for i in range(length)]
```
This is a python list comprehension for generating a list on random ascii letters the size of the length variable.

```python
str('').join([random.choice(string.ascii_letters) for i in range(length)])
```
The `str('').join()` method will combine all the letters in the list into a single string that can be used as a password.

Everything combined together will give:

```python
import random
import string
import click

def generate_password(length, is_digit):
    '''This function returns randomly generated string'''
    seed = string.ascii_letters
    if is_digit:
        seed += string.digits
    return str('').join([random.choice(seed) for i in range(length)])

@click.command()
@click.option('--length', default=8, help='length of password')
@click.option('--digit/--no-digit', default=False, help='include numbers in password')
def main(length, digit):
    password = generate_password(length, digit)
    click.echo(f'Password: {password}')

if __name__ == '__main__':
    main()
```
Running the command with the options will give:

```bash
$ python main.py --length 16 --digit
Password: C6Cdcvbax5nYcc2d
```
