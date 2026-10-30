# About the data files - in simple words

- `raw_orders.csv` - all shop orders, messy. This is the starting point.
  Columns: order_id (one number for one order), order_date (the day),
  customer_name (who bought), product (what they bought), amount (money).
- `customers.csv` - a small clean list of customers and their city.
- `products.csv` - a small clean list of products and their normal price.

Open `raw_orders.csv` first. Look for the mess: extra spaces, names in
CAPS, empty amounts, a -50 amount, and the same order_id coming twice.
