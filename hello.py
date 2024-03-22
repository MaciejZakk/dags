from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
import time
import logging

def print_hello():
	logger.info('Hello Airflow!')

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 22),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

dag = DAG(
    'DAG-1',
    default_args=default_args,
    description='A simple Airflow DAG',
    schedule_interval=timedelta(seconds=5),
)

start = DummyOperator(task_id='start', dag=dag)

hello_operator = PythonOperator(
    task_id='hello_task',
    python_callable=print_hello,
    dag=dag,
)

end = DummyOperator(task_id='end', dag=dag)

start >> hello_operator >> end
