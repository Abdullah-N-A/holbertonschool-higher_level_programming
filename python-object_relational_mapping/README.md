Python - MySQL & SQLAlchemy ORM
Description
This project links two powerful worlds: Databases and Python.

In the first part, you will use the MySQLdb module to connect to a MySQL database and execute SQL queries directly from Python.

In the second part, you will use SQLAlchemy, an Object Relational Mapper (ORM), to interact with the database using Python objects instead of writing SQL queries.

The goal is to understand how to manipulate relational data both with and without an ORM, and to see the advantages of abstraction, portability, and maintainability.

Learning Objectives
By the end of this project, you should be able to explain (without Google):

How to connect to a MySQL database from a Python script
How to SELECT rows in a MySQL table from a Python script
How to INSERT rows in a MySQL table from a Python script
What ORM means
How to map a Python class to a MySQL table
Requirements
OS: Ubuntu 20.04 LTS
Python: 3.8.5
MySQL: 8.0.25
MySQLdb: 2.0.x
SQLAlchemy: 1.4.x
Allowed editors: vi, vim, emacs
All files must end with a new line
The first line of all files must be exactly: #!/usr/bin/python3
All files must be executable
Code must follow pycodestyle (version 2.7.*)
All modules, classes, and functions must have documentation strings
You are not allowed to use execute with SQLAlchemy
A README.md file is mandatory at the root of the project folder
Setup Environment
Install MySQL (if not using sandbox)
sudo apt update
sudo apt install mysql-server
mysql --version
sudo mysql
