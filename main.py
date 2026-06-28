from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

# Load secrets from .env file
load_dotenv()

# Create our API app
app = FastAPI()

# Connect to Groq
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Define question structure
class Question(BaseModel):
    text: str

# Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to AI Backend!"}

# Ask endpoint
@app.post("/ask")
def ask_question(question: Question):
    # Send question to Groq LLM
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": question.text
            }
        ]
    )
    # Get answer from response
    answer = response.choices[0].message.content

    return {
        "question": question.text,
        "answer": answer
    }