Title: Django, The Break Down
Date: 2023-03-17 00:35
tags: django, web development
status: published

Django is a web framework written in python. It is a full featured framework used by many large companies, some of which are fortune 500 companies. Django is a framework that lets you build web apps as quickly as possible. In this article, I would break down django and explain it in a way that even a baby will know what django is all about 😉👌.

It is A secure framework with many features for making web development a fast process. You do not have to code every feature of your app from scratch, you can just leverage django's library to build web app features.

Django uses the Model-View-Template (MVT) architecture design principle. The benefit of this is that your code is already structured and as a beginner, you won't have to worry about writing your app the wrong way.

<center>
![django-mvt]({static}/images/MVT.png)
<center>

The model handles data through the database, view processes the data into information and the template renders that information on your browser. The view is bound to a URL or route such that when we navigate to a URL on our browser the view is fired, and from there the model then template.

### Model
A model is a representation of a database table. In django models are used to represent table schemas. The model comes with an Object-Relational-Mapper (ORM) that abstracts the process of querying database tables, you do not have to write raw SQL.

```python
from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=255)
  slug = models.SlugField(unique=True)
  body = models.TextField()
  publish = models.DateField()

  class Meta:
    db_table = 'posts'
```
When we create a model, django will use it to generate the SQL statement for the database table under the hood.

```sql
--
-- Create model Post
--
CREATE TABLE `posts` (`id` integer NOT NULL PRIMARY KEY, `slug` varchar(50) NOT NULL UNIQUE, `body` longtext NOT NULL, `publish` date NOT NULL);
```

### View
The view is where our application logic lives. The view process data from the database and returns an http response object. The response object is usually an html template response.

```python
from django.shortcuts import render
from . models import Post

def posts_view(request):
  posts = Post.objects.all() # Get all posts from database
  return render(request, 'posts.html', { 'posts': posts })
```

Django views accepts the `request` object as an argument, then we see the ORM in action when we call `Post.objects.all()` which is equivalent to the SQL statement `SELECT * FROM posts`. The render function binds the data via template context so that the posts will be accessible in the template.

The view is also bound to a URL so we can view the response object in our browser.

```python
from django.urls import path
from . views import post_views

urlpatterns = [
  path('posts/', posts_views),
]
```

### Template
Django has a template language for rendering data.  This is how we display the `posts` in html using django templates.

```html
<html>
  <head>
    <title>Django Template</title>
  </head>
  <body>
    {% for post in posts %}
    <h2>{{ post.title }}</h2>
    <small>{{ post.publish }}</small>
    <p>{{ post.body }}</p>
    {% endfor %}
  </body>
</html>
```

This syntax, `{% expression %}` the curl brackets and the percentage symbol, allows us to use python statements like if, if-else, for inside of the templates. The double curl brackets `{{ variable }}` syntax is used for accessing python objects, variables, etc. With django templates, you can control what can be displayed based on data passed in the template context.

### Creating A Blank Django Project

To create a blank django project, you must install django site-package using pip. once you have installed django, you use the `django-admin` command to create an empty django project.

```bash
pip install django # installing django

django-admin startproject djangoproject # start a blank django project
```

Your django project will look something like this.

```treeview
djangoproject/
|-- djangoproject/
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
`-- manage.py
```

Each django project is made up of apps. Apps in django represent a part of your web application for example, if I wanted to add a blog to my project I can create a blog app, if I want to add authentication, then I can create an app that handles that. Let's create a blog app in the project.

```bash
python manage.py startapp blog
```

This would create a folder blog with the structure below

```treeview
djangoproject/
|-- djangoproject/
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|   `-- __init__.py
|-- blog/
|   |-- migrations/
|   |-- admin.py
|   |-- tests.py
|   |-- apps.py
|   |-- models.py
|   |-- views.py
|   `-- __init__.py
`-- manage.py
```

You can see we have a file for models and views. We create our models inside of models.py and write our view functions inside of views.py. The django project folder has files for URLs and settings. The settings file is where we handle all our app configurations. Django comes with a sqlite database by default but you can modify the DATABASES config in the settings file to change it.

In this article, I broke down how django works. Django has its way of doing things which can be scary to people who wants to learn the framework, but once they understand the how and why they become like superheroes of web development. I hope this post was able to clarify some misconceptions you have about django.