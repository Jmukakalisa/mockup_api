from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()

# Input model
class UserInput(BaseModel):
    prompt: str

# Mock AI Response Generator
def mock_ai_response(prompt: str) -> str:
    # Simple logic to return a simulated response
    responses = [
        f"That's an interesting question: '{prompt}'. Let me think!",
        f"You mentioned '{prompt}', and I believe it's worth exploring more.",
        f"My response to '{prompt}' would be something profound if I were an AI model.",
        f"Analyzing '{prompt}'... it seems insightful!",
        f"I'm not OpenAI, but I'll say '{prompt}' is quite thought-provoking!"
    ]
    return random.choice(responses)

# API route for text processing
@app.post("/process")
async def process_text(input: UserInput):
    try:
        # Generate a mock response
        message = mock_ai_response(input.prompt)
        return {"status": "success", "response": message}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Root endpoint
@app.get("/")
async def root():
    return {"message": "API is running!"}
