# 🐍 Python Programming Projects

Two command-line Python applications built for **COMP513 Fundamentals of Computer Programming** (Grade: A-).

## 1. EventSure NZ: Ticket Fee Calculator
A booking tool that works out ticket protection fees for concerts, sports and conferences.

- Collects and validates customer details: event type, number of tickets, ticket price, age
- Calculates a base fee, a protection fee, a high-value surcharge and an age surcharge
- Prints a clear fee breakdown and lets the user process more bookings
- Includes a written algorithm (pseudocode) that was designed before the code

**Concepts used:** functions, `while` loops for validation, `if/else` selection, `try/except` error handling

## 2. Library Management System
A menu-driven app for managing a library's books.

- Login system that allows 3 attempts
- Add, remove, update, view and search books
- Saves data to a JSON file (`books.json`) so it persists between runs
- Unit tests with Python's `unittest` (`test_library.py`)

**Concepts used:** file handling, JSON, lists of dictionaries, input validation, unit testing

## 📁 Files
```
eventsure-calculator/
  algorithm.txt
  eventsure_calculator.py
library-management/
  books.json
  library_system.py
  test_library.py
screenshots/
  (0 images)
  eventsure/
    (11 images)
  library-system/
    (15 images)
  test-cases/
    (5 images)
  unit-tests/
    (5 images)
```

## ▶️ How to run
```bash
cd eventsure-calculator
python eventsure_calculator.py

cd ../library-management
python library_system.py        # demo login: admin / library123
python -m unittest test_library.py
```
Requires Python 3. No extra packages are needed.

## 🧪 Debugging and testing
I debugged both programs with breakpoints in Visual Studio and tested them with valid, invalid and boundary inputs (see `screenshots/`).
