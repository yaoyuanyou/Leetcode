# Write your MySQL query statement below
#https://leetcode.com/problems/department-top-three-salaries/description/
SELECT b.name AS Department,
    a.name AS Employee,
    a.salary AS Salary
FROM (SELECT id,
    name,
    salary,
    departmentId,
    DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS drk
    FROM Employee) a
LEFT JOIN Department b
ON a.departmentId = b.id
WHERE a.drk <= 3
ORDER BY a.id; 
