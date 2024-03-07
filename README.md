# AirBnB_clone
<<<<<<< HEAD
# husamrio.github.io
# AirBnB_clone_v4
# AirBnB_clone_v4
# alx-backend-javascript
=======
## Description

The first stage of creating an Airbnb clone is the console. This repository contains a command interpreter, as well as several classes, including the BaseModel class and its subclasses: Amenity, City, State, Place, and Review. The command interpreter functions like a shell, allowing users to input commands and manipulate object instances
methods and attributes.

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
- Style guidelines: [PEP 8 (version 1.7)](https://www.python.org/dev/peps/pep-0008/) \|| [Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/l\atest/example_google.html) || [WC3 Validator](https://github.com/holbertonschool/W3C-Validator)

  ## Authors
Hussein Abdullahi 
>>>>>>> b68f7f87b0abc92d0ae3fcb0563ea6860878a06a
