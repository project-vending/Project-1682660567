
import os

# Define the project directories
project_dir = "data_quality_monitoring"
data_dir = os.path.join(project_dir, "data")
expectations_dir = os.path.join(project_dir, "expectations")
airflow_dir = os.path.join(project_dir, "airflow")

# Create the project directories
os.makedirs(data_dir, exist_ok=True)
os.makedirs(expectations_dir, exist_ok=True)
os.makedirs(airflow_dir, exist_ok=True)

# Create the data files
data_files = ["data_file_1.csv", "data_file_2.csv", "data_file_3.csv"]
for filename in data_files:
    open(os.path.join(data_dir, filename), 'a').close()

# Create the Great Expectations files
ge_files = ["great_expectations.yml", "expectations_file_1.json", "expectations_file_2.json"]
for filename in ge_files:
    open(os.path.join(expectations_dir, filename), 'a').close()

# Create the Airflow files
airflow_files = ["dag.py", "config.py"]
for filename in airflow_files:
    open(os.path.join(airflow_dir, filename), 'a').close()
