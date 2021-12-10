login = input('Enter username')
store_user = ["ron", "piemel"]
if login not in store_user:
    print('That user does not exist')
    user = input('Create username')
    store_user.append(user)
    print('Welcome,', user, 'What do you want to do?')
else :
    user = login
    print('Welcome,', user, 'What do you want to do?')

action = input ('Would you like to buy/watch?')
if action == 'buy':
    print('The following stocks are available: ASML, TESLA and SHELL')

    print('Which stock would you like to buy?')

else:
    print('Check these amazing stocks out!')
    print('ASML, TESLA and SHELL')



#simpel: wat willen we bereiken hier?
# action = input('Do you already have an account? (y/n)')
# store_user = ["ron", "piemel"]
# if action == 'n':
#     user = input('Create Username: ')
#     if user in store_user:
#         print("That user already exists")
#     else user = input('Create username: ')
# elif action == 'y':
#     login = input('Enter your username to login. ')
#     if login in store_user:
#         print('Welcome,', user, 'What do you want to do?')
# else:
#     store_user.append(user)
#
# else:
#     print('Your username is not known. Please try again or create an account. ')
#     login= input('Enter your username to log in. ')

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




