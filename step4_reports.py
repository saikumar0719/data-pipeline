# STEP 4: Make reports.
# A report is a small, clear answer for the shop owner.
# We ask SQL questions and save each answer as a CSV file.
# Anyone can open a CSV report in Excel or Google Sheets.

import csv
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_DB_FILE = BASE_DIR / "output" / "shop.db"
DEFAULT_OUTPUT_DIR = BASE_DIR / "output"


def _run_query(db_file, sql):
    conn = sqlite3.connect(db_file)
    rows = conn.execute(sql).fetchall()
    conn.close()
    return rows


def get_daily_sales(db_file=DEFAULT_DB_FILE):
    """One row per day: day, total sales that day."""
    return _run_query(
        db_file,
        """
        SELECT order_date, SUM(amount)
        FROM orders
        GROUP BY order_date
        ORDER BY order_date
        """,
    )


def get_top_customers(db_file=DEFAULT_DB_FILE):
    """One row per customer: customer, total spent. Biggest first."""
    return _run_query(
        db_file,
        """
        SELECT customer_name, SUM(amount)
        FROM orders
        GROUP BY customer_name
        ORDER BY SUM(amount) DESC
        """,
    )


def get_top_products(db_file=DEFAULT_DB_FILE):
    """One row per product: product, total sold. Biggest first."""
    return _run_query(
        db_file,
        """
        SELECT product, SUM(amount)
        FROM orders
        GROUP BY product
        ORDER BY SUM(amount) DESC
        """,
    )


def _write_report(rows, output_file, header):
    output_file = Path(output_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for name, total in rows:
            writer.writerow([name, f"{total:.2f}"])
    return output_file


def make_reports(db_file=DEFAULT_DB_FILE, output_dir=DEFAULT_OUTPUT_DIR):
    """Make all 3 report files. Return the 3 lists of rows."""
    output_dir = Path(output_dir)
    daily = get_daily_sales(db_file)
    customers = get_top_customers(db_file)
    products = get_top_products(db_file)

    _write_report(daily, output_dir / "daily_sales.csv", ["order_date", "total_sales"])
    _write_report(customers, output_dir / "top_customers.csv", ["customer_name", "total_sales"])
    _write_report(products, output_dir / "top_products.csv", ["product", "total_sales"])
    return daily, customers, products


def main():
    daily, customers, products = make_reports()
    print("Report 1: Daily sales")
    for day, total in daily:
        print(f"  {day}: {total:.2f}")
    print("Report 2: Top customers")
    for name, total in customers:
        print(f"  {name}: {total:.2f}")
    print("Report 3: Top products")
    for name, total in products:
        print(f"  {name}: {total:.2f}")


if __name__ == "__main__":
    main()
