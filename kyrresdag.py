from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'start_date': datetime(2015, 6, 1)
}

with DAG('kyrredag', default_args=default_args, schedule_interval=timedelta(days=1)) as dag:
    t1 = BashOperator(
        task_id='hellokyrre',
        bash_command='echo "Kyrre er best"',
        dag=dag)
    t2 = BashOperator(
        task_id='byekyrre',
        bash_command='echo "Ingen protest"',
        dag=dag)

    t1 >> t2
