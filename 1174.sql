# Write your MySQL query statement below
# https://leetcode.com/problems/immediate-food-delivery-ii/
SELECT ROUND(AVG(CASE WHEN a.first_order = a.customer_pref_delivery_date THEN 1.0 ELSE 0.0 END)*100, 2) AS 'immediate_percentage'
FROM (SELECT customer_id, MIN(order_date) AS 'first_order',
            MIN(customer_pref_delivery_date) AS 'customer_pref_delivery_date'
    FROM Delivery
    GROUP BY customer_id) a
