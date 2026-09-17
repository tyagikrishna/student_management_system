# Attendance class - represents one attendance entry for one student on one date

class Attendance:

    def __init__(self, roll_number, date, status):
        self.roll_number = roll_number
        self.date = date
        self.status = status

    def to_dict(self):
        return {
            "Roll Number": self.roll_number,
            "Date": self.date,
            "Status": self.status
        }

    @staticmethod
    def from_dict(row):
        return Attendance(row["Roll Number"], row["Date"], row["Status"])

    def display(self):
        print("Date:", self.date, "| Status:", self.status)
