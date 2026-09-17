import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from storage import csv_store

TEST_FILE = "data/test_temp.csv"
FIELDS = ["Name", "Roll Number", "Branch"]


class TestCsvStore(unittest.TestCase):

    def tearDown(self):
        # remove the temporary file after each test
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def test_read_missing_file(self):
        rows = csv_store.read_all("data/this_file_does_not_exist.csv")
        self.assertEqual(rows, [])

    def test_append_and_read(self):
        csv_store.append_row(TEST_FILE, FIELDS,
                             {"Name": "Rahul", "Roll Number": "101", "Branch": "CSE"})

        rows = csv_store.read_all(TEST_FILE)

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["Name"], "Rahul")

    def test_write_all_overwrites(self):
        csv_store.append_row(TEST_FILE, FIELDS,
                             {"Name": "Rahul", "Roll Number": "101", "Branch": "CSE"})

        csv_store.write_all(TEST_FILE, FIELDS,
                            [{"Name": "Priya", "Roll Number": "102", "Branch": "ECE"}])

        rows = csv_store.read_all(TEST_FILE)

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["Name"], "Priya")


if __name__ == "__main__":
    unittest.main()
