from langchain_groq import ChatGroq
from app.config import Config
from langchain_google_genai import ChatGoogleGenerativeAI

# llm=ChatGroq(model=Config.LLM_MODEL,
#     api_key=Config.GROQ_API_KEY,
#     temperature=0
# )

llm = ChatGoogleGenerativeAI(model='gemini-2.5-flash',
api_key= Config.GOOGLE_API_KEY,
temperature=0)