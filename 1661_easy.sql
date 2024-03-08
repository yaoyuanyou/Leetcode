# Write your MySQL query statement below
# https://leetcode.com/problems/average-time-of-process-per-machine/?envType=study-plan-v2&envId=top-sql-50
SELECT machine_id, ROUND(SUM(timestamp)/SUM(num/2), 3) AS processing_time
FROM (
    SELECT machine_id, activity_type,
    CASE
    WHEN activity_type = 'start' THEN -SUM(timestamp)
    ELSE SUM(timestamp)
    END AS timestamp,
    COUNT(activity_type) AS num
    FROM Activity
    GROUP BY machine_id, activity_type
) a
GROUP BY machine_id;


# A faster query
SELECT machine_id,
    ROUND(AVG(CASE
            WHEN activity_type = 'start' THEN -timestamp
            ELSE timestamp
            END) * 2, 3) AS processing_time
FROM Activity
GROUP BY machine_id;
