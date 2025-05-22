# Bot-Crypto

This project is a cryptocurrency trading bot that utilizes technical analysis to identify potential buy and sell signals for Bitcoin (BTC) against USDT on the Binance exchange. It then sends these signals via Telegram messages.

## Features and Functionality

*   **Data Fetching:** Fetches real-time Bitcoin/USDT 1-minute candlestick data from the Binance exchange using the `ccxt` library.
*   **Technical Analysis:** Calculates the following technical indicators:
    *   Relative Strength Index (RSI)
    *   Exponential Moving Average (EMA)
    *   Bollinger Bands
    *   Volume Average
*   **Signal Generation:** Generates buy and sell signals based on the calculated indicators and predefined conditions.
*   **Telegram Integration:** Sends buy and sell signals to a specified Telegram chat ID using the `telegram` library.
*   **Duplicate Message Prevention:** Prevents sending duplicate buy signals to avoid redundant notifications.

## Technology Stack

*   **Python:** The core programming language.
*   **ccxt:** Cryptocurrency Exchange Trading Library for fetching market data.
*   **pandas:** Data analysis and manipulation library.
*   **ta:** Technical Analysis library for calculating indicators.
*   **python-telegram-bot:** Telegram Bot API wrapper.
*   **asyncio:** Asynchronous I/O library for concurrent execution.

## Prerequisites

Before running the bot, ensure you have the following installed:

*   **Python 3.7+**
*   **pip** (Python package installer)

You also need:

*   A Telegram bot token.  You can obtain this by creating a bot through BotFather on Telegram.
*   Your Telegram chat ID.  You can obtain this from services like [Chat ID Bot](https://telegram.me/chatid_echo_bot) or similar Telegram bots.
*   Sufficient funds in your Binance account if you intend to integrate the bot with the Binance API for automated trading (this is not implemented in the provided code, but is implied as a next step).

## Installation Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/XxGaGxX/Bot-Crypto.git
    cd Bot-Crypto
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate.bat  # On Windows
    ```

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    To generate requirements.txt, run:

    ```bash
    pip freeze > requirements.txt
    ```
    after installing all the dependencies.  This project requires the following packages: `ccxt`, `pandas`, `ta`, `python-telegram-bot`.

## Usage Guide

1.  **Configure the bot:**

    *   Open the `il_mio_genio/mainScript.py` file.
    *   Replace `"7630328411:AAE70_OfQdpxCNfa48HVAJR0MRZvlr7YUiE"` with your Telegram bot token.
    *   Replace `"716508575"` with your Telegram chat ID.

    ```python
    bot_token = "YOUR_TELEGRAM_BOT_TOKEN"
    chat_id = "YOUR_TELEGRAM_CHAT_ID"
    ```

2.  **Run the bot:**

    ```bash
    python main.py
    ```

    This will start the bot, which will begin fetching data, calculating indicators, and sending signals to your Telegram chat.  The bot will print logs to the console indicating its progress and any errors encountered.

## API Documentation

This project utilizes the following APIs:

*   **Binance API (via ccxt):**  The `ccxt` library provides a unified interface for accessing the Binance API.  The `fetch_ohlcv` method is used to retrieve candlestick data.  Refer to the [ccxt documentation](https://github.com/ccxt/ccxt) for more details.
*   **Telegram Bot API:** The `python-telegram-bot` library is used to interact with the Telegram Bot API.  The `send_message` method is used to send messages to the Telegram chat. Refer to the [python-telegram-bot documentation](https://python-telegram-bot.readthedocs.io/en/stable/) for more details.
*   **TA-Lib API:** The `ta` library is a wrapper around the TA-Lib. Refer to the [TA-Lib documentation](https://mrjbq7.github.io/ta-lib/) for more details.

## Contributing Guidelines

Contributions are welcome! If you find a bug or have an idea for a new feature, please open an issue or submit a pull request.

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes.
4.  Test your changes thoroughly.
5.  Submit a pull request.

## License Information

This project has no license specified. This means that all rights are reserved by the author. You are not allowed to copy, distribute, or modify the code without explicit permission from the author.

## Contact/Support Information

For questions or support, please open an issue on the GitHub repository.  You can also contact the repository owner directly through GitHub.