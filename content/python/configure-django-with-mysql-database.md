Title: Configure Django And MySQL Database
Date: 2023-01-17 8:00
tags: django, python, mysql
status: published

In this post, I will show you how to set up Django with MySQL database. This tutorial assumes you already have MySQL installed on your computer. Django comes with a default SQLite database that does not require any setup. SQLite databases are not good for large scale applications therefore, it is recommended you use a secure database like MySQL for your projects. Mysql is not free software but it has a free community version you can download from <a target="_blank" href="https://dev.mysql.com/downloads/mysql/">here</a>.

When you first install MySQL, it comes with a default root user. In some cases, you will be required to set a password for the root user; in others, you will not. It is not recommended to use MySQL's root user, so we are going to create a new user and grant the user the privileges from the root user. 

### Setup MySQL
Enter the MySQL shell with the following command

```bash
mysql -u root
```
If you configured a password during your installation you use the command below. This will show you a prompt where you can now enter your password.

```bash
mysql -u root -p
```


If you are using ubuntu or Debian Linux and the above commands did not work for you use:

```bash
sudo mysql
```

Create the database
```sql
CREATE DATABASE mydb;
```

Create a new user with a password.

```sql
CREATE USER 'dapo'@'localhost' IDENTIFIED BY 'password';
```

Grant privileges to your new user

```sql
GRANT ALL PRIVILEGES ON mydb.* TO 'dapo'@'localhost' WITH GRANT OPTION;
```
This command will allow the user have full access to the database `mydb`.

Then finally use the flush command to refresh.

```sql
FLUSH PRIVILEGES;
```



### Setup Django 

Before we can configure our Django app with MySQL first we need the following packages:

- mysqlclient
- django-environ

#### mysqlclient 
This is the package that allows MySQL to communicate with our Django server if you do not have it then your Django app will not run.

Install command:
```bash
pip install mysqlclient
```

#### django-environ
This is a package that allows us to manage environment variables easily, using a .env file. This package makes configuring MySQL with Django easy. 

Install command:
```bash
pip install django-environ
```

After you have installed the packages create a file called .env beside the settings.py file in your Django project.

```treeview
django_project/
|-- django_project/
|   |-- .env
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|   `-- __init__.py
```
Inside the .env file create an environment variable `DATABASE_URL` with the connection string as the value

```plaintext
DATABASE_URL=mysql://dapo:password@localhost/mydb
```
Import the environ module and load the environment variable inside of the settings.py.

```python
import environ

# Load the environment variable inside python
env = environ.Env()
environ.Env.read_env()
```

Finally, use the env variable to load the database configuration inside of the `DATABASES` python dictionary located inside `settings.py` file.

```python
# The database configuration will be generated from
# the connection string in the .env file
DATABASES = {
  'default': env.db()
}
```
The `env.db()` function will generate the configuration dictionary for MySQL with the `DATABASE_URL` environment variable.

```python
{
  'NAME': 'mydb', 
  'USER': 'dapo', 
  'PASSWORD': 'password', 
  'HOST': 'localhost', 
  'PORT': 3306, 
  'ENGINE': 'django.db.backends.mysql'
}
```

> You can connect to MySQL database hosted on another server. Change the HOST from localhost to the server's HOST name and set the PORT the server is using. The default PORT for MySQL is 3306. This is what most servers will use.

If you have reached the end of this article, You should be able to use django-environ to setup Django and MySQL. I know you can, because its not difficult. 