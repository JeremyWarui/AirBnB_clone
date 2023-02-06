## 0x00. AirBnB clone - The console

> This is a pair-programming project under the ALX-SE program.
> The project is a first phase of the AirBnB clone - the console.



### The console


This is a command line interpreter which is a single use function for managing the file storage
The console offers the functions to create, modify and delete the objects in the file storage


#### How to start it


```
git clone https://github.com/JeremyWarui/AirBnB_clone.git
cd AirBnB_clone
```


### How to use it




| Commands| Sample Usage                                | Functionality                              |
| ------- | --------------------------------------------| ------------------------------------------ |
| help    | help                                        | displays all commands available            |
| create  | create <class>                              | creates new object (ex. a new User, Place) |
| update  | User.update('123', {'name' : 'Greg_n_Mel'}) | updates attribute of an object             |
| destroy | User.destroy('123')                         | destroys specified object                  |
| show    | User.show('123')                            | retrieve an object from a file, a database |
| all     | User.all()                                  | display all objects in class               |
| count   | User.count()                                | returns count of objects in specified class|
| quit    | quit                                        | exits                                      |



### Examples:



Interactive Mode
```
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
```
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

### AUTHORS

- [Esther Warui](https://github.com/Esther-06)
- [Jeremy Mwangi](https://github.com/JeremyWarui)
