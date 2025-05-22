import ta
import ta.trend

def calculate_indicator_RSI(close):
    return ta.momentum.RSIIndicator(close, window=14).rsi()

def calculate_indicator_EMA(close,windowRange):
    return ta.trend.EMAIndicator(close, window=windowRange).ema_indicator()

