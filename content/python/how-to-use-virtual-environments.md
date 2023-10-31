Title: How to Create a Virtual Environment In Python?
Date: 2022-12-07 19:00
tags: python, virtualenv, venv

### What is a Virtual Environment

A virtual environment in python is a tool that isolates packages in your project so it does not conflict with other python packages. For example, in our main python environment, we have the python package `pygame==1.9.5` which we installed and used for Project A, and we want to start another project Project B that requires `pygame==2.1.2`. If we install another version of the pygame package python will not be able to differentiate between them, hence the reason for virtual environments.

<center>
![img-venv-diagram]({static}/images/venv-diagram.png)
</center>

to see all the packages in your main python environment run the command.

```bash
$ pip freeze
```
when you run this command you should see a list of packages with their version numbers.

### Why You Should Use a Virtual Environment 
It is recommended to use virtual environments when working on python projects but here are a few reasons why you should use them.

1. They help manage your project dependencies across multiple platforms
2. They prevent confusion in the future when newer versions of packages are released.
3. Keep the main python environment clean with only the necessary packages.

### Creating a Virtual Environment
Python has a built-in module for creating virtual environments. To create a virtual environment run the following command inside your project folder.

```bash
$ python -m venv .venv
```
Once the virtual environment has been created the final step will be to activate it. To activate it we run the following command in your project root folder.

for Linux/macOS

```bash
source .venv/bin/activate
```

for windows; cmd
```bash
./.venv/scripts/activate
```
for windows; git bash
```bash
source .venv/scripts/activate
```
Enter the command that corresponds to your operating system and it will activate the virtual environment that was created. The virtual environment is like the main python environment only without any packages. When you run `pip freeze` you will note that it has no packages installed inside of it.

The structure of a python project using a virtual environment will usually look like this:

```treeview
project_b/
|-- .venv/
|    |-- bin/
|    |-- lib/
|    |-- .gitignore
|    `-- pyvenv.cfg
|-- script.py
|-- main.py
```

All the packages installed inside of the probject_b virtual environment will be used for project_b only and does not affect packages of other projects.