# STEP 1: Read the raw data file.
# "Raw" means messy, just as it came. We do not fix anything here.
# We only open the file and look at it.

import csv
from pathlib import Path

# This is the folder where this project lives.
BASE_DIR = Path(__file__).resolve().parent
DEFAULT_RAW_FILE = BASE_DIR / "data" / "raw_orders.csv"


def load_rows(raw_file=DEFAULT_RAW_FILE):
    """Read a CSV file and return a list of rows.

    Each row is a dictionary (a set of name: value pairs).
    Example row: {"order_id": "O001", "amount": "250", ...}
    """
    rows = []
    with open(raw_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # first line of the CSV is the column names
        for row in reader:
            rows.append(row)
    return rows


def main():
    rows = load_rows()
    print(f"Raw rows found: {len(rows)}")
    print("First 3 rows:")
    for row in rows[:3]:
        print(row)


if __name__ == "__main__":
    main()
