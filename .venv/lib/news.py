# news.py
import requests
from dotenv import load_dotenv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os

load_dotenv()
ANALYZER = SentimentIntensityAnalyzer()
API_KEY = os.getenv('NEWS_API_KEY')


def fetch_news(symbol: str) -> list:
    url = 'https://cryptopanic.com/api/v1/posts/'
    params = {'auth_token': API_KEY, 'currencies': symbol}
    data = requests.get(url, params=params).json()
    return data.get('results', [])


def sentiment_score(text: str) -> float:
    vs = ANALYZER.polarity_scores(text)
    return vs['compound']  # rango [-1, +1]