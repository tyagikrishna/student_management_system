import csv
import os

def read_all(file_path):
    """Read every row of a csv file and return it as a list of dictionaries."""

    rows = []

    try:
        with open(file_path, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                rows.append(row)

    except FileNotFoundError:
       
        return []

    return rows


def write_all(file_path, fieldnames, rows):
    """Overwrite the csv file with the given list of dictionaries."""

    make_folder(file_path)

    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)


def append_row(file_path, fieldnames, row):
    """Add one row to the end of the csv file."""

    make_folder(file_path)

    file_is_new = not os.path.exists(file_path) or os.path.getsize(file_path) == 0

    with open(file_path, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if file_is_new:
            writer.writeheader()

        writer.writerow(row)


def make_folder(file_path):
    """Create the data folder if it is missing, so writing never fails."""

    folder = os.path.dirname(file_path)

    if folder != "" and not os.path.exists(folder):
        os.makedirs(folder)
