import ccxt
import pandas as pd
import ta
import time
import os
from dotenv import load_dotenv
import ta.momentum
import ta.trend

#TODO creare signal buy e sell + time.sleep(60)

exchange = ccxt.binance({})

def fetch_ohlc(symbol):
    data = exchange.fetch_ohlcv(symbol=symbol, timeframe='5m') #fetch dei valori
    df = pd.DataFrame(data=data, columns=["timestamp",'open','high','low','close','volume'])
    print(df)
    return df

def calc_indicators(df):
    macd = ta.trend.MACD(close=df['close'])
    ema = ta.trend.EMAIndicator(close=df['close'], window=20)
    df['rsi'] = ta.momentum.RSIIndicator(df['close'], window=14).rsi()
    df['macd'] = macd.macd()
    df['macd_signal'] = macd.macd_signal()
    df['zlema'] = ema.ema_indicator()
    return df


def check_indicators(df):
    last = df.iloc[-1]
    macd = last['macd']
    macd_signal = last['macd_signal']
    rsi = last['rsi']

    # se il macd interseca il signal da sopra = trend negativo
    # se il macd interseca il signal da sotto = trend positivo

    # condizione BUY, se l' RSI <= 30, il MACD è maggiore del Signal e
    # nella candela precedente il macd era sotto, è avvenuta un intersezione dal basso verso l'alto

    buy_signal = (
        (df["MACD"] > df["Signal"])
        & (df["Prev_MACD"] <= df["Prev_Signal"])
        & (df["Close"] > df["ZLEMA"])
    )
    sell_signal = (
        (df["MACD"] < df["Signal"])
        & (df["Prev_MACD"] >= df["Prev_Signal"])
        & (df["Close"] < df["ZLEMA"])
    )

    if(buy_signal):
        buy_signal()
    elif(sell_signal):
        sell_signal()
    else :
        return


def main() :
    while True:
        df = fetch_ohlc("BTC/USDT")
        df = calc_indicators(df)
        check_indicators(df)


if __name__ == "__main__" :
    main()
