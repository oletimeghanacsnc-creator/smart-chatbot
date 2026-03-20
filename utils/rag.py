import faiss
import numpy as np
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer("all-MiniLM-L6-v2")
index = None
chunks = []

def build_index(text):
    global index, chunks
    try:
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_text(text)
        vecs = np.array(embedder.encode(chunks)).astype("float32")
        index = faiss.IndexFlatL2(vecs.shape[1])
        index.add(vecs)
    except Exception as e:
        print(f"RAG build error: {e}")

def retrieve(query, k=3):
    try:
        if index is None or not chunks:
            return ""
        q = np.array(embedder.encode([query])).astype("float32")
        _, I = index.search(q, k)
        return "\n\n".join(chunks[i] for i in I[0])
    except Exception as e:
        return ""