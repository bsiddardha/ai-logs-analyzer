# embedding.py - drop-in replacement
from fastembed import TextEmbedding

model = TextEmbedding("sentence-transformers/all-MiniLM-L6-v2")

def embed_texts(texts):
    return list(model.embed(texts))

def embed_query(query):
    return list(model.embed([query]))[0]