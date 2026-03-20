import os

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
SERPER_API_KEY = os.environ.get("SERPER_API_KEY", "")
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
LLM_MODEL = "llama3-8b-8192"