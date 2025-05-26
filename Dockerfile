FROM apache/airflow:3.0.0-python3.11

WORKDIR /opt/airflow

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY airflow/dags/ dags/
COPY airflow/utils/ utils/
COPY airflow/templates/ templates/

# Expose port for Render to bind to Airflow UI
EXPOSE 8080

USER airflow

CMD ["sh", "-c", "airflow standalone --port $PORT --host 0.0.0.0"]
