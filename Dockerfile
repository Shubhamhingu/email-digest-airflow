FROM apache/airflow:3.0.0-python3.11

WORKDIR /opt/airflow

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY airflow/dags/ dags/
COPY airflow/utils/ utils/
COPY airflow/templates/ templates/

EXPOSE 8080

USER airflow

# ✅ Use bash to resolve $PORT at runtime
ENTRYPOINT ["bash", "-c"]
CMD ["airflow standalone"]
