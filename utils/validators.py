


def is_valid_name(name):
    """Name must not be empty and must not contain digits."""

    name = name.strip()

    if name == "":
        return False

    for ch in name:
        if ch.isdigit():
            return False

    return True


def is_valid_roll_number(roll_number):
    """Roll number must be digits only."""

    roll_number = roll_number.strip()

    if roll_number == "":
        return False

    return roll_number.isdigit()


def is_valid_branch(branch):
    """Branch must not be empty."""

    return branch.strip() != ""


def is_valid_date(date):
    """Date must be in DD-MM-YYYY format."""

    parts = date.strip().split("-")

    if len(parts) != 3:
        return False

    day = parts[0]
    month = parts[1]
    year = parts[2]

    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        return False

    if len(day) != 2 or len(month) != 2 or len(year) != 4:
        return False

    if int(day) < 1 or int(day) > 31:
        return False

    if int(month) < 1 or int(month) > 12:
        return False

    return True


def is_valid_status(status):
    """Attendance status can only be P or A."""

    return status.strip().upper() in ["P", "A"]


def ask_name(message):
    """Keep asking until the user types a valid name."""

    while True:
        value = input(message)

        if is_valid_name(value):
            return value.strip()

        print("Invalid name. Name cannot be empty or contain numbers.")


def ask_roll_number(message):

    while True:
        value = input(message)

        if is_valid_roll_number(value):
            return value.strip()

        print("Invalid roll number. Please enter digits only.")


def ask_branch(message):

    while True:
        value = input(message)

        if is_valid_branch(value):
            return value.strip()

        print("Branch cannot be empty.")


def ask_date(message):

    while True:
        value = input(message)

        if is_valid_date(value):
            return value.strip()

        print("Invalid date. Please use DD-MM-YYYY format.")


def ask_status(message):

    while True:
        value = input(message)

        if is_valid_status(value):
            return value.strip().upper()

        print("Invalid status. Enter P for present or A for absent.")


def ask_confirm(message):
    """Used before deleting something."""

    answer = input(message + " (y/n): ")
    return answer.strip().lower() == "y"
