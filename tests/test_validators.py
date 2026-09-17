import unittest
import sys
import os

# so the test file can import from the project folder
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import validators


class TestValidators(unittest.TestCase):

    def test_valid_name(self):
        self.assertTrue(validators.is_valid_name("Rahul Sharma"))

    def test_empty_name(self):
        self.assertFalse(validators.is_valid_name("   "))

    def test_name_with_number(self):
        self.assertFalse(validators.is_valid_name("Rahul123"))

    def test_valid_roll_number(self):
        self.assertTrue(validators.is_valid_roll_number("24BCE1001"[0:2]))
        self.assertTrue(validators.is_valid_roll_number("101"))

    def test_roll_number_with_letters(self):
        self.assertFalse(validators.is_valid_roll_number("10A"))

    def test_empty_branch(self):
        self.assertFalse(validators.is_valid_branch(""))

    def test_valid_date(self):
        self.assertTrue(validators.is_valid_date("05-09-2026"))

    def test_wrong_date_format(self):
        self.assertFalse(validators.is_valid_date("5/9/2026"))

    def test_invalid_month(self):
        self.assertFalse(validators.is_valid_date("05-13-2026"))

    def test_status(self):
        self.assertTrue(validators.is_valid_status("p"))
        self.assertTrue(validators.is_valid_status("A"))
        self.assertFalse(validators.is_valid_status("X"))


if __name__ == "__main__":
    unittest.main()
