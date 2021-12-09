
#simpel: wat willen we bereiken hier?

doel = input('Wat wilt u doen?')
#keuzelijst: kopen/mijn portfolio performance bekijken
if doel = kopen:
    #gebeurt keuzelijst wat je wil kopen (dictionary van 10 items)
else:
    #zoekt naar portfolios users
    #vraag om input: welke wil je bekijken?
    #print(keuze portfolio)

#API connection

import requests
import pandas as pd

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=53HGXB28Z5ZZKI9S'
r = requests.get(url)
data = r.json()

print(data)

data.keys()




