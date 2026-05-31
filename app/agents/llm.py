from langchain_groq import ChatGroq
from app.config import Config

llm=ChatGroq(model=Config.LLM_MODEL,
    api_key=Config.GROQ_API_KEY,
    temperature=0
)