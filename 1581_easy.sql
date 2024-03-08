# Write your MySQL query statement below
# https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/?envType=study-plan-v2&envId=top-sql-50
SELECT customer_id, COUNT(*) AS count_no_trans
FROM Visits
LEFT JOIN Transactions
USING (visit_id)
WHERE transaction_id IS NULL
GROUP BY customer_id;
