from datetime import datetime
import pyjokes
import json
import requests

time = datetime.now().strftime('%H:%M:%S')
joke = pyjokes.get_joke(language='en', category='all')
chiste = pyjokes.get_joke(language='es', category='all')

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

    if user_message in ("what's the time?", "what's the time", "whats the time?", "whats the time", "what time is it?", "what time is it", "give me the time", "time", "qué hora es?", "qué hora es", "que hora es?", "que hora es", "dime la hora", "dame la hora", "hora", "muéstrame la hora", "muestrame la hora"):
        return time

    if user_message in ("joke", "say joke", "tell me a joke", "tell a joke", "tell joke", "give me a joke", "make me laugh", "cheer me up", "lighten up the mood"):
        return joke 
    
    if user_message in ("chiste", "di un chiste", "di chiste", "dime chiste", "dime un chiste", "cuenta un chiste", "cuenta chiste", "cuéntame chiste", "cuéntame un chiste", "cuentame chiste", "cuentame un chiste", "hazme reir", "anímame", "animame", "súbeme el ánimo", "súbeme el animo", "subeme el ánimo", "subeme el animo"):
        return chiste

    if user_message in ("hello", "hi", "greetings", "good morning", "morning"):
        return "Greetings!"

    if user_message in ("hola", "holaa", "holaaa", "holis", "holiss", "holisss", "holi", "holii", "holiii", "hey", "heyy", "heyyy" "ey", "eyy", "eyyy", "buenos días", "buenos díass", "buenos díasss", "buenos dias", "buenos diass", "buenos diassss", "buen día", "buen díaa", "buen díaaa", "buen dia", "buen diaa", "buen diaaa"):
        return "Hola!"

    if user_message in ("who are you?", "who're you?", "what's your name?", "whats your name?", "what should i call you?", "who are you", "who're you", "what's your name", "whats your name", "what should i call you"):
        return "I am Aome, your personal AI assistant!"

    if user_message in ("quién eres?", "quien eres?", "quien eres", "quién eres", "cómo te llamas?", "como te llamas?", "cómo te llamas", "como te llamas", "cómo debería llamarte?",  "cómo deberia llamarte?",  "como debería llamarte?",  "como deberia llamarte?", "cómo debería llamarte",  "cómo deberia llamarte",  "como debería llamarte",  "como deberia llamarte", "cuál es tu nombre?", "cual es tu nombre?", "cuál es tu nombre", "cual es tu nombre"):
        return "Soy Aome, tu asistente personal de inteligencia artificial!"
    
    return "I don't understand what you said, check your spelling.\n\nNo entiendo lo que dijiste, revisa tu ortografía."