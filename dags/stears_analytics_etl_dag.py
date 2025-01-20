from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = { 
    'owner': 'airflow', 
    'depends_on_past': False, 
    'start_date': datetime(2025, 1, 1), 
    'email_on_failure': False, 
    'email_on_retry': False, 
    'retries': 1, 
    'retry_delay': timedelta(minutes=1),
}

stears_analytics_dag = DAG(
    'stears_analytics_dag',
    default_args=default_args,
    description='A data pipe line for stears data anlytics requirements',
    schedule=timedelta(seconds=30),
    catchup=False
)

run_stears_analytics_etl_task = BashOperator(
    task_id = 'run_stears_analytics_etl',
    bash_command='python /opt/airflow/stears_analytics/main.py && sleep 30 && python /opt/airflow/stears_analytics/main.py',
    dag = stears_analytics_dag
)