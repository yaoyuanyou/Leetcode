# Write your MySQL query statement below
# https://leetcode.com/problems/capital-gainloss/
SELECT
    stock_name,
    SUM(price - sell) AS capital_gain_loss
FROM (SELECT stock_name,
    operation,
    price,
    LAG(price, 1) OVER(PARTITION BY stock_name ORDER BY operation_day) AS sell
    FROM Stocks) a
WHERE operation = 'Sell'
GROUP BY stock_name;
