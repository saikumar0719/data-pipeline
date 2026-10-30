-- A simple SQL example. SQL is how we ask a database questions.
-- Read it line by line:

SELECT customer_name, SUM(amount)   -- which results do I want? name, and total money added up
FROM orders                         -- from which table? orders
GROUP BY customer_name              -- make one group for each customer
ORDER BY SUM(amount) DESC;          -- sort: biggest total first (DESC = descending, big to small)
