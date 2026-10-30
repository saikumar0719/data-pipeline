# My First Data Pipeline - a small shop story

This is a learning project. It is built and tested locally on my
computer. It is not production. No cloud, no cost, nothing to install.
You only need Python.

## The shop story

A small shop writes down its orders every day. The list is messy:

- the same order is written two times
- some orders have no amount (the money part is empty)
- one amount is wrong: -50
- names are messy, like `  ravi kumar ` and `RAVI KUMAR`

The shop owner asks one simple question: "How much did I really sell?"

This project fixes the messy list and answers that question.
Messy data in, clean data, trusted reports out.

## What this project does - 4 steps

1. Read - open the messy orders file (`data/raw_orders.csv`)
2. Clean - fix names, remove duplicates, drop bad amounts
3. Load - put the clean orders into a small database (SQLite)
4. Report - make 3 small reports: sales per day, top customers, top products

Each step is one small Python file: `step1_read_raw.py`,
`step2_clean.py`, `step3_load_sql.py`, `step4_reports.py`.
`pipeline.py` runs all 4 steps in order.

## Run it - exact commands

```bash
cd my-first-data-pipeline
python3 pipeline.py
```

That is all. No install step, because this project uses only the
Python that is already on the computer.

To run the tests (tests check the work automatically):

```bash
PYTHONPATH=. python3 -m unittest discover -s tests -v
```

## Expected output - the numbers you should see

- Raw rows found: 40
- Clean rows: 34 (40 - 3 duplicates - 2 missing amounts - 1 negative amount)
- Daily sales:
  - 2026-10-01: 2020.00
  - 2026-10-02: 1910.00
  - 2026-10-03: 2050.00
  - 2026-10-04: 1770.00
  - 2026-10-05: 2000.00
- TOTAL SALES: 9750.00
- Top customer: Priya Sharma (2500.00)
- Top product: Bag (4020.00)

After a run, look in the `output/` folder:

- `clean_orders.csv` - the clean orders
- `daily_sales.csv`, `top_customers.csv`, `top_products.csv` - the reports
- `shop.db` - the small database file

## Read next, in this order

1. `WORDS_SIMPLE.md` - every new word, in simple words
2. `LEARN_IN_ORDER.md` - how to learn this project yourself, step by step
3. `HOW_TO_EXPLAIN.md` - what to say about this project, in simple English
4. `PREVIOUS_3_PROJECTS_MAP.md` - how this small project explains my 3 bigger projects
