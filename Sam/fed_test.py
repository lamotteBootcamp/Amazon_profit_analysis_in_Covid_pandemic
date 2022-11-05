import requests
from config import fred_key
from pprint import pprint
import pandas as pd
# from config import who_key

start = input("enter a start date (YYYY-MM-DD): ")
end = input("enter an end date (YYYY-MM-DD): ")
url = f'https://api.stlouisfed.org/fred/series?series_id=DPRIME&api_key={fred_key}&file_type=json&realtime_start={start}&realtime_end={end}'

response = requests.get(url)
pprint(response.json())

# df = pd.read_json(response.json())
# df.head()