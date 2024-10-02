from src.domain.models import ValueExpression
from src.infrastructure.openai_client import OpenAIClient

class SentimentAnalyzer:
    def __init__(self, openai_client: OpenAIClient):
        self.openai_client = openai_client

    async def analyze(self, expression: ValueExpression) -> str:
        prompt = f'Sentiment analysis of the following text:{expression.content}, only response "POSITIVE" or "NEGATIVE"'
        return await self.openai_client.get_sentiment(prompt)