# alu-AirBnB_clone

This is a simple clone of the AirBnB project for ALU. The goal is to build a basic version of AirBnB using Python, with a command-line interpreter to manage different objects like users, places, and more.

## Project Description

This project is part of my ALU coursework. It helped me learn about object-oriented programming, file storage, and building a simple command interpreter in Python.

## Command Interpreter

The command interpreter lets you create, show, update, and delete objects. It works in interactive mode (with a prompt) or non-interactive mode (by passing commands as arguments).

### How to Start

1. Make sure you have Python 3 installed.
2. Open a terminal in the project folder.
3. Start the interpreter with:
   ```
   python console.py
   ```

### How to Use

When you see the prompt `(hbnb)`, you can type commands like:
- `create User`
- `show User <id>`
- `destroy User <id>`
- `all User`
- `update User <id> name "John"`
- `quit` (to exit)

### Examples

```
$ python console.py
(hbnb) create User
(hbnb) show User 1234-5678
(hbnb) all User
(hbnb) update User 1234-5678 first_name "Betty"
(hbnb) quit
```

## Contributors

See the AUTHORS file for a list of contributors.
