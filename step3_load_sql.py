# STEP 3: Put clean data into a database and ask questions with SQL.
# A database is an organised place to keep tables.
# SQLite is a small database that lives in ONE file: shop.db
# SQL is the language we use to ask the database questions.
#
# Words used in the SQL below:
#   SELECT  = which columns (or results) do I want?
#   FROM    = which table?
#   WHERE   = only rows that match this rule (a filter)
#   GROUP BY = make one group for each value (example: one group per day)
#   ORDER BY = sort the result (example: by date, oldest first)
#   SUM     = add up all the numbers in a group

import csv
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DEFAULT_CLEAN_FILE = BASE_DIR / "output" / "clean_orders.csv"
DEFAULT_DB_FILE = BASE_DIR / "output" / "shop.db"


def load_to_sqlite(clean_file=DEFAULT_CLEAN_FILE, db_file=DEFAULT_DB_FILE):
    """Load clean_orders.csv into the SQLite table called orders."""
    db_file = Path(db_file)
    db_file.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    # Start fresh each time, so running twice does not double the data.
    cur.execute("DROP TABLE IF EXISTS orders")
    cur.execute(
        """
        CREATE TABLE orders (
            order_id TEXT,
            order_date TEXT,
            customer_name TEXT,
            product TEXT,
            amount REAL
        )
        """
    )
    with open(clean_file, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO orders VALUES (?, ?, ?, ?, ?)",
                (
                    row["order_id"],
                    row["order_date"],
                    row["customer_name"],
                    row["product"],
                    float(row["amount"]),
                ),
            )
    conn.commit()
    count = cur.execute("SELECT COUNT(*) FROM orders").fetchone()[0]
    conn.close()
    print(f"Rows loaded into database table 'orders': {count}")
    return db_file


def query_daily_sales(db_file=DEFAULT_DB_FILE):
    """SQL query 1: total sales for each day."""
    conn = sqlite3.connect(db_file)
    # SELECT the day, SUM (add up) the amount,
    # FROM the orders table,
    # GROUP BY day (one result row per day),
    # ORDER BY day (sort, oldest day first).
    rows = conn.execute(
        """
        SELECT order_date, SUM(amount)
        FROM orders
        GROUP BY order_date
        ORDER BY order_date
        """
    ).fetchall()
    conn.close()
    return rows


def query_big_orders(db_file=DEFAULT_DB_FILE, minimum=400):
    """SQL query 2: only big orders (this is a WHERE filter)."""
    conn = sqlite3.connect(db_file)
    # WHERE keeps only rows where amount is bigger than the minimum.
    rows = conn.execute(
        """
        SELECT order_id, customer_name, product, amount
        FROM orders
        WHERE amount > ?
        ORDER BY amount DESC
        """,
        (minimum,),
    ).fetchall()
    conn.close()
    return rows


def main():
    load_to_sqlite()
    print("Daily sales from SQL:")
    for day, total in query_daily_sales():
        print(f"  {day}: {total:.2f}")
    print("Big orders over 400 from SQL:")
    for row in query_big_orders():
        print(f"  {row}")


if __name__ == "__main__":
    main()
