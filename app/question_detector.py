import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def detect_questions_llm(text):
    prompt = f"""
    You are a helpful assistant. From the following transcript, extract every spoken question as a list. 
    Only include actual questions, not statements. Return them as plain numbered lines.

    Transcript:
    \"\"\"{text}\"\"\"

    Questions:
    """

    response = client.models.generate_content(
        model="gemini-2.5-pro", contents=prompt
        )
    
    extracted = response.candidates[0].content.parts[0].text.strip()

    questions = [line.strip("-• ") for line in extracted.split("\n") if line.strip()]

    return questions
