# STEP 2: Clean the data.
# Cleaning means fixing small problems so the data can be trusted.
# Problems in our shop data:
#   1. Extra spaces in names, like "  ravi kumar "
#   2. Names in different case, like "RAVI KUMAR" and "ravi kumar"
#   3. Missing amount (empty) -> we drop that row, we cannot guess money
#   4. Negative amount, like -50 -> that is a mistake, we drop that row
#   5. Same order_id coming two times (duplicate) -> keep the LAST row,
#      because the last row is the newest correction.

import csv
from pathlib import Path

from step1_read_raw import load_rows

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_OUTPUT_FILE = BASE_DIR / "output" / "clean_orders.csv"
FIELD_NAMES = ["order_id", "order_date", "customer_name", "product", "amount"]


def clean_name(name):
    """Fix a name: remove extra spaces and make it Title Case."""
    # "  ravi   kumar " -> "Ravi Kumar"
    return " ".join((name or "").strip().split()).title()


def clean_rows(rows):
    """Take raw rows, return clean rows (a new list)."""
    by_order_id = {}  # order_id -> row. A later row replaces an earlier one.
    for row in rows:
        # Fix text fields first.
        order_id = (row.get("order_id") or "").strip()
        if not order_id:
            continue  # no order id, we cannot use this row

        # Check the amount. Amount comes as text from the CSV file.
        amount_text = (row.get("amount") or "").strip()
        if amount_text == "":
            continue  # missing value: drop the row
        try:
            amount = float(amount_text)
        except ValueError:
            continue  # not a number: drop the row
        if amount <= 0:
            continue  # negative (or zero) amount is a mistake: drop the row

        clean_row = {
            "order_id": order_id,
            "order_date": (row.get("order_date") or "").strip(),
            "customer_name": clean_name(row.get("customer_name")),
            "product": (row.get("product") or "").strip().title(),
            "amount": amount,
        }
        # If this order_id was seen before, this LAST row wins.
        by_order_id[order_id] = clean_row

    return list(by_order_id.values())


def write_clean_rows(clean_rows_list, output_file=DEFAULT_OUTPUT_FILE):
    """Write clean rows to a new CSV file."""
    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)
        writer.writeheader()
        for row in clean_rows_list:
            out = dict(row)
            out["amount"] = f"{row['amount']:.2f}"
            writer.writerow(out)
    return output_file


def main():
    raw_rows = load_rows()
    clean = clean_rows(raw_rows)
    write_clean_rows(clean)
    print(f"Raw rows: {len(raw_rows)}")
    print(f"Clean rows: {len(clean)}")
    print(f"Removed: {len(raw_rows) - len(clean)} rows (duplicates and bad amounts)")


if __name__ == "__main__":
    main()
