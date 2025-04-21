import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY=os.getenv('GROQ_API_KEY')
BASE_DB_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "db")
