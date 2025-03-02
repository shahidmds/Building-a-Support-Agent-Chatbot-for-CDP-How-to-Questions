import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load scraped documentation
with open("../scraper/scraped_docs.json", "r", encoding="utf-8") as f:
    docs_data = json.load(f)

docs_list = []
for source, text in docs_data.items():
    chunks = text.split(". ")
    docs_list.extend(chunks)

# Load Embedding Model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate Embeddings
embeddings = np.array([embedding_model.encode(chunk) for chunk in docs_list]).astype("float32")

# Create FAISS Index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Save FAISS Index & Documents
faiss.write_index(index, "../data/faiss_index.bin")
with open("../data/doc_texts.json", "w", encoding="utf-8") as f:
    json.dump(docs_list, f)

print("✅ FAISS Index Created Successfully!")
