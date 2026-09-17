import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.student import Student
from models.attendance import Attendance


class TestStudent(unittest.TestCase):

    def test_to_dict(self):
        student = Student("Rahul", "101", "CSE")
        result = student.to_dict()

        self.assertEqual(result["Name"], "Rahul")
        self.assertEqual(result["Roll Number"], "101")
        self.assertEqual(result["Branch"], "CSE")

    def test_from_dict(self):
        row = {"Name": "Priya", "Roll Number": "102", "Branch": "ECE"}
        student = Student.from_dict(row)

        self.assertEqual(student.name, "Priya")
        self.assertEqual(student.branch, "ECE")


class TestAttendance(unittest.TestCase):

    def test_to_dict(self):
        entry = Attendance("101", "05-09-2026", "P")
        result = entry.to_dict()

        self.assertEqual(result["Roll Number"], "101")
        self.assertEqual(result["Status"], "P")

    def test_from_dict(self):
        row = {"Roll Number": "103", "Date": "06-09-2026", "Status": "A"}
        entry = Attendance.from_dict(row)

        self.assertEqual(entry.date, "06-09-2026")
        self.assertEqual(entry.status, "A")


if __name__ == "__main__":
    unittest.main()
