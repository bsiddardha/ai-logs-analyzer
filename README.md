# 🧠 AI DevOps Analyzer

AI-powered log analysis platform that helps DevOps engineers identify failures, root causes, severity levels, and recommended fixes from application logs.

---

## 🚀 Features

* Upload application logs
* Semantic log search using vector embeddings
* AI-powered root cause analysis
* Severity assessment
* Fix recommendations
* FastAPI REST API
* Interactive web interface
* Docker support
* Docker Compose support
* GitHub Actions CI/CD pipeline
* Docker Hub deployment

---

## 🏗️ Architecture

```text
User
 │
 ▼
Frontend (HTML + JavaScript)
 │
 ▼
FastAPI Backend
 │
 ├── Log Ingestion
 ├── Embedding Generation
 ├── FAISS Vector Search
 └── Groq LLM Analysis
```

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* Uvicorn
* Pydantic

### AI / ML

* Groq (LLaMA 3)
* Sentence Transformers
* FAISS

### Frontend

* HTML
* CSS
* JavaScript

### DevOps

* Docker
* Docker Compose
* GitHub Actions
* Docker Hub

---

## 📁 Project Structure

```text
ai-devops-analyzer/
│
├── app/
│   ├── main.py
│   ├── ingestion.py
│   ├── embedding.py
│   ├── retrieval.py
│   ├── db.py
│   └── llm.py
│
├── frontend/
│   └── index.html
│
├── logs/
│
├── .github/
│   └── workflows/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Local Setup

### 1. Clone Repository

```bash
git clone https://github.com/your-username/ai-devops-analyzer.git

cd ai-devops-analyzer
```

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

### 5. Get a Groq API Key

1. Create an account on Groq.
2. Generate an API key.
3. Add it to the `.env` file.

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://localhost:8000
```

API Documentation:

```text
http://localhost:8000/docs
```

---

## 🐳 Docker

### Build Image

```bash
docker build -t ai-devops-analyzer .
```

### Run Container

```bash
docker run -p 8000:8000 --env-file .env ai-devops-analyzer
```

Open:

```text
http://localhost:8000
```

---

## 🐳 Docker Compose

### Start Application

```bash
docker compose up --build
```

### Run in Background

```bash
docker compose up -d
```

### Stop Application

```bash
docker compose down
```

---

## 🔄 CI/CD Pipeline

GitHub Actions automatically:

1. Builds the Docker image
2. Pushes the image to Docker Hub

Triggered on:

* Push to `main`

---

## 📄 Sample Logs

```text
2026-04-23 10:02:49 ERROR [db] Connection timeout
2026-04-23 10:02:52 ERROR [db] Connection refused
2026-04-23 10:02:52 CRITICAL Service failed
2026-04-23 10:02:55 Pod restarting (CrashLoopBackOff)
```

---

## 💡 Example Questions

```text
Why did the service fail?

What is the root cause?

How can I fix this issue?

What is the severity level?

Summarize these logs.
```

---

## 🔐 Security

* `.env` is excluded using `.gitignore`
* API keys are never committed to source control
* Environment variables are loaded securely

---

## ⚠️ Common Issues

### GROQ_API_KEY Not Found

Ensure:

* `.env` exists in the project root
* The API key is valid
* The application is restarted after updating the `.env` file

### First Run Is Slow

The embedding model may need to download on the first run. Subsequent runs will be significantly faster.

---

## 🚀 Future Enhancements

* Kubernetes Deployment
* Real-Time Log Streaming
* Multiple LLM Support
* Authentication & Authorization
* Grafana Integration
* Cloud Deployment (AWS / Azure)

---

## 👨‍💻 Author

**B Siddardha**


