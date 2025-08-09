from dotenv import load_dotenv

from lanchain_groq import ChatGroq
import os
load_dotenv()

llm= ChatGroq(groq_api_key= os.getenv("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"), model_name="llama-3.3-70b-versatile")
if __name__=="__main__":
    llm.invoke("What are the two main ingradients in samosa")
    print(response.content)

