# strategy.py
from market import fetch_price
from news import fetch_news, sentiment_score

def generate_signal(symbol: str) -> str:
    # 1) Precio actual
    price = fetch_price(symbol)

    # 2) Noticias y sentimiento
    news_items = fetch_news(symbol)
    if news_items:
        avg_sent = sum(
            sentiment_score(item['title'] + ' ' + item.get('body', ''))
            for item in news_items
        ) / len(news_items)
    else:
        avg_sent = 0

    # 3) Lógica simple de señales
    if avg_sent > 0.3:
        return 'buy'
    elif avg_sent < -0.3:
        return 'sell'
    else:
        return 'hold'