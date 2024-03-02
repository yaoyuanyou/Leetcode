#Premium
SELECT DISTINCT a.id,
  a.name
FROM Accounts a
LEFT JOIN (
  SELECT id,
    login_date,
    LAG(login_date, 4) OVER(PARTITION BY id ORDER BY login_date) AS lag4
  FROM Logins
)t
USING id
WHERE DATADIFF(day, lag4, login_date) = 4;
