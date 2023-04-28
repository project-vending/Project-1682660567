python
import os
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from great_expectations.core import ExpectationSuiteValidationResult
from great_expectations import DataContext

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 2),
    'retry_delay': timedelta(minutes=5),
}


def validate_data_expectations():
    context = DataContext(os.path.join(os.getcwd(), 'data_quality_monitoring', 'expectations'))
    suite = context.get_expectation_suite('data_quality_suite')
    batch_kwargs = {'path': os.path.join(os.getcwd(), 'data_quality_monitoring', 'data')}
    batch = suite.get_batch(batch_kwargs=batch_kwargs)
    result = batch.validate(expectation_suite=suite)
    if isinstance(result, ExpectationSuiteValidationResult):
        return result.success
    else:
        return False


with DAG('data_quality_monitoring_dag', default_args=default_args, schedule_interval='@daily') as dag:

    t1 = PythonOperator(
        task_id='validate_data_quality',
        python_callable=validate_data_expectations,
        dag=dag
    )
