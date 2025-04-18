# bot.py
from executor import execute
from apscheduler.schedulers.blocking import BlockingScheduler
from dotenv import load_dotenv
import os

load_dotenv()

SYMBOL = os.getenv('SYMBOL', 'BTCUSDT')
INTERVAL_MIN = int(os.getenv('INTERVAL_MINUTES', 5))

scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', minutes=INTERVAL_MIN)
def job():
    execute(SYMBOL)

if __name__ == '__main__':
    print(f"Iniciando bot para {SYMBOL}, cada {INTERVAL_MIN} min...")
    scheduler.start()