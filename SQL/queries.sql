# Example queries for analysis:

Total sales by product:
SELECT p.product_name, SUM(f.total_amount) AS total_sales
FROM fact_sales f
JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.product_name;
Sales by customer location:

Total sales by location:
SELECT c.location, SUM(f.total_amount) AS total_sales
FROM fact_sales f
JOIN dim_customer c ON f.customer_id = c.customer_id
GROUP BY c.location;
Sales by quarter:


Total sales by quarter:
SELECT t.quarter, SUM(f.total_amount) AS total_sales
FROM fact_sales f
JOIN dim_time t ON f.time_id = t.time_id
GROUP BY t.quarter;
