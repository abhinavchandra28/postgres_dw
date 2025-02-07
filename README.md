# postgres_dw
End to End Data Warehouse (postgreSQL, PySpark, Airflow)

Star Schema:
Fact Table: fact_sales
Attributes: sale_id, product_id, customer_id, time_id, quantity, total_amount.
Dimension Tables:
dim_product: product_id, product_name, category, price.
dim_customer: customer_id, customer_name, email, location.
dim_time: time_id, date, day, month, year, quarter.

Run the following SQL in PostgreSQL to create the schema:

sql
-- Create dim_product table
CREATE TABLE dim_product (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255),
    category VARCHAR(255),
    price NUMERIC
);

-- Create dim_customer table
CREATE TABLE dim_customer (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(255),
    email VARCHAR(255),
    location VARCHAR(255)
);

-- Create dim_time table
CREATE TABLE dim_time (
    time_id SERIAL PRIMARY KEY,
    date DATE,
    day INT,
    month INT,
    year INT,
    quarter INT
);

-- Create fact_sales table
CREATE TABLE fact_sales (
    sale_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES dim_product(product_id),
    customer_id INT REFERENCES dim_customer(customer_id),
    time_id INT REFERENCES dim_time(time_id),
    quantity INT,
    total_amount NUMERIC
);
