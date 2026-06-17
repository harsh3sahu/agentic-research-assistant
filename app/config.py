from dotenv import load_dotenv

import os

load_dotenv()
class Config: 
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")
    LLM_MODEL=("llama-3.3-70b-versatile")
    TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")
    GOOGLE_API_KEY= os.getenv("GOOGLE_API_KEY")
    EMBEDDING_MODEL=("sentence-transformers/all-MiniLM-L6-v2")
    HF_TOKEN=os.getenv("HF_TOKEN")


    CHROMA_PATH="./chroma_db"
    COLLECTION_NAME=("research_documents")
    CHUNK_SIZE=1000
    CHUNK_OVERLAP=200
    TOP_K=5
    SCORE_THRESHOLD=0.5

    DATA_DIR="data"
 

