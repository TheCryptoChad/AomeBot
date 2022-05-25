# AomeBot

Aome is a telegram bot capable of answering commands and having conversation. This project with Python, the [CoinGecko API](https://www.coingecko.com/en/api), and the following libraries:

- [Python-Telegram-Bot](https://pypi.org/project/python-telegram-bot/)
- [Datetime](https://pypi.org/project/DateTime/)
- [Pyjokes](https://pypi.org/project/pyjokes/)
- [Requests](https://pypi.org/project/requests/)
- [JSON](https://docs.python.org/3/library/json.html)

## Demo

You can interact with the bot [here](https://t.me/aome_bot).

## Installation

In order to run this app locally you must first clone the repository with:
```sh
git clone https://github.com/TheCryptoChad/AomeBot.git
```

Then, navigate inside the directory and install the necessary dependencies with:
```sh
pip install datetime pyjokes requests python-telegram-bot
```

Then, replace the `api_key` in `API.py`:
```
api_key = 'YOUR_BOT_API_KEY'
```

Finally, you can run the `main.py` file.

## Features

- ### Bilingual

Everything Aome can do in English, she can do in Spanish. This includes, answering commands, displaying crypto data, telling the time, telling jokes, and having a conversation.

- ### Answering Commands

Aome is capable of answering commands such as: `/start`, `/help`, `/contact`, and `/ayuda`.

![gif](./commands.gif)

- ### Having a Conversation

Aome is capable of having small conversations, like greeting the user and introducing herself. Keep in mind, the possible input from the user is not tokenized so the input must be one of the predetermined phrases for Aome to recognize and respond to it. There are multiple variations of each supported phrase included, so don't worry too much about your grammar.

![gif](./conversation.gif)

- ### Telling the Time

Aome is capable of telling the time as a response to phrases like `"tell me the time"` or `"dame la hora"`.

![gif](./time.gif)

- ### Telling Jokes

Aome is capable of telling a joke as a response to phrases like `"make me laugh"` or `"cuéntame un chiste"`.

![gif](./jokes.gif)

- ### Displaying Crypto Data

Aome can display market data for any cryptocurrency thanks to the CoinGecko API, to use this feature, simply type the name of the desired coin.

![gif](./crypto.gif)

- ### API Calls

CoinGecko's API is called upon receiving a `user_message` that is recognized as part of the API's array of cryptocurrencies. It will provide an array of different market stats for the coin, which can then be displayed.
```py
coinList = 'https://api.coingecko.com/api/v3/coins/list'
listCall = requests.get(coinList)
jsonCall = json.loads(listCall.content)
coinIds = [item["id"] for item in jsonCall]

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in (coinIds):
        page = 'https://api.coingecko.com/api/v3/coins/'
        api = requests.get(f'{page}{user_message}')
        json_data = json.loads(api.content)
        name = json_data['name']
        symbol = json_data['symbol']
        price = "{:,.2f}".format(float(json_data['market_data']['current_price']['usd']))
        high24 = "{:,.2f}".format(float(json_data['market_data']['high_24h']['usd']))
        low24 = "{:,.2f}".format(float(json_data['market_data']['low_24h']['usd']))
        market_cap = "{:,.2f}".format(float(json_data['market_data']['market_cap']['usd']))
        price1h = "{:,.2f}".format(float(json_data['market_data']['price_change_percentage_1h_in_currency']['usd']))
        price24h = "{:,.2f}".format(float(json_data['market_data']['price_change_percentage_24h_in_currency']['usd'])) 
        price7d = "{:,.2f}".format(float(json_data['market_data']['price_change_percentage_7d_in_currency']['usd'])) 
        price30d = "{:,.2f}".format(float(json_data['market_data']['price_change_percentage_30d_in_currency']['usd'])) 
        price1y = "{:,.2f}".format(float(json_data['market_data']['price_change_percentage_1y_in_currency']['usd'])) 
        return f"Displaying {name}'s Data\n\nSymbol: {symbol} | Current Price: ${price}\n\n24H High: ${high24} | 24H Low: ${low24}\n\nMarket Cap: ${market_cap}\n\nPrice Changes:\n1H: {price1h}% | 24H: {price24h}%\n7D: {price7d}% | 30D: {price30d}%\n1Y: {price1y}%\n\n\nMostrando Información de {name}\n\nSímbolo: {symbol} | Precio Actual: {price}\n\nMáx. 24H ${high24} | Mín. 24H ${low24}\n\nCapitalización de Mercado: ${market_cap}\n\nCambios en el Precio:\n1H: {price1h}% | 24H: {price24h}%\n7D: {price7d}% | 30D: {price30d}%\n1A: {price1y}%"
``` 
