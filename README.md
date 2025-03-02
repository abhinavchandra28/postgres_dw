# postgres_dw
End to End Data Warehouse (postgreSQL, PySpark, Airflow)

Star Schema:
Fact Table: fact_sales
Attributes: sale_id, product_id, customer_id, time_id, quantity, total_amount.


Dimension Tables:
dim_product: product_id, product_name, category, price.
dim_customer: customer_id, customer_name, email, location.
dim_time: time_id, date, day, month, year, quarter.


The sql/create_table.sql scripts can be used to create a schema.

The data generation here is raandom which can be replaced by any other source like hdfs,s3, gcs, api etc.

The airflow setup can be further customized to populate the fact and dimensions table.
