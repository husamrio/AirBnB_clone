# AirBnB_clone
## Description

This is the first phase of the Airbnb Clone: the console. This repository holds a command interpreter and classes (i.e. BaseModel class and several other classes that inherit from it: Amenity, City, State, Place, Review), and a command interpreter. The command interpreter, like a shell, can be activated, take in user input, and perform certain tasks to manipulate the object instances.
## Command Interpreter Usage
********************************************************************************
| Commands |  Sample Usage  | Functionality  |
|----------|----------------|----------------|
|` help ` |` help` | displays all commands available |
| `create` | `create <class>` | creates new object (ex. a new User, Place) |
| `update` | `User.update('123', {'name' : 'Greg_n_Mel'})` | updates attribute of an object |
| `destroy` |  `User.destroy('123')` | destroys specified object |
| `show` | `User.show('123')` | retrieve an object from a file, a database |
| `all` | `User.all()` | display all objects in class |
| `count` | `User.count()` | returns count of objects in specified class |
| `quit` | `quit` | exits |

#### Installation
```bash
git clone git@github.com:husamrio/AirBnB_clone.git
cd AirBnB_clone
## Usage 
## Interactive Mode
```bash

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
 Non-Interactive Mode
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Environment
- Language: Python3
- OS: Ubuntu 20.04 LTS

  ## Authors
Hussein Abdullahi 
