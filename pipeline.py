# pipeline.py - run the whole project, step by step, in order.
# A pipeline is just steps done one after another, like an assembly line.
# Run it with:  python3 pipeline.py

from pathlib import Path

from step1_read_raw import load_rows
from step2_clean import clean_rows, write_clean_rows
from step3_load_sql import load_to_sqlite
from step4_reports import make_reports

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"


def run_pipeline():
    print("=" * 50)
    print("MY FIRST DATA PIPELINE - a small shop story")
    print("=" * 50)

    print("\nSTEP 1: reading raw data")
    raw_rows = load_rows()
    print(f"Raw rows found: {len(raw_rows)}")

    print("\nSTEP 2: cleaning the data")
    clean = clean_rows(raw_rows)
    clean_file = write_clean_rows(clean, OUTPUT_DIR / "clean_orders.csv")
    print(f"Clean rows: {len(clean)}")
    print(f"Removed: {len(raw_rows) - len(clean)} rows (duplicates and bad amounts)")
    print(f"Saved clean file: {clean_file.name}")

    print("\nSTEP 3: loading clean data into a database")
    db_file = load_to_sqlite(clean_file, OUTPUT_DIR / "shop.db")
    print(f"Database file: {db_file.name}, table: orders")

    print("\nSTEP 4: making reports")
    daily, customers, products = make_reports(db_file, OUTPUT_DIR)
    total = sum(total for _day, total in daily)
    print("Daily sales:")
    for day, day_total in daily:
        print(f"  {day}: {day_total:.2f}")
    print(f"TOTAL SALES: {total:.2f}")
    print(f"Top customer: {customers[0][0]} ({customers[0][1]:.2f})")
    print(f"Top product: {products[0][0]} ({products[0][1]:.2f})")
    print("\nDone. Reports are in the output/ folder:")
    print("  output/daily_sales.csv")
    print("  output/top_customers.csv")
    print("  output/top_products.csv")
    return {
        "raw_rows": len(raw_rows),
        "clean_rows": len(clean),
        "total_sales": total,
    }


if __name__ == "__main__":
    run_pipeline()
