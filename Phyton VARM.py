#LOGIN USERNAME

# login = input('Enter username')
# store_user = ["ron", "piemel"]
# if login not in store_user:
#     print('That user does not exist')
#     user = input('Create username')
#     store_user.append(user)
#     print('Welcome,', user, 'What do you want to do?')
# else :
#     user = login
#     print('Welcome,', user, 'What do you want to do?')

#DEFINE BUYSTOCK

import requests
import pandas as pd

stock = ["ASML", "RDSA", "AAPL"]

def BuyStock():
    print("The following stocks are available: ", stock)
    select = int(input("Which stock would like to buy? (0, 1, 2):"))
    stock_select = stock[select]
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_select}&outputsize=full&apikey=73R6EIWTFXMUJFO0'
    r = requests.get(url)
    data = r.json()
    return(data)

print(BuyStock())

#DEFINE SEE PERFORMANCE PORTFOLIO
def ViewPortfolio())

# def getStocksData(ticker):
#
#     url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ + ticker + '&outputsize=full&apikey=73R6EIWTFXMUJFO0'
#
#     r = requests.get(url)
#
#     if r.status_code != 200:
#
#         raise ValueError("Could not retrieve data, code:", r.status_code)
#
#



    # def getstockcode():
    #     query = input("What would you like: ") IBM
    #
    #     url = (f'https://www.alphavantage.co/(IBM)?function=SYMBOL_SEARCH&keywords={query}&apikey=73R6EIWTFXMUJFO0')
    #     r = requests.get(url)
    #     data = r.json()




    # cars = ["Opel Astra", "BMW Z4", "Peugeot 207"]
#
# def selecteer_auto():
#     print("We hebben de volgende auto's: ", cars)
#
#     selectie = int(input("Welke auto wilt u huren (0..2)?"))
#     return cars[selectie]
#
#     def vraag_hoeveel_dagen():
#         pass
#
#     while True: print("Wat wilt u doen?")
#     print("h voor huren, s voor stop")
#     selectie = input()
#     if selectie == "h": car = selecteer_auto()
#     print("U heeft geseleteerd:", car) elif selectie == 's':
#     break


# action = input ('Would you like to buy/watch?')
# if action == 'buy':
#     print('The following stocks are available: ASML, TESLA and SHELL')
#
#     print('Which stock would you like to buy?')
#
# else:
#     print('Check these amazing stocks out!')
#     print('ASML, TESLA and SHELL')



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




