from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import populate_dimensions  
import populate_fact_table  

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    'data_warehouse_etl',
    default_args=default_args,
    description='ETL pipeline to populate data warehouse',
    schedule_interval='@daily',
    start_date=datetime(2025, 1, 1),
    catchup=False,
) as dag:

    # Task 1: Populate Dimension Tables
    populate_dimensions_task = PythonOperator(
        task_id='populate_dimensions',
        python_callable=populate_dimensions.main,  # Add a main() function to your script
    )

    # Task 2: Populate Fact Table
    populate_fact_table_task = PythonOperator(
        task_id='populate_fact_table',
        python_callable=populate_fact_table.main,  # Add a main() function to your script
    )

    # Define task dependencies
    populate_dimensions_task >> populate_fact_table_task
