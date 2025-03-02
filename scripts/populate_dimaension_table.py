import psycopg2

# Database connection details
DB_CONFIG = {
    "dbname": "YOUR_DATABASE",
    "user": "YOUR_USERNAME",
    "password": "YOUR_PASSWORD",
    "host": "localhost",
    "port": 5432
}

# Sample data
products = [
    ("Laptop", "Electronics", 800),
    ("Smartphone", "Electronics", 500),
    ("Headphones", "Accessories", 50)
]

customers = [
    ("Alice", "alice@example.com", "New York"),
    ("Bob", "bob@example.com", "San Francisco"),
    ("Charlie", "charlie@example.com", "Chicago")
]

times = [
    ("2025-01-01", 1, 1, 2025, 1),
    ("2025-01-02", 2, 1, 2025, 1),
    ("2025-01-03", 3, 1, 2025, 1)
]

# Function to insert data
def insert_data(query, data):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.executemany(query, data)
        conn.commit()
        cursor.close()
        conn.close()
        print("Data inserted successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Insert into dim_product
product_query = "INSERT INTO dim_product (product_name, category, price) VALUES (%s, %s, %s)"
insert_data(product_query, products)

# Insert into dim_customer
customer_query = "INSERT INTO dim_customer (customer_name, email, location) VALUES (%s, %s, %s)"
insert_data(customer_query, customers)

# Insert into dim_time
time_query = "INSERT INTO dim_time (date, day, month, year, quarter) VALUES (%s, %s, %s, %s, %s)"
insert_data(time_query, times)
