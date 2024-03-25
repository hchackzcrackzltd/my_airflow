from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.mysql_operator import MySqlOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 24),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def extract_data():
    # Code to extract data from REST API
    pass

def load_to_mysql():
    # Code to load data into MySQL
    pass

with DAG('octagontomysql', default_args=default_args, schedule_interval='@daily') as dag:

    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
    )

    load_task = PythonOperator(
        task_id='load_to_mysql',
        python_callable=load_to_mysql,
    )

    extract_task >> load_task
