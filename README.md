# GoIT Python Core — Homework 04

## Overview

This repository contains the solutions for Homework 04 of the GoIT Python Core course. The project includes four tasks focused on file processing, working with directories, command-line arguments, and building a console-based contact assistant.

## Project Structure

```text
goit-pycore-hw-04/
├── main.py            # Task 1: Calculate total and average salary
├── salary_file.txt    # Developer salary data
├── task2.py           # Task 2: Parse cat information
├── cats_file.txt      # Cat data
├── hw03.py            # Task 3: Display a colored directory tree
├── assistant.py       # Task 4: Console contact assistant
├── requirements.txt   # Project dependencies
├── .gitignore         # Git ignore rules
└── README.md          # Project documentation
```

## Requirements

- Python 3
- `pip` for installing dependencies
- A terminal or command-line interface

The project uses the following external dependency:

- [Colorama](https://pypi.org/project/colorama/) — provides colored terminal output.

## Installation

### 1. Clone the repository

```bash
git clone git@github.com:mustafos/goit-pycore-hw-04.git
cd goit-pycore-hw-04
```

Replace `https://github.com/mustafos/goit-pycore-hw-04.git` with the URL of your GitHub repository.

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

**macOS / Linux**

```bash
source .venv/bin/activate
```

**Windows (PowerShell)**

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Task 1 — Calculate Total and Average Salary

**File:** `main.py`

### Description

The `total_salary(path)` function reads a text file containing developer names and their salaries. It calculates the total salary and the average salary.

Each non-empty line in the input file must contain a developer's name and salary separated by a comma.

### Input format

Example of `salary_file.txt`:

```text
Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
```

### Run

```bash
python main.py
```

### Expected output

```text
Total salary: 6000
Average salary: 2000.0
```

### Implementation details

- Reads the file using UTF-8 encoding.
- Processes each non-empty line.
- Calculates the total and average salaries.
- Handles missing files and file-reading or data-format errors.

## Task 2 — Parse Cat Information

**File:** `task2.py`

### Description

The `get_cats_info(path)` function reads a file containing cat records and returns a list of dictionaries.

Each record contains three comma-separated values:

- `id` — the cat's unique identifier.
- `name` — the cat's name.
- `age` — the cat's age.

### Input format

Example of `cats_file.txt`:

```text
60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
```

### Run

```bash
python task2.py
```

### Expected output

The function returns a list of dictionaries in this format:

```python
[
    {
        "id": "60b90c1c13067a15887e1ae1",
        "name": "Tayson",
        "age": "3"
    },
    {
        "id": "60b90c2413067a15887e1ae2",
        "name": "Vika",
        "age": "1"
    },
    {
        "id": "60b90c2e13067a15887e1ae3",
        "name": "Barsik",
        "age": "2"
    }
]
```

The complete output depends on the records in `cats_file.txt`.

### Implementation details

- Reads the file using UTF-8 encoding.
- Splits each non-empty line into ID, name, and age.
- Returns the records as a list of dictionaries.
- Handles missing files and file-reading or data-format errors.

## Task 3 — Colored Directory Tree

**File:** `hw03.py`

### Description

The program displays the contents of a specified directory as a hierarchical tree. It uses command-line arguments to receive the directory path.

Directories are displayed in blue, and files are displayed in green. The output uses tree connectors to show the directory structure.

### Run

Display the current project directory:

```bash
python hw03.py .
```

Display a specific directory:

```bash
python hw03.py /path/to/directory
```

For example, on macOS or Linux:

```bash
python hw03.py ~/Documents
```

### Implementation details

- Uses `sys.argv` to read the directory path.
- Uses `pathlib.Path` to work with filesystem paths.
- Uses `colorama` to format terminal output with colors.
- Traverses directories recursively.
- Sorts entries for consistent output.
- Displays directories and files with different colors.
- Reports invalid paths and filesystem access errors.

**Note:** The program recursively displays accessible contents, including hidden directories such as `.git` and `.venv` when they are present in the selected directory.

## Task 4 — Console Contact Assistant

**File:** `assistant.py`

### Description

The console assistant manages contacts stored in a Python dictionary. It supports adding contacts, updating phone numbers, looking up a contact, displaying all contacts, and exiting the program.

Contacts are stored in memory while the program is running. They are not saved to a file or database.

### Run

```bash
python assistant.py
```

### Available commands

| Command    | Syntax                    | Description                                                 |
| ---------- | ------------------------- | ----------------------------------------------------------- |
| `hello`  | `hello`                 | Displays a greeting.                                        |
| `add`    | `add username phone`    | Adds a new contact or sets the phone number for a username. |
| `change` | `change username phone` | Updates an existing contact's phone number.                 |
| `phone`  | `phone username`        | Displays the phone number for a contact.                    |
| `all`    | `all`                   | Displays all saved contacts.                                |
| `exit`   | `exit`                  | Exits the assistant.                                        |
| `close`  | `close`                 | Exits the assistant.                                        |

### Example session

```text
Welcome to the assistant bot!
Enter a command: hello
How can I help you?
Enter a command: add John 1234567890
Contact added.
Enter a command: add Anna 9876543210
Contact added.
Enter a command: phone John
1234567890
Enter a command: change John 1112223333
Contact updated.
Enter a command: all
John: 1112223333
Anna: 9876543210
Enter a command: exit
Good bye!
```

### Implementation details

- Uses a dictionary to store contact names and phone numbers.
- Uses `parse_input()` to parse commands and arguments.
- Separates command parsing from contact-management functions.
- Validates the number of command arguments.
- Reports when a requested contact does not exist.
- Keeps interactive input and output inside `main()`.
- Supports both `exit` and `close` commands.

## Dependencies

The project's dependencies are listed in `requirements.txt`.

Install them with:

```bash
python -m pip install -r requirements.txt
```

Current dependency:

```text
colorama==0.4.6
```

## Notes

- Run commands from the project root directory unless a different working directory is explicitly specified.
- `salary_file.txt` and `cats_file.txt` are sample input files used by the corresponding scripts.
- The contact assistant stores contacts only for the duration of the current session.
- The `.venv/` directory is excluded from version control and should not be committed to the repository.

## Author

Mustafa Bekirov
