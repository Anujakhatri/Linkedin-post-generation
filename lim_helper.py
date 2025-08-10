from dotenv import load_dotenv

from lanchain_groq import ChatGroq
import os
load_dotenv()

llm= ChatGroq(groq_api_key= os.getenv("your_secret_key"), model_name="llama-3.3-70b-versatile")
if __name__=="__main__":
    llm.invoke("What are the two important method to cook meat")
    print(response.content)

