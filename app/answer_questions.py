import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def answer_question(question: str) -> str:
    prompt = f"""
    You are a knowledgeable human assistant. Answer the following question clearly and concisely.

    Question: {question}

    Answer:
    """
    response = client.models.generate_content(
        model="gemini-2.5-pro", contents=prompt
        )
    
    return response.text.strip()
