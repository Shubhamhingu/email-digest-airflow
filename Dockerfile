FROM apache/airflow:3.0.0-python3.11

WORKDIR /opt/airflow

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy DAGs and utilities
COPY airflow/dags/ dags/
COPY airflow/utils/ utils/
COPY airflow/templates/ templates/

# Use Airflow user
USER airflow

CMD ["airflow", "standalone"]
