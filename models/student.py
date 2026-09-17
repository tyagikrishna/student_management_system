# Student class - represents one student record

class Student:

    def __init__(self, name, roll_number, branch):
        self.name = name
        self.roll_number = roll_number
        self.branch = branch

    def to_dict(self):
        # convert object to dictionary so it can be written to csv
        return {
            "Name": self.name,
            "Roll Number": self.roll_number,
            "Branch": self.branch
        }

    @staticmethod
    def from_dict(row):
        # build a Student object from a csv row
        return Student(row["Name"], row["Roll Number"], row["Branch"])

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Branch:", self.branch)
        print("---------------------------")
