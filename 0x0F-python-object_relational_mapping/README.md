# Python - Object-relational mapping
Object-Relational Mapper (ORM) is a code library that automates the transfer of data stored in relational database tables into
object that are more commonly used in application code.

ORMs provide a bridge between relational database tables, relationships and fields and python objects (in this case).

## Background Context
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:

```python
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```

With ORM:
```python
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```

Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.

## Resources
Read or watch
* [Object-relational mappers](https://alx-intranet.hbtn.io/rltoken/a8DUOWhXpNX3TEwgyT-U8A)
* [mysqlclient/MySQLdb documentation (please don’t pay attention to _mysql)](https://alx-intranet.hbtn.io/rltoken/JtFaKjnqxudr6Hi05Us1Lw)
* [MySQLdb tutorial](https://alx-intranet.hbtn.io/rltoken/TdUSYFNGbXJG1WjCEoq5FA)
* [SQLAlchemy tutorial](https://alx-intranet.hbtn.io/rltoken/YyL5hsscviNH04XGW-XpfA)
* [SQLAlchemy](https://alx-intranet.hbtn.io/rltoken/j9azWF2Db_2rNolTxOF3SA)
* [mysqlclient/MySQLdb](https://alx-intranet.hbtn.io/rltoken/0zLhY9KqKjn-zmdb7X598Q)
* [Introduction to SQLAlchemy](https://alx-intranet.hbtn.io/rltoken/pw50Bl1Bj84wksxm018dwA)
* [Flask SQLAlchemy](https://alx-intranet.hbtn.io/rltoken/B-xIdMtGvpus8vHxAIRrPg)
* [10 common stumbling blocks for SQLAlchemy newbies](https://alx-intranet.hbtn.io/rltoken/deIzPMrfK8Ixqm-AboFHWg)
* [Python SQLAlchemy Cheatsheet](https://alx-intranet.hbtn.io/rltoken/dZfUNK3lJicGMK5PU0bE7Q)
* [SQLAlchemy ORM Tutorial for Python Developers (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)](https://alx-intranet.hbtn.io/rltoken/hNxBKC8lHge5XjsRO8ksHQ)
* [SQLAlchemy Tutorial](https://alx-intranet.hbtn.io/rltoken/5G_R2NmQRFqiZb84qxYERQ)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General

1. Why Python programming is awesome
2. How to connect to a MySQL database from a Python script
3. How to SELECT rows in a MySQL table from a Python script
4. How to INSERT rows in a MySQL table from a Python script
5. What ORM means
6. How to map a Python Class to a MySQL table

## Copyright - Plagiarism

1. You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
2. You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
3. You are not allowed to publish any content of this project.
4. Any form of plagiarism is strictly forbidden and will result in removal from the program.

##Requirements

1. Allowed editors: vi, vim, emacs
2. All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
3. Your files will be executed with MySQLdb version 2.0.x
4. Your files will be executed with SQLAlchemy version 1.4.x
5. All your files should end with a new line
6. The first line of all your files should be exactly 
    ```python 
    #!/usr/bin/python3
    ```
7. A README.md file, at the root of the folder of the project, is mandatory
8. Your code should use the pycodestyle (version 2.8.*)
9. All your files must be executable
10. The length of your files will be tested using wc
11. All your modules should have a documentation
    ```python 
    python3 -c 'print(__import__("my_module").__doc__)'
    ```
12. All your classes should have a documentation 
    ```python
    python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    ```
13. All your functions (inside and outside a class) should have a documentation 
    ```python
    python3 -c 'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    ```
14. A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
15. You are not allowed to use execute with sqlalchemy


## More Info
### Install MySQLdb module version 2.0.x

For installing MySQLdb, you need to have MySQL installed: How to install MySQL 8.0 in Ubuntu 20.04

```python
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```

### Install SQLAlchemy module version 1.4.x

```python
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```

Also, you can have this warning message:

```
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)  
```

You can ignore it.