# Write your MySQL query statement below
# https://leetcode.com/problems/game-play-analysis-iv/
SELECT ROUND(COUNT(player_id)/(SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM (SELECT player_id,
        event_date,
        MIN(event_date) OVER(PARTITION BY player_id ORDER BY event_date) AS initial_date
    FROM Activity) a
WHERE DATEDIFF(event_date, initial_date) = 1;
