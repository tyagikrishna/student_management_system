import config
from models.student import Student
from storage import csv_store
from utils import validators

def get_all_students():
    rows = csv_store.read_all(config.STUDENT_FILE)
    students = []
    for row in rows:
        students.append(Student.from_dict(row))
    return students

def roll_number_exists(roll_number):
    for student in get_all_students():
        if student.roll_number == roll_number:
            return True
    return False

def find_student(roll_number):
    for student in get_all_students():
        if student.roll_number == roll_number:
            return student
    return None

def save_all_students(students):
    rows = []
    for student in students:
        rows.append(student.to_dict())
    csv_store.write_all(config.STUDENT_FILE, config.STUDENT_FIELDS, rows)

def add_student():
    name = validators.ask_name("Enter student name: ")
    roll_number = validators.ask_roll_number("Enter roll number: ")

    if roll_number_exists(roll_number):
        print("A student with this roll number already exists.")
        return

    branch = validators.ask_branch("Enter branch: ")
    student = Student(name, roll_number, branch)
    csv_store.append_row(config.STUDENT_FILE, config.STUDENT_FIELDS, student.to_dict())
    print("Student added successfully.")

def display_students():
    students = get_all_students()
    print("\n===== STUDENT RECORDS =====")
    if len(students) == 0:
        print("No students found.")
        return
    for student in students:
        student.display()
    print("Total students:", len(students))

def search_student():
    roll_number = validators.ask_roll_number("Enter roll number to search: ")
    student = find_student(roll_number)
    if student is None:
        print("Student not found.")
        return
    print("\n===== STUDENT FOUND =====")
    student.display()

def update_student():
    roll_number = validators.ask_roll_number("Enter roll number to update: ")
    students = get_all_students()
    found = False

    for student in students:
        if student.roll_number == roll_number:
            found = True
            print("\nStudent found.")
            print("Enter new details:")
            student.name = validators.ask_name("Enter new name: ")
            student.branch = validators.ask_branch("Enter new branch: ")

    if found:
        save_all_students(students)
        print("Student information updated successfully.")
    else:
        print("Student not found.")

def delete_student():
    roll_number = validators.ask_roll_number("Enter roll number to delete: ")
    students = get_all_students()
    remaining = []
    found = False

    for student in students:
        if student.roll_number == roll_number:
            found = True
            continue
        remaining.append(student)

    if not found:
        print("Student not found.")
        return

    if not validators.ask_confirm("Are you sure you want to delete this student?"):
        print("Delete cancelled.")
        return

    save_all_students(remaining)
    print("Student deleted successfully.")

def student_menu():
    while True:
        print("\n===== STUDENT RECORDS MENU =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
