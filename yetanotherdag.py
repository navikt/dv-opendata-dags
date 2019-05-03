from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'start_date': datetime(2018, 6, 1)
}

with DAG('yetanotherdag', default_args=default_args, schedule_interval=timedelta(days=1)) as dag:
    t1 = BashOperator(
        task_id='hellodag',
        bash_command='echo "Hello dag"',
        dag=dag)
    t2 = BashOperator(
        task_id='byedag',
        bash_command='echo "Bye dag"',
        dag=dag)

    t1 >> t2
