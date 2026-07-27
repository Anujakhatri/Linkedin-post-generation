import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv(dotenv_path=".env")

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "").strip()
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

llm = None

if GROQ_API_KEY:
    llm = ChatGroq(groq_api_key=GROQ_API_KEY, model_name=GROQ_MODEL)


def is_configured():
    return llm is not None


if __name__ == "__main__":
    if not is_configured():
        print("GROQ_API_KEY is not configured. Please add it to the .env file.")
    else:
        response = llm.invoke("What are the two main ingredients in samosa")
        print(response.content)

