from services import student_service
from services import attendance_service
from services import report_service

# Entry point of the project.
# This file only shows the main menu and calls the correct module.


def main_menu():

    while True:

        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Student Records")
        print("2. Attendance")
        print("3. Reports")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_service.student_menu()

        elif choice == "2":
            attendance_service.attendance_menu()

        elif choice == "3":
            report_service.report_menu()

        elif choice == "4":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
