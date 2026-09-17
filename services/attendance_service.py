import config
from models.attendance import Attendance
from storage import csv_store
from services import student_service
from utils import validators

def get_all_attendance():
    rows = csv_store.read_all(config.ATTENDANCE_FILE)
    entries = []
    for row in rows:
        entries.append(Attendance.from_dict(row))
    return entries

def get_attendance_of(roll_number):
    entries = []
    for entry in get_all_attendance():
        if entry.roll_number == roll_number:
            entries.append(entry)
    return entries

def already_marked(roll_number, date):
    for entry in get_attendance_of(roll_number):
        if entry.date == date:
            return True
    return False

def calculate_percentage(roll_number):
    entries = get_attendance_of(roll_number)
    if len(entries) == 0:
        return 0.0
    present = 0
    for entry in entries:
        if entry.status == "P":
            present = present + 1
    percentage = (present / len(entries)) * 100
    return round(percentage, 2)

def mark_attendance():
    roll_number = validators.ask_roll_number("Enter roll number: ")
    student = student_service.find_student(roll_number)
    if student is None:
        print("Student not found. Please add the student first.")
        return

    print("Marking attendance for:", student.name)
    date = validators.ask_date("Enter date (DD-MM-YYYY): ")

    if already_marked(roll_number, date):
        print("Attendance for this date is already marked.")
        return

    status = validators.ask_status("Enter status (P = present, A = absent): ")
    entry = Attendance(roll_number, date, status)
    csv_store.append_row(config.ATTENDANCE_FILE, config.ATTENDANCE_FIELDS, entry.to_dict())
    print("Attendance marked successfully.")

def view_attendance():
    roll_number = validators.ask_roll_number("Enter roll number: ")
    student = student_service.find_student(roll_number)
    if student is None:
        print("Student not found.")
        return

    entries = get_attendance_of(roll_number)
    print("\n===== ATTENDANCE OF", student.name.upper(), "=====")
    if len(entries) == 0:
        print("No attendance records found for this student.")
        return

    for entry in entries:
        entry.display()
    print("---------------------------")
    print("Total classes:", len(entries))
    print("Attendance percentage:", calculate_percentage(roll_number), "%")

def delete_attendance():
    roll_number = validators.ask_roll_number("Enter roll number: ")
    date = validators.ask_date("Enter date to delete (DD-MM-YYYY): ")
    entries = get_all_attendance()
    remaining = []
    found = False

    for entry in entries:
        if entry.roll_number == roll_number and entry.date == date:
            found = True
            continue
        remaining.append(entry)

    if not found:
        print("No attendance record found for this student on that date.")
        return

    rows = []
    for entry in remaining:
        rows.append(entry.to_dict())
    csv_store.write_all(config.ATTENDANCE_FILE, config.ATTENDANCE_FIELDS, rows)
    print("Attendance record deleted successfully.")

def attendance_menu():
    while True:
        print("\n===== ATTENDANCE MENU =====")
        print("1. Mark Attendance")
        print("2. View Attendance of a Student")
        print("3. Delete an Attendance Record")
        print("4. Back to Main Menu")

        choice = input("Enter your choice: ")
        if choice == "1":
            mark_attendance()
        elif choice == "2":
            view_attendance()
        elif choice == "3":
            delete_attendance()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
