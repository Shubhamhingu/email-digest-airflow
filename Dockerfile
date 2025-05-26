FROM apache/airflow:3.0.0-python3.11

WORKDIR /opt/airflow

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Airflow assets
COPY airflow/dags/ dags/
COPY airflow/utils/ utils/
COPY airflow/templates/ templates/

# Set permissions and use Airflow user
USER airflow

# Run airflow standalone
CMD ["airflow", "standalone"]
