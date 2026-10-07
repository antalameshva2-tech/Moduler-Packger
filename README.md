# 🚀 Multi-Utility Toolkit

### Python Modules & Packages Project

**Developed by:** MESHVA ANTALA  
**Version:** v1.0.0  
**Language:** Python 3.x  
**Project Type:** Modules & Packages  

---

## 📌 About the Project

**Multi-Utility Toolkit** is a menu-driven Python project that combines different useful utilities into one program.

The project is created to demonstrate how **Python Modules, Packages, Custom Modules, Functions, File Handling, Exception Handling, and Built-in Libraries** can be used together in a single application.

The main program provides different options for:

- Datetime and Time Operations
- Mathematical Operations
- Random Data Generation
- UUID Generation
- File Operations
- Module Attribute Exploration

---

# ✨ Features

## 🕒 1. Datetime and Time Operations

The project provides the following datetime and time utilities:

- Display Current Date and Time
- Calculate Difference Between Two Dates
- Format Date into Custom Format
- Stopwatch
- Countdown Timer

These operations are available through the **Datetime and Time Operations** menu.

---

## 🧮 2. Mathematical Operations

Mathematical operations are implemented using the custom:

```text
math_operations.py
```

Available operations:

- Factorial
- Compound Interest
- Trigonometric Calculations
  - Sin
  - Cos
  - Tan
- Area of Circle
- Area of Rectangle
- Area of Triangle

The mathematical module also validates negative values where required.

---

## 🎲 3. Random Data Generation

The project uses Python's `random` module for different random-data operations.

Available options:

- Generate Random Number
- Generate Random List
- Create Random Password
- Generate Random OTP
- Random Sampling

---

## 🔑 4. Generate Unique Identifiers

The project uses Python's `uuid` module to generate a unique identifier.

Example:

```text
Generated UUID:
xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

---

## 📁 5. File Operations

File operations are implemented using the custom module:

```text
file_operations.py
```

Available operations:

- Create a New File
- Write to a File
- Read from a File
- Append to a File

The file module uses different file modes:

```text
x → Create a new file
w → Write data
r → Read data
a → Append data
```

The module also handles errors such as `FileExistsError`, `FileNotFoundError`, and `OSError`.

---

## 🔍 6. Explore Module Attributes

The project demonstrates the use of:

```python
importlib
```

and:

```python
dir()
```

The user can enter a module name and see the available attributes of that module.

Example:

```text
Enter module name to explore: math
```

The program imports the module and displays its available attributes.

---

# 📂 Project Structure

```text
Multi-Utility-Toolkit/
│
├── main.py
├── README.md
│
└── custom_modules/
    │
    ├── __init__.py
    ├── file_operations.py
    └── math_operations.py
```

---

# 📄 File Description

## `main.py`

`main.py` is the main program file.

It contains the main menu and connects all the different operations.

It imports the custom modules:

```python
from custom_modules import file_operations
from custom_modules import math_operations
```

The main menu contains:

```text
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
```

The program starts from the `main()` function.

---

## `README.md`

This file contains the complete documentation of the project.

It explains:

- Project information
- Features
- Project structure
- Modules
- Installation
- Usage
- Concepts
- Learning objectives
- Author information

---

## `custom_modules/__init__.py`

This file is used to initialize the `custom_modules` package.

It imports:

```python
from . import file_operations
from . import math_operations
```



---

## `custom_modules/file_operations.py`

This custom module handles file-related operations.

Functions included:

```python
create_file()
write_file()
read_file()
append_file()
```

It uses Python's built-in file handling functionality.

---

## `custom_modules/math_operations.py`

This custom module handles mathematical calculations.

Functions included:

```python
factorial()
compound_interest()
trigonometry()
circle_area()
rectangle_area()
triangle_area()
```

It uses Python's built-in `math` module.

---

# 🛠️ Technologies Used

| Technology / Module | Purpose |
|---|---|
| Python 3.x | Main programming language |
| `datetime` | Date and time operations |
| `time` | Stopwatch and countdown |
| `math` | Mathematical calculations |
| `random` | Random data generation |
| `uuid` | Unique identifier generation |
| `importlib` | Dynamic module importing |
| File Handling | File create, read, write and append |

---

# 📦 Requirements

The project requires:

```text
Python 3.x
```

All modules used in this project are Python standard-library modules.

Therefore, no external package installation is required.

---

# ⚙️ Installation

## Step 1: Install Python

Make sure Python 3.x is installed.

Check the installed version:

```bash
python --version
```

---

## Step 2: Open the Project

Open the project folder in **VS Code** or another Python IDE.

Make sure the project structure is:

```text
Multi-Utility-Toolkit/
│
├── main.py
├── README.md
│
└── custom_modules/
    ├── __init__.py
    ├── file_operations.py
    └── math_operations.py
