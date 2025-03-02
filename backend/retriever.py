import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# Load FAISS Index & Docs
index = faiss.read_index("../data/faiss_index.bin")
with open("../data/doc_texts.json", "r", encoding="utf-8") as f:
    docs_list = json.load(f)

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_docs(query, top_k=3):
    query_embedding = np.array([embedding_model.encode(query)]).astype("float32")
    _, indices = index.search(query_embedding, top_k)
    return [docs_list[i] for i in indices[0]]
