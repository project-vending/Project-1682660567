
import os

# Airflow home directory
AIRFLOW_HOME = os.environ.get('AIRFLOW_HOME', '~/airflow')

# Airflow DAGs directory
DAGS_FOLDER = os.path.join(AIRFLOW_HOME, 'dags')

# Airflow logs directory
AIRFLOW_LOGS = os.path.join(AIRFLOW_HOME, 'logs')

# PostgreSQL connection settings
POSTGRES_DB_NAME = 'my_db'
POSTGRES_USERNAME = 'my_username'
POSTGRES_PASSWORD = 'my_password'
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = '5432'

# Default Airflow settings
DEFAULT_ARGS = {
    'owner': 'my_username',
    'depends_on_past': False,
    'start_date': datetime.today(),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0
}
