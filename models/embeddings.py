import os
import sys

sys.path.insert(0, "C:\\Users\\oleti\\OneDrive\\Desktop\\chatbot")

from sentence_transformers import SentenceTransformer

def get_embedder():
    try:
        return SentenceTransformer("all-MiniLM-L6-v2")
    except Exception as e:
        print(f"Embedder error: {e}")
        return None