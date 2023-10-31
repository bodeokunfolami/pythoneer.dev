Title: Installing MySQL Community Server on Windows 11
Date: 2023-03-30 12:00
category: mysql
tags: mysql

MySQL is a relational database management system (RDBMS). Relational databases are the most widely used databases today. They store data in tables which consist of rows and columns. MySQL is a popular relational database amongst others, and in this article i will show you how to install mysql on windows 11. There are two ways of installing mysql, with windows msi installer or downloading the zip archive files and setting it up on your system. I would recommend the second method, So you will know how to configure mysql on your local system.

### Downloading MySQL

Download mysql zip files from <a href="https://dev.mysql.com/downloads/mysql" target="_blank">here</a>

<center>
![img-msql-download-1]({static}/images/mysql-download-1.png)
</center>

Once downloaded extract the archive file to this location

```text
C:\mysql
```

The mysql files extracted does not have a data folder. The data folder is where mysql stores database information. To create a data folder run the command below.

```plaintext
"C:\mysql\bin\mysqld" --initialize
```

The command above will create the data directory in the default location `C:\mysql\data` and initialize the system database.

### Starting The Server

You can start the mysql server in the terminal console using the command

```plaintext
"C:\mysql\bin\mysqld" --console
```

This will start the server and you can open a new terminal and connect to mysql client. MySQL comes with a default user root that does not have a password. You can connect to mysql using the default user account.

### Add MySQL to System Path

In order to connect to mysql effectively, you must add mysql to system path. If you do not have mysql in your system path, You will always have to connect to mysql from mysql bin folder

```plaintext
"C:\mysql\bin\mysql" -u root
```

To add mysql to system path:

- Copy the location of the mysql bin folder `c:\mysql\bin` to clipboard
- Search for "environment variables" in windows search bar and open it
- Click on the environment variables button
- Select path under the system panel.
- Click on edit.
- Click new and paste the mysql bin folder location
- Select apply and save

For the best experience, it is better to install mysql server as a service, that way the mysql server will always run in the background. To install the server as a service run the command.

```text
C:> "C:\mysql\bin\mysqld" --install
```

This adds mysql service to windows services.
