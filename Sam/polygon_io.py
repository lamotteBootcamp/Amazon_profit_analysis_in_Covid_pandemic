import requests
from config import polygon_key
from pprint import pprint
import pandas as pd
import json

# UNIX timestamp for 2020-01-01
start_day = '1577858400000'

# UNIX timestamp for 2022-01-01
end_day = '1641016800000'

# Amazon Ticker
ticker = 'WMT'

# url to polygon.io data REST API
url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{start_day}/{end_day}?adjusted=false&sort=asc&limit=10000&apiKey={polygon_key}'

response = requests.get(url)
json_data = response.json()
df = pd.DataFrame(json_data['results'])
df.to_csv(f'{ticker}_stock_data_2_year.csv')