# market.py
from binance.client import Client
from dotenv import load_dotenv
import os

# Carga variables de entorno\load_dotenv()
API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv('BINANCE_SECRET_KEY')

# Instancia cliente
client = Client(API_KEY, API_SECRET)


def fetch_price(symbol: str) -> float:
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker['price'])


def place_order(symbol: str, side: str, quantity: float):
    order = client.create_order(
        symbol=symbol,
        side=side.upper(),
        type='MARKET',
        quantity=quantity
    )
    return order