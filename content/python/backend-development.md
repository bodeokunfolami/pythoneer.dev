Title: Back-end Development: Flask vs Django
Date: 2022-10-12 12:57
Modified: 2022-11-25 23:10
tags: python, web development, flask, django

### What is a server?
A server is a computer in any location on the planet that provides computational logic and operations remotely to multiple devices.

### What is back-end development?
This is the process of developing software handles data of a web application. Without the back-end a website is just static HTML and CSS. Think of a website back-end as instructions or code that determines how data is rendered in the browser in the form of markup.The back-end contains the logic for processing data gotten interacting with website. Back-end development is also known as server-side programming. The back-end of a website is the reason why you can make a post on facebook, order an item from an e-commerce website etc. The back-end interacts with a database to store data from a website.

There are different server-side programming languages such as Python, Javascript (Nodejs), Ruby, Go etc. These languages can be used to build web application. Python is one of the best languages for web development, because of its simple syntax that almost resembles plain english. Despite it's simplicity it is a very powerful language.

### What is a Web Framework?
A web framework is a software that makes building websites easy. Python has many web frameworks but in this tutorial we will be looking at two of the most popular.

There are two main frameworks used in python for building web applications. The first is Django and the second Flask. Django is a robust framework with many features while flask can be considered as a micro framework. Django has a pre-determined structure and pattern of writing web apps and flask makes it very simple to get a web application up and running.

### The Django Web Framework
With django you can build applications that are robust and secure, it's structure makes it easy to build scalable web apps. Django is what we call a full-stack framework, it is structured into the Model-View-Template architecture. Models determines data structure. The model through the object relation mapper (ORM) let you query database tables in python instead of raw SQL. The view handle the logic of the web application like payment processing, user login/logout etc. before the html is generated with the templates and sent to the client side. Django makes it very easy to work with html forms via django forms. Django comes with is own template engine, django templates used for generating web pages.

To start a new django project

1. Install django with python package manager (pip)
2. Start a new django project

Install django with pip
```bash
$ pip install django
```
Create a django project
```bash
$ django-admin startproject django_project
```
The folder structure for a new django project
```treeview
django_project/
|-- django_project/
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
`-- manage.py
```
Django comes with a command line utility, *manage.py* for managing a django project. with it you can start and stop the django development server.

#### settings
This is were all the configuration of our django application is written. In settings we have our database config, template config, debug mode etc.
#### urls
This is our project root url configurations. this is were we add routes to our django app. Django comes with a default url path `'admin/'` for django administration.
```python
from django.urls import path
from django.contrib import admin
from myapp.views import index_view

urlpatterns = [
    path('admin/', admin.site.urls), # https://example.com/admin/
    path('', index_view) # website home https://example.com
]
```
#### wsgi
This is the file responsible for deployment of our django application. The wsgi file is the entry point to a django application used by web servers.

A django project is sectioned into apps. Apps in django represent modular parts of a django project. For example you can have an app for authentication, and another for blog etc.

A django project structure with app *myapp*

```treeview
django_project/
|-- django_project/
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|   `-- __init__.py
|-- myapp/
|   |-- migrations/
|   |-- admin.py
|   |-- tests.py
|   |-- apps.py
|   |-- models.py
|   |-- views.py
|   `-- __init__.py
`-- manage.py
```

#### migrations
Migrations are changes made to a database.The migration folder contains all database migrations. migrations keep track of changes made in a database. changes made to a database can easily be reverted back if the application encounter challenges due to any reason.
#### admin
Django has a default admin website for managing a website content. We register our models that we want to access in the admin in the `admin.py` file.
#### tests
Every good software is often well tested. Django support test-driven development based on python's built-in unit testing library. We write tests inside of the `tests.py`.
#### models
Models are python objects that represents a database schema. For example you can have a database table 'books' with columns 'title' and 'description'. A web app's data is managed using models. Every database table must have a primary key column, django understands this and auto creates a primary key column for model.

An example of a django model

```python
from django import models

class Book(models.Model):
    class Meta:
        db_table = 'books' # table name

    title = models.CharField(max_length=255) # column 1
    description = models.TextField() # column 2
    
    def __str__(self):
        return self.title
```
#### views
This is where our application logic lives. Some other programming language may call this file a controller. The view handles request and perform operations based on the data it receives.A django view is an interface between the database and templates. An example of a simple django view


```python
from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return HttpResponse('Hello, Django') # shows 'Hello, Django' in browser
```

### Flask Web Framework
Flask is a micro framework which has a small and easy to extend core. It is easy to learn and use and it is "beginner-friendly" because it does not have boilerplate code or dependencies like other frameworks. Flask uses jinja2 for rendering templates. Flask was initially created as an April Fool's joke, but it became very popular quickly and it is still actively maintained today. We can quickly create a flask web application in a single python file 'app.py'

> Flask does connect to databases by default you have to install packages for connecting to a database server.

An example of a flask web application.


```python
from flask import Flask

app = Flask(__name__) # create app

@app.route('/') # register route
def index():
    return 'Hello, Flask' # shows 'Hello, Flask' in browser

if __name__ == '__main__':
    app.run(debug=True) # run the development server
```
With just a few lines of code we have a flask app. This feels a lot easier than django and its boilerplate code. In flask there is no pre defined project structure, you can structure your project how you want. It is a framework that is extremely flexible.

### Conclusion
Django and Flask are both excellent choices for your next project, but if you want to build a small project thats does not require much or you just want to have the flexibility of building web apps however you like then flask might be the best option. On the other hand, Django's learning curve may be steep but once learnt the possibilities are endless because of its rich library of tools that help build large web application in a short period of time.