import sys
sys.path.append('/opt/airflow')
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

from utils.fetch_news import get_top_headlines
from utils.send_email import send_html_email

import os

API_KEY = os.environ.get("NEWSAPI_KEY")
TO_EMAIL = os.environ.get("TO_EMAIL")
FROM_EMAIL = os.environ.get("FROM_EMAIL")
LOGIN = os.environ.get("SMTP_LOGIN")
PASSWORD = os.environ.get("SMTP_PASSWORD")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def fetch_articles(ti):
    articles = get_top_headlines(API_KEY)
    ti.xcom_push(key="articles", value=articles)

def render_and_send_email(ti):
    articles = ti.xcom_pull(task_ids="fetch_articles", key="articles")
    
    env = Environment(loader=FileSystemLoader("/opt/airflow/templates"))
    template = env.get_template("digest_template.html")
    html_content = template.render(articles=articles)

    send_html_email(
        subject="🗞️ Your Daily News Digest",
        html_content=html_content,
        to_email=TO_EMAIL,
        from_email=FROM_EMAIL,
        smtp_server=SMTP_SERVER,
        smtp_port=SMTP_PORT,
        login=LOGIN,
        password=PASSWORD
    )

with DAG(
    dag_id="news_digest_dag",
    start_date=datetime(2025, 5, 18),
    schedule="@daily",
    catchup=False,
    tags=["news", "email"]
) as dag:

    fetch = PythonOperator(
        task_id="fetch_articles",
        python_callable=fetch_articles
    )

    send = PythonOperator(
        task_id="render_and_send_email",
        python_callable=render_and_send_email
    )

    fetch >> send
