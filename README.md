# Python Projects

This repository is a collection of Python practice projects, ranging from short command-line exercises to a personal finance tracker. Each script can be explored and run independently.

## Repository contents

```text
.
├── README.md
├── Smaller projects/
│   ├── Calendar_app.py
│   ├── Contact_app.py
│   ├── Random_password_generator.py
│   ├── Student_records_manager.py
│   ├── TDL.py
│   ├── Trivia_game.py
│   └── todo_list.json
└── personal_finance_tracker_project/
    ├── data_entry.py
    ├── finance_data.csv
    └── main.py
```

## Smaller projects

These programs are interactive command-line exercises. Run a script from the `Smaller projects` directory so that its relative data-file paths work as intended.

### Calendar app — `Calendar_app.py`

The calendar exercise. (The current file is empty, so it does not yet implement calendar behavior.)

### Contact book — `Contact_app.py`

A menu-driven contact book that can add, view, edit, delete, and list contacts. Each contact has a name, phone number, email address, and physical address. Contacts are held in memory while the program runs; they are not saved between runs.

### Random password generator — `Random_password_generator.py`

Prompts for a password length and whether to include uppercase letters, punctuation, and digits. Lowercase letters are always available, and one character from each selected optional group is included. The script requires a length of at least five characters and prints the generated password.

### Student records manager — `Student_records_manager.py`

An in-memory example of student records, courses, and grades. Its functions add students and grades, check course enrollment, calculate average grades, list students by course, and filter students above a grade threshold. The file also runs a small example with Alice and Bob when executed. Records are not persisted.

### To-do list — `TDL.py`

A menu-driven task list. You can view tasks, add a description, mark a task complete, delete a task, and display the menu again. Tasks are stored in `todo_list.json` in the current working directory.

### Trivia game — `Trivia_game.py`

Selects five random questions from a small built-in trivia set, checks typed answers without case sensitivity, and reports the score. The game starts as soon as the script is run.

## Personal finance tracker

The `personal_finance_tracker_project` folder contains a command-line tracker for recording income and expenses. The menu can add a transaction, show transactions and totals for a date range, and optionally plot income and expenses over time.

- `main.py` contains the menu, CSV storage helper, date-range filtering, summaries, and charting.
- `data_entry.py` contains prompts and validation for dates, positive amounts, transaction categories, and descriptions.
- `finance_data.csv` is the tracker’s transaction data file. The program creates it with the expected columns if it is missing.

Transactions use the date format `dd-mm-yyyy`, and categories are `Income` or `Expense`. The date-range summary reports total income, total expenses, and net savings. The optional chart uses Matplotlib.

### Requirements and running

Python 3 is required. The finance tracker also imports `pandas` and `matplotlib`:

```bash
python -m pip install pandas matplotlib
```

Run the tracker from its folder so it reads and writes `finance_data.csv` there:

```bash
cd personal_finance_tracker_project
python main.py
```

Run a smaller project from its folder in the same way, for example:

```bash
cd "Smaller projects"
python TDL.py
```

Replace `TDL.py` with another script name to run a different exercise. `Calendar_app.py` currently has no implementation.

## Notes

- These are standalone learning projects rather than a single installable application; there is no shared package or automated test suite in the repository.
- The contact book and student records are in-memory demonstrations. The to-do list and finance tracker are the projects that write data files.
- `todo_list.json` currently provides the to-do list's saved task data. Avoid committing personal or sensitive transaction/contact details if you add them to project data files.
