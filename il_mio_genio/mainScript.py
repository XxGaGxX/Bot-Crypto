import pandas as pd
import ta.volatility
import telegram
import asyncio
from il_mio_genio.fetchData import fetch_data
from il_mio_genio.indexCalc import calculate_indicator_RSI, calculate_indicator_EMA

bot_token = "7630328411:AAE70_OfQdpxCNfa48HVAJR0MRZvlr7YUiE"
chat_id = "716508575"
last_message = ""
bot = telegram.Bot(token=bot_token)


async def run_bot():
    global last_message
    print("💹 CryptoBot avviato...")

    # per evitare messaggi duplicati
    
    # Messaggio di test per verificare che il bot Telegram funzioni
    try:
        print('bot startato')
    except Exception as e:
        print(f"❌ Errore invio messaggio test Telegram: {e}")

    try:
        while True:
            data = fetch_data("BTC", "USDT")
            print(f"Dati ricevuti: {len(data) if data else 0}")

            if not data:
                print("❌ Nessun dato ricevuto.")
                await asyncio.sleep(60)
                continue

            print(f"Esempio ultimo dato: {data[-1]}")

            df = pd.DataFrame(
                data, columns=["timestamp", "open", "high", "low", "close", "volume"]
            )
            df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

            df["rsi"] = calculate_indicator_RSI(df["close"])
            df["ema20"] = calculate_indicator_EMA(df["close"], 20)

            bb = ta.volatility.BollingerBands(df["close"], window=20, window_dev=2)
            df["bb_low"] = bb.bollinger_lband()
            df["bb_mid"] = bb.bollinger_mavg()

            df["bb_high"] = bb.bollinger_hband()
            df["volume_avg"] = df["volume"].rolling(window=5).mean()
            df["green_candle"] = df["close"] > df["open"]

            last = df.iloc[-1]
            print("Ultimi valori calcolati:")
            print(last[["close", "bb_low", "ema20", "bb_mid", "rsi"]])

            text_Buy = f"""
🚀 *Segnale di ACQUISTO - BTC/USDT*  
🕒 Timestamp: {last['timestamp'].strftime('%Y-%m-%d %H:%M')}  
💰 Prezzo Attuale: ${last['close']:.2f}  
📊 RSI: {last['rsi']:.2f}  
📈 EMA 20: ${last['ema20']:.2f}  
🔻 Banda Bassa BB: ${last['bb_low']:.2f}  

📍 Condizioni:  
• Prezzo sotto banda bassa Bollinger ✅  
• RSI sopra 40 ✅  
• Prezzo sopra EMA 20 ✅  

👉 [Compra su Bybit](https://www.bybit.com/trade/usdt/BTCUSDT)  

#Bitcoin #TradingBot
"""

            text_Sell = f"""
⚠️ *Segnale di VENDITA - BTC/USDT*  

🕒 Timestamp: {last['timestamp'].strftime('%Y-%m-%d %H:%M')}  
💰 Prezzo Attuale: ${last['close']:.2f}  
📊 RSI: {last['rsi']:.2f}  
📉 EMA 20: ${last['ema20']:.2f}  
🔹 Banda Media BB: ${last['bb_mid']:.2f}  

📍 Condizioni:  
• Prezzo sopra media BB oppure RSI > 70 ✅  

👉 [Vendi su Bybit](https://www.bybit.com/trade/usdt/BTCUSDT)  

#Bitcoin #TakeProfit
"""

            
            if (
                (last["rsi"] > 50 and last["rsi"] < 70)
                and (last["close"] > last["ema20"])
                and last["green_candle"]
                and (last["close"] > last["bb_high"])
                and (last["volume"] > last["volume_avg"])
            ):
                if last_message != text_Buy.strip():
                    print("Invio messaggio BUY BREAKOUT")
                    try:
                        await bot.send_message(
                            chat_id=chat_id, text=text_Buy, parse_mode="Markdown"
                        )
                        last_message = text_Buy.strip()
                    except Exception as e:
                        print(f"❌ Errore invio messaggio BUY: {e}")
            elif (last["close"] > last["bb_mid"]) or (last["rsi"] > 70):
                if last_message != "sell":
                    print("Invio messaggio SELL")
                    try:
                        await bot.send_message(
                            chat_id=chat_id, text=text_Sell, parse_mode="Markdown"
                        )
                        last_message = "sell"
                        print(last_message)
                    except Exception as e:
                        print(f"❌ Errore invio messaggio SELL: {e}")

            await asyncio.sleep(60)
    except asyncio.CancelledError:
        print("⏹️ Bot interrotto manualmente.")
