import config
from services import student_service
from services import attendance_service

def branch_wise_count():
    students = student_service.get_all_students()
    print("\n===== BRANCH WISE REPORT =====")
    if len(students) == 0:
        print("No students found.")
        return

    counts = {}
    for student in students:
        branch = student.branch.upper()
        if branch in counts:
            counts[branch] = counts[branch] + 1
        else:
            counts[branch] = 1

    for branch in counts:
        print(branch, ":", counts[branch], "student(s)")
    print("---------------------------")
    print("Total students:", len(students))

def attendance_summary():
    students = student_service.get_all_students()
    print("\n===== ATTENDANCE SUMMARY =====")
    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        percentage = attendance_service.calculate_percentage(student.roll_number)
        print(student.roll_number, "-", student.name, ":", percentage, "%")

def low_attendance_report():
    students = student_service.get_all_students()
    print("\n===== LOW ATTENDANCE REPORT (below", config.MINIMUM_ATTENDANCE, "%) =====")
    if len(students) == 0:
        print("No students found.")
        return

    found = False
    for student in students:
        entries = attendance_service.get_attendance_of(student.roll_number)
        if len(entries) == 0:
            continue
        percentage = attendance_service.calculate_percentage(student.roll_number)
        if percentage < config.MINIMUM_ATTENDANCE:
            found = True
            print(student.roll_number, "-", student.name, ":", percentage, "%")

    if not found:
        print("No student is below the minimum attendance.")

def topper_report():
    students = student_service.get_all_students()
    print("\n===== BEST ATTENDANCE =====")
    best_student = None
    best_percentage = -1

    for student in students:
        entries = attendance_service.get_attendance_of(student.roll_number)
        if len(entries) == 0:
            continue
        percentage = attendance_service.calculate_percentage(student.roll_number)
        if percentage > best_percentage:
            best_percentage = percentage
            best_student = student

    if best_student is None:
        print("No attendance has been marked yet.")
        return

    print("Name:", best_student.name)
    print("Roll Number:", best_student.roll_number)
    print("Branch:", best_student.branch)
    print("Attendance:", best_percentage, "%")

def report_menu():
    while True:
        print("\n===== REPORTS MENU =====")
        print("1. Branch Wise Student Count")
        print("2. Attendance Summary of All Students")
        print("3. Low Attendance Report")
        print("4. Best Attendance")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")
        if choice == "1":
            branch_wise_count()
        elif choice == "2":
            attendance_summary()
        elif choice == "3":
            low_attendance_report()
        elif choice == "4":
            topper_report()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
