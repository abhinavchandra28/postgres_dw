import psycopg2
import random

# Database connection details
DB_CONFIG = {
    "dbname": "YOUR_DATABASE",
    "user": "YOUR_USERNAME",
    "password": "YOUR_PASSWORD",
    "host": "localhost",
    "port": 5432
}

# Generate random sales data
def generate_sales_data():
    sales_data = []
    for _ in range(20):  # Generate 20 random sales
        product_id = random.randint(1, 3)
        customer_id = random.randint(1, 3)
        time_id = random.randint(1, 3)
        quantity = random.randint(1, 5)
        total_amount = quantity * random.choice([800, 500, 50])  # Corresponding product prices
        sales_data.append((product_id, customer_id, time_id, quantity, total_amount))
    return sales_data

# Insert data into fact_sales
def insert_sales_data(data):
    query = """
    INSERT INTO fact_sales (product_id, customer_id, time_id, quantity, total_amount)
    VALUES (%s, %s, %s, %s, %s)
    """
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.executemany(query, data)
        conn.commit()
        cursor.close()
        conn.close()
        print("Fact table populated successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    sales_data = generate_sales_data()
    insert_sales_data(sales_data)
