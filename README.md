# 📬 Email Digest Generator using Apache Airflow 3 + Docker

This project automates the process of sending a daily HTML email digest with top news headlines using **Apache Airflow 3**, **Docker**, **NewsAPI**, and **SMTP (Gmail)**.

---

## 🚀 Features

- Fetches latest headlines using [NewsAPI.org](https://newsapi.org/)
- Renders them using a customizable Jinja2 HTML template
- Sends the digest via Gmail SMTP
- Dockerized with Airflow 3 support ('standalone' mode)
- Secrets and credentials stored securely in a '.env' file

---

## 🗂️ Folder Structure
```
email-digest-airflow/
├── airflow/
│ ├── dags/
│ │ └── news_digest_dag.py
│ ├── utils/
│ │ ├── fetch_news.py
│ │ └── send_email.py
│ ├── templates/
│ │ └── digest_template.html
│ ├── requirements.txt
├── .env
├── .gitignore
├── docker-compose.yaml
└── README.md
```
---

## ⚙️ Getting Started

### Prerequisites

- Docker + Docker Compose
- A [NewsAPI](https://newsapi.org/) API key
- A Gmail account with [App Passwords enabled](https://support.google.com/accounts/answer/185833)

---

### 🔐 Step 1: Create '.env'

Create a file named '.env' in the root project directory:
```
File contents as follows:
NEWSAPI_KEY=your_newsapi_key
SMTP_LOGIN=your.email@gmail.com
SMTP_PASSWORD=your_gmail_app_password
TO_EMAIL=recipient@example.com
FROM_EMAIL=your.email@gmail.com
```


### 🐳 Step 2: Run with Docker Compose
Run Your Docker Desktop Engine
```bash
docker compose up --build
```

Then access the Airflow UI at:
👉 http://localhost:8080

Default credentials (set via Airflow 3 standalone):
🔄 Airflow auto-reloads DAG changes from dags/.
You can also trigger the DAG manually in the UI or with:
```bash
docker exec -it airflow_digest airflow dags trigger news_digest_dag
```
🧾 Step 3: Python Dependencies
These are installed automatically inside Docker via requirements.txt:
```
requests
jinja2
```
If needed, update airflow/requirements.txt and rebuild:

```bash
docker compose build
```
📧 How It Works
fetch_articles pulls the latest headlines using NewsAPI

render_and_send_email uses Jinja2 to render an HTML template

Sends the result as a styled email digest using SMTP (TLS)

The HTML is rendered from templates/digest_template.html, which you can customize.

🧑‍💻 For Developers
Hot-reload supported:
Changes in:
dags/
utils/

templates/
...will reflect inside the container immediately if volumes are mounted correctly.

Check inside container:

```bash
docker exec -it airflow_digest bash
ls /opt/airflow/dags
```
🔒 Security
Use Gmail App Passwords, not your real password

Never commit .env or secrets — they’re in .gitignore

Use os.environ.get() to safely access secrets in code

✅ Git Best Practices
Add this to .gitignore:
```
gitignore
Copy
Edit
.env
__pycache__/
*.pyc
*.log
*.db
logs/
airflow/airflow.db
airflow/webserver_config.py
```
📌 Credits
Apache Airflow

NewsAPI.org

Jinja2

Gmail SMTP for mail delivery

🙌 Contributions
Pull requests welcome!
Fork the repo → Make your changes → Submit a PR ✨

yaml
Copy
Edit

---

Let me know if you'd like:
- A Markdown badge version (Docker, Python, License)
- GitHub Actions CI/CD setup
- Project license (MIT, Apache 2.0, etc.) included

Just paste the above into your `README.md`, and you're good to push to GitHub! ✅
