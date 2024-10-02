from fastapi import FastAPI, Depends
from src.domain.models import ValueExpression
from src.application.sentiment_analyzer import SentimentAnalyzer
from src.infrastructure.openai_client import OpenAIClient

app = FastAPI()

def get_sentiment_analyzer():
    openai_client = OpenAIClient()
    return SentimentAnalyzer(openai_client)

@app.post("/sentimental-analyst/")
async def analyze_sentiment(
    expression: ValueExpression,
    analyzer: SentimentAnalyzer = Depends(get_sentiment_analyzer)
):
    result = await analyzer.analyze(expression)
    return {"message": result}