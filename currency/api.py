import requests
import os 

COINMARKETCAP_API_KEY = os.environ.get("COINMARKETCAP_API_KEY")

# from https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide


def fetch_data_from_coinmarketcap():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY,
    }
    params = {
        'start': '1',
        'limit': '30',
        'convert': 'USD',
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Failed to retrieve data: {response.text}')
