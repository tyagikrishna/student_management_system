# Student Management System

A menu driven Student Management System written in Python. It stores student
records and daily attendance in CSV files and generates simple reports from
that data. The whole project runs in the terminal and needs no external
libraries.

## Overview

Small colleges and coaching centres often keep student details and attendance
in notebooks or loose Excel sheets. Records get duplicated, attendance is hard
to total up, and finding the students who are short of attendance means
counting by hand.

This project solves that with three connected modules: one to manage student
records, one to mark and view attendance, and one to turn that stored data into
reports such as branch wise counts and a low attendance list.

## Features

**Student Records**
- Add a student with validated name, roll number and branch
- Display all students with a total count
- Search a student by roll number
- Update the name and branch of an existing student
- Delete a student, with a confirmation prompt

**Attendance**
- Mark attendance for a student on a given date (Present / Absent)
- Blocks marking the same student twice on the same date
- Blocks marking attendance for a roll number that does not exist
- View the full attendance history and percentage of one student
- Delete a wrongly entered attendance record

**Reports**
- Branch wise student count
- Attendance percentage summary of all students
- Low attendance report (students below 75%)
- Student with the best attendance

## Technologies Used

- Python 3
- `csv` module for file storage
- `os` module for path handling
- `unittest` module for testing
- Git and GitHub for version control

No third party packages are required.

## Folder Structure

```
student_management/
├── main.py                        entry point and main menu
├── config.py                      file paths and settings
├── models/
│   ├── student.py                 Student class
│   └── attendance.py              Attendance class
├── storage/
│   └── csv_store.py               all csv reading and writing
├── services/
│   ├── student_service.py         module 1 - student records
│   ├── attendance_service.py      module 2 - attendance
│   └── report_service.py          module 3 - reports
├── utils/
│   └── validators.py              input validation
├── tests/
│   ├── test_validators.py
│   ├── test_models.py
│   └── test_csv_store.py
├── data/
│   ├── students.csv               sample data
│   └── attendance.csv             sample data
└── docs/
    └── REPORT.md                  project report with diagrams
```

## How to Install and Run

1. Make sure Python 3 is installed:

   ```
   python3 --version
   ```

2. Clone the repository:

   ```
   git clone <your-repository-url>
   cd student_management
   ```

3. Run the program from the project root folder:

   ```
   python3 main.py
   ```

   Run it from the project root, not from inside a subfolder, because the
   data file paths in `config.py` are relative to the root.

4. Use the number keys to move through the menus. Choose `4` on the main menu
   to exit.

The `data` folder already contains a few sample records so the reports show
something on the first run. Delete the two CSV files if you want to start
with an empty system.

## How to Test

Run all unit tests from the project root:

```
python3 -m unittest discover -s tests -v
```

This runs 17 tests covering input validation, the model classes and the CSV
storage layer. All of them should pass.

Manual test ideas:
- Try adding a student with a name containing digits, it should be rejected
- Try adding a roll number that already exists, it should be rejected
- Try marking attendance for a roll number that was never added
- Try marking attendance twice for the same student on the same date
- Delete `data/students.csv` and open the reports, it should say no students
  found instead of crashing

## Screenshots

Add screenshots of the main menu, the student list, the attendance summary and
the low attendance report here before submitting.

## Future Enhancements

- Move storage from CSV to SQLite so searching is faster on large data
- Add marks and grade calculation as a fourth module
- Add a login system separating admin and teacher roles
- Export reports as PDF or Excel
- Build a simple GUI using Tkinter
