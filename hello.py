from airflow import DAG
from datetime import datetime
from airflow.operators.python_operator import PythonOperator
from uneven_intervals_timetable import UnevenIntervalsTimetable

def helloWorld():
    print("Hello World")

with DAG(dag_id="hello_world_dag",
         start_date=datetime(2024,1,1),
         schedule=UnevenIntervalsTimetable(),
         catchup=False) as dag:

	task1 = PythonOperator(task_id="hello_world",python_callable=helloWorld)

task1
