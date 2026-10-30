# Learn this project in order - go slowly

Do not read everything at once. Do one step a day if you want.
After each step, run the project again and look at the numbers.

## Step 0 - Just run it

Run: `python3 pipeline.py`
What you will see: 4 step headings, raw rows 40, clean rows 34,
total sales 9750.00, top customer Priya Sharma, top product Bag.
Exercise: run it two times. See that the numbers do not change.
Running again is safe because step 3 starts the table fresh.

## Step 1 - Open the raw CSV and see the mess

Open `data/raw_orders.csv` in any text editor or spreadsheet.
What you will see: 40 orders, names like `  ravi kumar ` and
`RAVI KUMAR`, empty amounts on O031 and O032, a -50 on O033,
and O002, O005, O011 each coming two times.
Exercise: find one more messy name by eye and say how you would fix it.

## Step 2 - Read the first code file

Open `step1_read_raw.py`. It is short.
What you will see: it opens the CSV file and counts the rows.
It changes nothing. Raw in, list of rows out.
Exercise: in the terminal, run `python3 step1_read_raw.py`.
See the raw count: 40. Then close the file. That is all for now.

## Step 3 - Read the cleaning file

Open `step2_clean.py`. Read only the top comments first.
What you will see: the 5 cleaning rules - fix spaces, fix name case,
drop missing amounts, drop negative amounts, keep the last duplicate.
Exercise: add one duplicate row to `data/raw_orders.csv` (copy the
O001 line at the end, same order_id). Run `python3 pipeline.py`.
Raw becomes 41, clean stays 34. Then remove that line again.

## Step 4 - Look at the clean file

Open `output/clean_orders.csv` after a run.
What you will see: 34 rows, neat names like Ravi Kumar, no empty
amounts, no -50, each order_id only once. For O002 the amount is 120,
the LAST value, not the first value 100.
Exercise: change one amount in `data/raw_orders.csv`, for example
change O003 from 500 to 600. Run the pipeline. See total sales go
from 9750 to 9850. Then change it back and run again.

## Step 5 - Read the database and SQL file

Open `step3_load_sql.py`. Read the comments at the top first:
SELECT, FROM, WHERE, GROUP BY, ORDER BY, SUM in simple words.
What you will see: clean rows go into a table called `orders`
inside the database file `output/shop.db`, then 2 SQL queries run.
Exercise: run `python3 step3_load_sql.py` and read the daily sales
it prints. Say each line out loud: "On this day, the shop sold this much."

## Step 6 - Read the reports file

Open `step4_reports.py`, then open the 3 files in `output/`:
`daily_sales.csv`, `top_customers.csv`, `top_products.csv`.
What you will see: each report is just a SQL answer saved as a file.
Daily sales adds to 9750. Top customer is Priya Sharma, 2500.
Exercise: add the daily sales numbers on paper or a calculator.
Check they make 9750. Reports you can check by hand, you can trust.

## Step 7 - Read the tests

Open `tests/test_pipeline.py`. A test is an automatic check.
What you will see: checks for clean count = 34, no duplicates,
no bad amounts, clean names, and daily total = clean total.
Exercise: run `PYTHONPATH=. python3 -m unittest discover -s tests -v`.
See 6 tests and the word OK. Then break one thing on purpose:
change a test number, see it fail, then fix it back. Failing is safe here.

## Step 8 - Learn the words

Open `WORDS_SIMPLE.md`. Read 5 words a day, out loud.
What you will see: every big word explained in one simple line,
with an example from this shop project.
Exercise: cover the meaning, look only at the word, and say the
meaning in your own simple words. Start with: data, row, column,
table, pipeline.

## Step 9 - Practice explaining

Open `HOW_TO_EXPLAIN.md`. Read the 30-second version out loud, 3 times.
What you will see: you can already explain this whole project.
No big words needed. The shop story does the work.
Exercise: record yourself saying the 30-second version on your phone.
Listen once. That recording is your practice for a recruiter call.

## Step 10 - See the bigger projects

Open `PREVIOUS_3_PROJECTS_MAP.md` last, not first.
What you will see: your 3 bigger projects are this same shop story,
with bigger tools for bigger data.
Exercise: for each big project, say one line: "Same story, this tool
does my step ___." If you can do that, you understand them.

## Checklist - tick these off

- [ ] I ran `python3 pipeline.py` and saw total sales 9750
- [ ] I opened the raw CSV and found the duplicates and bad amounts
- [ ] I can say what step 1, 2, 3, and 4 each do, in one line each
- [ ] I added a duplicate row, re-ran, and saw clean stay at 34
- [ ] I changed one amount, re-ran, and saw the total change
- [ ] I ran the tests and saw 6 tests, OK
- [ ] I can explain SELECT, FROM, WHERE, GROUP BY, and SUM in simple words
- [ ] I can say the 30-second explanation without reading it
- [ ] I read the map and can link each big project to my 4 steps
