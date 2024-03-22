from airflow import DAG
from datetime import datetime
from airflow.operators.python_operator import PythonOperator

def helloWorld():
    print("Hello World")

with DAG(dag_id="DAG-1",
         start_date=datetime(2024,1,1),
         schedule_interval=timedelta(seconds=10),
         catchup=False) as dag:

	task1 = PythonOperator(task_id="hello_world",python_callable=helloWorld)

task1
