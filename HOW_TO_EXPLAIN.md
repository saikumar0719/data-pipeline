# How to explain this project - ready to say

Say these lines as they are. Simple words are strong.
First person: say "I", because you did this work.

## 30-second version

"I made a small data pipeline for a shop. The shop orders were messy.
Some orders came two times, some had no amount, and names were messy.
I cleaned the data with Python, put it in a database, and made reports
with SQL. In the end, I could say the true total sales: 9750."

## 1-minute version

"This is my first data project. I started with a raw file of 40 shop
orders. Raw means messy, just as it came. I wrote four small steps.
Step one, I read the file. Step two, I cleaned it: I fixed names,
removed duplicate orders, and dropped orders with missing or negative
amounts. Only 34 clean orders were left. Step three, I loaded the clean
orders into a SQLite database. Step four, I used SQL to make three
reports: daily sales, top customers, and top products. I also wrote
tests. The tests check automatically that there are no duplicates and
that the report total matches the clean data. Total sales is 9750."

## 6 basic interview questions and answers

**Q1. What is this project?**
A. "It is a small pipeline. It takes messy shop orders, cleans them,
and makes sales reports. I used Python, a CSV file, SQLite, and SQL."

**Q2. What problem did you fix?**
A. "The raw data had problems. Three orders came two times. Two orders
had no amount. One amount was negative, -50. Names had extra spaces
and different case. I fixed all of these in the cleaning step."

**Q3. What is a duplicate?**
A. "A duplicate is the same thing written two times. In my data, the
same order_id came twice. I kept only the last row, because the last
row is the newest correction."

**Q4. How did you test it?**
A. "I wrote tests with Python. The tests run the cleaning and check:
the clean count is 34, there are no duplicates, no amounts are zero
or negative, and the daily sales total equals the clean orders total,
9750. If a check fails, the test fails."

**Q5. What is SQL here?**
A. "SQL is the language I used to ask the database questions.
For example, I grouped orders by day and added the amounts with SUM.
That gave me sales for each day."

**Q6. What would you do if data is very big?**
A. "If the data is very big, I cannot use one small file on my laptop.
I would keep the files in the cloud, like S3 or BigQuery, and use a
bigger tool to clean them. The steps stay the same: read, clean, load,
report. Only the tools get bigger. That is what my other 3 projects do."
