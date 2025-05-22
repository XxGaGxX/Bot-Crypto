import ccxt

def fetch_data(crypto, coin):
    exchange = ccxt.binance()
    try:
        ticker = exchange.fetch_ohlcv(f"{crypto}/{coin}", '1m', limit=1000)
        return ticker
    except Exception as e:
        print(f"Errore fetch_data: {e}")
        return []
