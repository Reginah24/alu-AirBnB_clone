# alu-AirBnB_clone

## Project Description
This project is a simplified clone of the AirBnB web application, developed as part of the ALU software engineering curriculum. It aims to build a basic command-line interface (CLI) for managing objects that represent AirBnB entities such as users, places, amenities, and more. The project demonstrates object-oriented programming, data serialization, and persistence using JSON.

## Command Interpreter
The command interpreter is a custom shell that allows you to create, show, update, and destroy objects interactively or in non-interactive mode. It is built using Python's `cmd` module.

### How to Start
To start the command interpreter, run:

```bash
python console.py
```

### How to Use
Once started, you will see the prompt `(hbnb)`. You can enter commands such as:

- `create <ClassName>`: Creates a new instance of a class (e.g., BaseModel, User) and prints its id.
- `show <ClassName> <id>`: Shows the string representation of an instance.
- `destroy <ClassName> <id>`: Deletes an instance.
- `all [<ClassName>]`: Shows all instances, or all instances of a class.
- `update <ClassName> <id> <attribute> <value>`: Updates an instance's attribute.
- `quit` or `EOF`: Exits the interpreter.

### Examples
```
(hbnb) create BaseModel
b6a6e15c-c67d-4312-9a75-9d084935e579
(hbnb) show BaseModel b6a6e15c-c67d-4312-9a75-9d084935e579
[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {...}
(hbnb) update BaseModel b6a6e15c-c67d-4312-9a75-9d084935e579 name "My First Model"
(hbnb) all BaseModel
["[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {...}"]
(hbnb) quit
```

## Authors
See the `AUTHORS` file for a list of contributors.

---
This project is for educational purposes only.