```

---

# ▶️ How to Run

Open the terminal inside the project folder.

Run:

```bash
python main.py
```

The program will display the main menu.

---

# 🖥️ Main Menu

The program starts with:

```text
==============================
Welcome to Multi-Utility Toolkit
==============================

Choose an option:
1. Datetime and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique Identifiers (UUID)
5. File Operations (Custom Module)
6. Explore Module Attributes (dir())
7. Exit
```

The user can select an option by entering its number.

---

# 📚 Python Concepts Used

This project demonstrates several important Python concepts.

### 1. Modules

Built-in Python modules are imported and used:

```python
import datetime
import time
import math
import random
import uuid
import importlib
```

---

### 2. Custom Modules

The project contains custom modules:

```text
file_operations.py
math_operations.py
```

---

### 3. Package

The `custom_modules` folder contains:

```text
__init__.py
```

which is used for the custom Python package.

---

### 4. Functions

Different tasks are divided into separate functions.

This makes the program easier to understand and organize.

---

### 5. Exception Handling

The project uses `try` and `except` blocks to handle errors.

Example:

```python
try:
    ...
except ValueError:
    ...
```

---

### 6. File Handling

The project demonstrates file handling using:

```python
open()
```

with different modes:

```text
x → Create
r → Read
w → Write
a → Append
```

---

### 7. `importlib`

The project uses `importlib.import_module()` to dynamically import a module.

---

### 8. `dir()`

The `dir()` function is used to display the available attributes of a module.

---

# 🎯 Learning Objectives

This project helps in understanding:

- How Python modules work
- How to create custom modules
- How to create and use packages
- How to import custom modules
- How to use Python standard-library modules
- How to work with files
- How to handle exceptions
- How to create menu-driven programs
- How to use `importlib`
- How to use the `dir()` function
- How to organize a Python project

---

# 🌟 Project Highlights

```text
✔ Menu-Driven Python Program
✔ Python Modules
✔ Python Package
✔ Custom Modules
✔ Date & Time Operations
✔ Mathematical Operations
✔ Random Data Generation
✔ UUID Generation
✔ File Handling
✔ Module Exploration
✔ Exception Handling
✔ Beginner-Friendly Structure
```

---

# 🚀 Future Improvements

The project can be extended in the future by adding:

- More mathematical operations
- More file management options
- Additional date and time utilities
- More random-data features
- Better user interface
- More custom modules
- Additional utility functions

---

# 👩‍💻 Author

## MESHVA ANTALA

**Python Developer / Student**

This project was developed to practice and understand **Python Modules and Packages** along with different built-in Python libraries.

---

# 📌 Version

**Current Version:** `v1.0.0`

### Version History

| Version | Description |
|---|---|
| v1.0.0 | Initial release of Multi-Utility Toolkit |

---

# 📜 License

This project is created for **educational and learning purposes**.

---

# ❤️ Thank You

Thank you for checking out the **Multi-Utility Toolkit**!

⭐ If you find this project useful, you can give the repository a star.