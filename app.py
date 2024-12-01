import requests
from dotenv import load_dotenv
import os

load_dotenv()


API_KEY = os.getenv("Alpha_Vantage_API_key")
base_url = 'https://www.alphavantage.co/query'

# Define parameters
params = {
    'function': 'CURRENCY_EXCHANGE_RATE',
    'from_currency': 'USD',
    'to_currency': 'ZMW',
    'apikey': API_KEY
}

response = requests.get(base_url, params=params)
data = response.json()

# Extract the exchange rate
exchange_rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
print(f"Real-time USD/ZMW exchange rate: {exchange_rate}")
