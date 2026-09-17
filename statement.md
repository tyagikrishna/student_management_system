# Problem Statement

## Problem

Many small educational institutes, coaching centres and individual departments
still maintain student details and daily attendance manually, either in
registers or in unstructured spreadsheets. This creates a few practical
problems:

- The same student sometimes gets entered twice under different roll numbers.
- Attendance is recorded on paper, so calculating a percentage for one student
  means counting rows by hand.
- Finding all the students who are short of the required attendance before an
  exam is slow and error prone.
- There is no single place where a student's details and their attendance
  history are connected, so the two records drift apart over time.

There is a need for a simple, offline system that keeps student records and
attendance together, prevents obviously wrong entries at the point of input,
and produces the summaries a teacher actually needs.

## Scope of the Project

**Included**

- Creating, viewing, searching, updating and deleting student records
- Marking and viewing attendance for a student on a specific date
- Validating every input before it is saved
- Preventing duplicate roll numbers and duplicate attendance entries
- Storing all data permanently in CSV files so it survives program restarts
- Generating reports: branch wise count, attendance summary, low attendance
  list and best attendance
- Unit tests for validation, models and the storage layer

**Not included**

- Multiple users, login or role based access
- A graphical or web interface; the system is command line only
- Marks, grades, fee management or timetable handling
- Network or multi computer access; the system runs on one machine

## Target Users

1. **Class teachers and faculty** who need to mark daily attendance and check
   which students are falling short.
2. **Department or office staff** who maintain the list of enrolled students
   and keep it updated.
3. **Small coaching centres** that have too few students to justify buying
   commercial ERP software.
4. **Students learning Python**, as a readable example of a modular file based
   application.

## High Level Features

| Module | Feature | Description |
|---|---|---|
| Student Records | Add Student | Saves a new student after validating name, roll number and branch, and rejects duplicate roll numbers |
| Student Records | Display Students | Lists all stored students with a total count |
| Student Records | Search Student | Finds a single student by roll number |
| Student Records | Update Student | Changes the name and branch of an existing record |
| Student Records | Delete Student | Removes a record after asking for confirmation |
| Attendance | Mark Attendance | Records Present or Absent for a valid student on a valid date |
| Attendance | View Attendance | Shows a student's full history with total classes and percentage |
| Attendance | Delete Attendance | Removes a wrongly entered attendance record |
| Reports | Branch Wise Count | Groups students by branch and counts them |
| Reports | Attendance Summary | Shows the percentage of every student in one view |
| Reports | Low Attendance | Lists students below the 75% limit set in the config |
| Reports | Best Attendance | Identifies the student with the highest percentage |
