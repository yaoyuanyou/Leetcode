# Write your MySQL query statement below
# https://leetcode.com/problems/product-sales-analysis-i/?envType=study-plan-v2&envId=top-sql-50
SELECT product_name, year, price
FROM Sales
LEFT JOIN Product
USING (product_id);
