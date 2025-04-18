# executor.py
from market import place_order, fetch_price
from strategy import generate_signal
from dotenv import load_dotenv
import os

load_dotenv()

# Selecciona modo de tamaño
USE_RISK = os.getenv('RISK_PCT') is not None


def get_quantity(symbol: str) -> float:
    # precio actual
    price = fetch_price(symbol)

    if USE_RISK:
        # porcentaje de riesgo sobre balance en USDT
        from market import client  # para balance
        balance = float(client.get_asset_balance('USDT')['free'])
        risk_pct = float(os.getenv('RISK_PCT')) / 100
        qty = (balance * risk_pct) / price
    else:
        qty = float(os.getenv('TRADE_SIZE'))
    return round(qty, 6)


def execute(symbol: str):
    signal = generate_signal(symbol)
    qty = get_quantity(symbol)
    order = None

    if signal == 'buy':
        order = place_order(symbol, 'BUY', qty)
    elif signal == 'sell':
        order = place_order(symbol, 'SELL', qty)
    # si hold, order queda None

    print(f"{symbol} | Signal: {signal} | Qty: {qty} | Order: {order}")
    return order