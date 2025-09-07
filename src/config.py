from dotenv import load_dotenv
import os
load_dotenv()



class Settings:
    def __init__(self):
        self.GROQ_API_KEY = os.getenv("GROQ_API_KEY")
        self.TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
        self.model="llama-3.1-8b-instant"

settings = Settings()