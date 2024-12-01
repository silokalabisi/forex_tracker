import requests
from dotenv import load_dotenv
import os

load_dotenv()


API_KEY = os.getenv("Alpha_Vantage_API_key")
base_url = 'https://www.alphavantage.co/query'

# Define parameters

# US Dollar
params = {
    'function': 'CURRENCY_EXCHANGE_RATE',
    'from_currency': 'USD',
    'to_currency': 'ZMW',
    'apikey': API_KEY
}

# Chinese Yuan
paramsCH = {
    'function': 'CURRENCY_EXCHANGE_RATE',
    'from_currency': 'USD',
    'to_currency': 'CNY',
    'apikey': API_KEY
}

#  US
response = requests.get(base_url, params=params)
data = response.json()

#  China
responseCH = requests.get(base_url, params=paramsCH)
dataCH = responseCH.json()

# Extract the exchange rate
# US
exchange_rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
print(f"Real-time USD/ZMW exchange rate: {exchange_rate}")
# China
exchange_rateCH = dataCH['Realtime Currency Exchange Rate']['5. Exchange Rate']
print(f"Real-time USD/CNY exchange rate: {exchange_rateCH}")
