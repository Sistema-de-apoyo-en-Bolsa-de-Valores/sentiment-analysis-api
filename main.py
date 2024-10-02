from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import openai

load_dotenv()  # Loads environment variables from .env file


class ValueExpresion(BaseModel):
    content: str


app = FastAPI()


@app.post("/sentimental-analyst/")
async def say_hello(expresion: ValueExpresion):
    openai.api_key = os.environ.get("SECRET_KEY_OPENAI")
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text",
                     "text": f'Sentiment analysis of the following text:{expresion.content}, only response "POSITIVE" or "NEGATIVE"'},
                ],
            }
        ],
    )
    return {"message": f"{response.choices[0].message.content}"}
