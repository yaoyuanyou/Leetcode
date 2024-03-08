# Write your MySQL query statement below
# https://leetcode.com/problems/students-and-examinations/?envType=study-plan-v2&envId=top-sql-50
SELECT student_id, student_name, subject_name, 
    CASE
    WHEN attended_exams IS NULL THEN 0
    ELSE attended_exams
    END AS attended_exams
FROM Students
JOIN Subjects
LEFT OUTER JOIN (SELECT student_id, subject_name, COUNT(student_id) AS attended_exams
FROM Examinations
GROUP BY student_id, subject_name) a
USING (student_id, subject_name)
ORDER BY student_id, subject_name;
