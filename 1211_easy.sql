# Write your MySQL query statement below
#https://leetcode.com/problems/queries-quality-and-percentage/
SELECT a.query_name, ROUND(AVG(a.rating/position), 2) AS quality, CASE WHEN b.rating IS NULL THEN 0 ELSE ROUND(b.rating/ COUNT(a.query_name) * 100, 2) END AS poor_query_percentage
FROM Queries a
LEFT JOIN (SELECT query_name, COUNT(*) AS 'rating' FROM Queries  WHERE rating < 3 GROUP BY query_name) b ON a.query_name = b.query_name
WHERE a.query_name IS NOT NULL
GROUP BY a.query_name;
