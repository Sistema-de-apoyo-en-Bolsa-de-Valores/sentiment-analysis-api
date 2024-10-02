import os
import openai
from dotenv import load_dotenv

load_dotenv()

class OpenAIClient:
    def __init__(self):
        self.api_key = os.environ.get("SECRET_KEY_OPENAI")
        openai.api_key = self.api_key

    async def get_sentiment(self, prompt: str) -> str:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                    ],
                }
            ],
        )
        return response.choices[0].message.content