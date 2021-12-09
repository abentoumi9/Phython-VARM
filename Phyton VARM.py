
#simpel: wat willen we bereiken hier?
user = input('Create Username: ')
store_user=["ron","piemel"]

if user in store_user:
    print("That user already exists")
    user = input('Create username: ')
    store_user.append(user)
else:
    store_user.append(user)

login = input('Enter your username to login. ')
if login in store_user:
    print('Welcome,', user, 'What do you want to do?')
else:
    print('Your username is not known. Please try again or create an account. ')
    login= input('Enter your username to log in. ')

#
# person = input('Do you have a username? (y/n) ')
# if person == 'y':
#     username = input('What is your username?')
#     elif username = vera, retrieve data vera
# else:
#     print('You have to setup a username.')
#     #choose username



# doel = input('Wat wilt u doen?')
# #keuzelijst: kopen/mijn portfolio performance bekijken
# #maken mensen keuze
# if doel = kopen:
#     #gebeurt keuzelijst wat je wil kopen (dictionary van 10 items)
# else:
#     #zoekt naar portfolios users
#     #> 1 portfolio: vraag om input: welke wil je bekijken?
#     #print(keuze portfolio)
#
# #API connection
#
# import requests
# import pandas as pd
#
# url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=53HGXB28Z5ZZKI9S'
# r = requests.get(url)
# data = r.json()
#
# print(data)
#
# data.keys()




