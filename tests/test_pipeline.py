# Tests check the work automatically, so we do not have to check by hand.
# These tests use only unittest, which comes free with Python.

import csv
import tempfile
import unittest
from pathlib import Path

from step1_read_raw import load_rows
from step2_clean import clean_rows, write_clean_rows
from step3_load_sql import load_to_sqlite
from step4_reports import make_reports

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_FILE = BASE_DIR / "data" / "raw_orders.csv"

# These numbers come from the sample data in data/raw_orders.csv:
# 40 raw rows - 3 duplicates - 2 missing amounts - 1 negative amount = 34
EXPECTED_CLEAN_ROWS = 34
EXPECTED_TOTAL = 9750.00


class TestPipeline(unittest.TestCase):
    def setUp(self):
        self.raw_rows = load_rows(RAW_FILE)
        self.clean = clean_rows(self.raw_rows)

    def test_raw_count(self):
        self.assertEqual(len(self.raw_rows), 40)

    def test_clean_count_is_correct(self):
        self.assertEqual(len(self.clean), EXPECTED_CLEAN_ROWS)

    def test_no_duplicates_in_clean_data(self):
        ids = [row["order_id"] for row in self.clean]
        self.assertEqual(len(ids), len(set(ids)), "clean data still has duplicates")

    def test_no_bad_amounts_in_clean_data(self):
        for row in self.clean:
            self.assertGreater(row["amount"], 0)

    def test_names_are_clean(self):
        for row in self.clean:
            name = row["customer_name"]
            self.assertEqual(name, name.strip())
            self.assertEqual(name, name.title())

    def test_daily_sales_total_equals_clean_total(self):
        # Run the full later steps in a temp folder, like CI does.
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            clean_file = write_clean_rows(self.clean, tmp_path / "clean_orders.csv")
            db_file = load_to_sqlite(clean_file, tmp_path / "shop.db")
            daily, _customers, _products = make_reports(db_file, tmp_path)

            clean_total = sum(row["amount"] for row in self.clean)
            daily_total = sum(total for _day, total in daily)
            self.assertAlmostEqual(clean_total, EXPECTED_TOTAL, places=2)
            self.assertAlmostEqual(daily_total, clean_total, places=2)

            # Also check the daily_sales.csv file itself adds up.
            with open(tmp_path / "daily_sales.csv", newline="", encoding="utf-8") as f:
                rows = list(csv.DictReader(f))
            file_total = sum(float(r["total_sales"]) for r in rows)
            self.assertAlmostEqual(file_total, EXPECTED_TOTAL, places=2)


if __name__ == "__main__":
    unittest.main()
