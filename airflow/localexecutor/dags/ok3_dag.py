from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

# Argumentos padrão da DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
}

# Definição da DAG — usar 'schedule' em vez de 'schedule_interval'
with DAG(
    dag_id='dag_criar_arquivo_ok3',
    default_args=default_args,
    description='DAG que cria um arquivo OK.txt utilizando BashOperator',
    schedule=None,        
    catchup=False,
    tags=['exemplo', 'bash'],
) as dag:

    criar_arquivo_task = BashOperator(
        task_id='criar_arquivo_ok3_txt',
        bash_command='touch /opt/airflow/dags/OK3.txt',
    )
