from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="sales_etl",
    start_date=datetime(2025, 10, 22),
    schedule="@daily",
    catchup=False,
) as dag:

    run_etl = BashOperator(
        task_id="run_etl_pipeline",
        bash_command="python /opt/airflow/main.py"
    )
bash_command="docker run your-dockerhub-username/sales-etl-dataops:latest"
