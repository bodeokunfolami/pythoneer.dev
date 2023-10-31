Title: Setup Windows 11 for Python Development
Date: 2022-12-20 16:50
tags: python, windows

Python is an interpreted, general purpose, high level programming language. It is a popular language for data science, web development etc. It has an easy to understand syntax that makes it an excellent choice for beginner programmers.

In this tutorial, we'll learn how to setup python on a windows 11 machine. This tutorial also works for other versions of windows.

### Step 1: Installing Python
To install the python, download the latest version from <a href="https://python.org/downloads" target="_blank">python.org</a>

<center><img src="{static}/images/download-python.png" alt="download-python" width="90%" class="shadow"><center>

Navigate to your downloads folder and double click on the installer to launch. Once the installer is running make sure to click "Add python.exe to PATH" at the bottom corner of the installer window then click "Install Now".

<center><img src="{static}/images/installing-python-1.png" alt="installing-python-1" width="90%"></center>

> If you do not click "Add python.exe to PATH" it will be difficult to install python packages in the future, if you miss this step you can uninstall and install python again.

To verify that python installed successfully and has been added to your system path, open windows command prompt and type the command `python --version`. You should see an output of the version of python installed on your computer.

At this stage we have successfully installed python on our computer. The next step is to decide what we will use to write and run our python code. We could use a IDE or a normal text editor. For this tutorial we will be using a text editor but if you want to use an IDE you can use <a href="https://jetbrains.com/pycharm/download/" target="_blank">PyCharm IDE</a>

### Step 2: Download Git
In this step we will download git. Git is a version control software for managing multiple versions of your application. But the main reason we are downloading git is so we can use git bash which is a unix like command shell. Git bash is better for software development than the default windows shell (CMD). To download git head to <a href="https://git-scm.com/downloads" target="_blank">git-scm.com</a>

<center><img src="{static}/images/download-git.png" alt="download-git" width="90%"></center>

Run the installer to install git on your computer.

### Step 3: Download Vscode Text Editor
We will be using visual studio code as our text editor to write our code. Vscode is the worlds most popular text editor with a large community, which makes it an ideal choice amongst software developers for coding. You can download the latest version of vscode from <a target='_blank' href='https://code.visualstudio.com'>code.visualstudio.com</a>

<center><img src="{static}/images/download-vscode.png" alt="download-vscode" width="90%"></center>

Follow the installation steps to install visual studio code on your computer. Once visual studio has been installed, It will launch the default editor window.

<center><img src="{static}/images/vscode-window.png" alt="vscode-window" width="90%"></center>

### Step 4: Configure Vscode for Python Development

In this step we are going to install a python extension inside of vscode. This extension lets you run your python code with vscode. To install the extension click on the extension tab on the sidebar and use the search bar to search 'python'. The first result of that search is the extension to install.

<center><img src="{static}/images/download-python-extension.png" alt="download-python-extension" width="90%"></center>

### Last Step: Set Git Bash as Default Profile
Vscode comes with an built-in terminal shell that defaults to windows power shell. We are going to change it to git bash. To change the default terminal profile to git bash:

1. Click on the settings icon
2. Click on "Command Palette..."
3. Type "select profile" and click on the option that appear below
4. Select Git bash

<center><img src="{static}/images/select-default-profile.png" alt="select-default-profile" width="90%"></center>

### Finally
We have setup our computer for windows development. The next thing to do is to write a python script and run with vscode. Create a new file and save it as `hello.py` and type the following `print('Hello World')`. To run the script click on the play icon on the upper right corner of the text editor window.

<center><img src="{static}/images/run-python-script.png" alt="run-python-script" width="90%"></center>