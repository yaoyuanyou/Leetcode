#Premium
SELECT employee, team_size
FROM Employee
LFET JOIN (SELECT team, COUNT(*) AS team_size
          FORM Employee
          GROUP BY team)
USING team;
