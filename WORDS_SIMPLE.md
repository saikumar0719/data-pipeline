# Words in simple words

Read this slowly. One word at a time. Every word has an example
from this shop project. You can repeat these lines in an interview.

- **Data** — facts written down, like names, dates, and money — the shop orders are data.
- **Row** — one line in a table, for one thing — one row is one order, like O001.
- **Column** — one kind of fact in every row, top to bottom — the amount column holds money.
- **Table** — rows and columns together, like a neat list — the orders table has 34 clean rows.
- **Database** — a place that keeps tables in an organised way — our database is the file shop.db.
- **CSV file** — a simple text file where values are split by commas — raw_orders.csv is a CSV file.
- **SQL** — the language used to ask a database questions — we use SQL to get daily sales.
- **Query** — one question asked in SQL — "total sales for each day" is a query.
- **Script** — a small file of instructions for the computer — step2_clean.py is a script.
- **Program** — instructions that do a job when you run them — pipeline.py is a small program.
- **Run** — tell the computer to do the instructions — you run pipeline.py in the terminal.
- **Terminal / command** — the window where you type instructions — `python3 pipeline.py` is a command.
- **Bug** — a mistake in the instructions or the data — a -50 amount is a data bug we drop.
- **Test** — an automatic check that the work is right — our tests check there are no duplicates.
- **Pipeline** — steps done one after another, in order — read, clean, load, report is our pipeline.
- **Raw data** — data just as it came, still messy — raw_orders.csv is raw data.
- **Clean data** — data after fixing the mess, ready to trust — clean_orders.csv is clean data.
- **Report** — a small clear answer made from data — daily_sales.csv is a report.
- **Duplicate** — the same thing written two times — order O002 came twice, we kept the last one.
- **Missing value / null** — an empty place where a value should be — two orders had no amount.
- **Filter** — keep only rows that match a rule — we keep only amounts bigger than 0.
- **Group by** — put rows into groups that share a value — group orders by day to get daily sales.
- **Sum** — add numbers up — SUM adds all amounts in a group to give a total.
- **Sort** — put results in order, like big to small — top customers are sorted by total spent.
- **Join** — matching rows from two tables using a shared value — orders can join customers on the customer name.
- **File** — one saved thing on the computer — README.md is a file.
- **Folder** — a place that holds files — the data folder holds the CSV files.
- **Python** — a simple, popular language for writing scripts — all our step files are Python.
- **GitHub** — a website that keeps code and its history — my projects live on GitHub.
- **Repository / repo** — one project folder kept on GitHub — this project would be one repo.
- **Commit** — one saved change on GitHub, with a short message — saving the cleaned code is a commit.
- **README** — the first file that explains a project in simple words — this project's README tells the shop story.
- **Cloud** — other computers on the internet that store data and run work — BigQuery and S3 live in the cloud.
- **Batch** — doing a job on a whole group at once, like once a day — our pipeline runs on one file at a time, a batch.
- **Streaming** — data coming live, second by second, not in one file — a shop app sending each order at once is streaming.
- **Warehouse** — a very big database in the cloud for reports — BigQuery is a data warehouse.
- **Lake / lakehouse** — a big place in the cloud that keeps raw and clean files, ready for questions — S3 with clean tables is a lakehouse.

When a big word scares you, come back here. Big projects use these
same words. Only the tools get bigger. The idea stays the same.
