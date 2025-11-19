from airflow import DAG
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.decorators import task
from airflow.utils.dates import days_ago
from airflow.providers.postgres.hooks.postgres import PostgresHook
import json

## Define the DAG
with DAG(
    dag_id='nasa_apod_postgres',
    start_date=days_ago(1),
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    ## Step 1: Create the table if it doesn't exists
    @task
    def create_table():
        ## Initialize the Postgres hook
        postgres_hook = PostgresHook(postgres_conn_id="my_postgres_connection")

        ## SQL query to create the table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS nasa_apod (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255),
            explanation TEXT,
            url TEXT,
            date DATE
            media_type VARCHAR(50)
        );
        
        """
        ## Execute the table creation query
        postgres_hook.run(create_table_query)
    
