from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from app.ingestion import ingest
from app.embedding import embed_texts, embed_query
from app.db import add_embeddings, search
from app.llm import analyze_logs

app = FastAPI(title="AI DevOps Analyzer")

# ------------------------
# Models
# ------------------------

class LogRequest(BaseModel):
    log: str

class QueryRequest(BaseModel):
    query: str

# ------------------------
# Serve UI (NO JINJA)
# ------------------------

@app.get("/")
def home():
    return FileResponse("frontend/index.html")

# ------------------------
# Health Check (Kubernetes liveness & readiness probes)
# ------------------------

@app.get("/health")
def health():
    return {"status": "healthy"}

# ------------------------
# Upload Logs
# ------------------------

@app.post("/upload")
def upload_logs(request: LogRequest):
    chunks = ingest(request.log)
    vectors = embed_texts(chunks)
    add_embeddings(vectors, chunks)

    return {"message": "Logs uploaded", "chunks": len(chunks)}

# ------------------------
# Query Logs
# ------------------------

@app.post("/query")
def query_logs(request: QueryRequest):
    query_vector = embed_query(request.query)
    results = search(query_vector)

    if not results:
        return {"answer": "No logs found"}

    context = "\n".join(results)
    answer = analyze_logs(context)

    return {"answer": answer}