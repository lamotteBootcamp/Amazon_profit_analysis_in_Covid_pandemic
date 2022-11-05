import requests
from config import polygon_key
from pprint import pprint
import pandas as pd
import json

start_day = '2020-01-01'
end_day = '2022-01-01'
ticker = 'AMZN'
url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{start_day}/{end_day}?adjusted=false&sort=asc&apiKey=WXd5mRJwCsgBP72mBuUiB740rsfgvZpi'

response = requests.get(url)
json_data = response.json()
pprint(json_data)
df = pd.DataFrame(json_data['results'])
df.to_csv(f'{ticker}_stock_data_2_year_updated.csv')