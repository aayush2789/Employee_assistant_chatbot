from langchain_groq import ChatGroq
from config import GROQ_API_KEY

llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",  
    temperature=0.2,
    streaming= True,
)