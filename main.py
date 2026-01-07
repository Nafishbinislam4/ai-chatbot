from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from llama_cpp import Llama

app = FastAPI()

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Load knowledge base
with open("data.txt", "r", encoding="utf-8") as f:
    documents = [line.strip() for line in f.readlines() if line.strip()]

doc_embeddings = embedder.encode(documents)
dimension = doc_embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(np.array(doc_embeddings))

# Load local LLM (model file will be added later)
llm = Llama(
    model_path="model.gguf",
    n_ctx=2048,
    n_threads=2
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    question_embedding = embedder.encode([req.message])
    D, I = index.search(np.array(question_embedding), k=1)
    context = documents[I[0][0]]

    prompt = f"""
You are a helpful customer support assistant.
Use the context below to answer.

Context:
{context}

Question:
{req.message}

Answer:
"""

    response = llm(prompt, max_tokens=200)
    answer = response["choices"][0]["text"].strip()

    return {"reply": answer}

@app.get("/")
def health():
    return {"status": "AI chatbot running"}

