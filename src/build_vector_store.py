import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import pickle
import os

# Load Dataset
df = pd.read_csv("data/deeptriage/classifier_data_5.csv")

# Use first 100 bug reports for Milestone 1 demo
df = df.head(100)

# Combine title + description
documents = (
    df["issue_title"].fillna("") +
    " " +
    df["description"].fillna("")
).tolist()

print("Loaded", len(documents), "documents")

# Embedding Model
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

embeddings = model.encode(documents)

# Create FAISS Index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

# Create folder
os.makedirs("vector_store", exist_ok=True)

# Save index
faiss.write_index(
    index,
    "vector_store/bug_index.faiss"
)

# Save text mapping
with open(
    "vector_store/documents.pkl",
    "wb"
) as f:
    pickle.dump(documents, f)

print("FAISS index created successfully!")