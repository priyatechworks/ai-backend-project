from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Welcome to AI Backend!"}

@app.post("/ask")
def ask_question(question: Question):
    return {
        "question": question.text,
        "answer": "AI answer will come here in Stage 6!"
    }