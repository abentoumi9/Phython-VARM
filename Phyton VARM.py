

#API connection

import requests
import pandas as pd

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=53HGXB28Z5ZZKI9S'
r = requests.get(url)
data = r.json()

print(data)

data.keys()

