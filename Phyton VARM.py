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

#MAIN LOOP
while True:
    print("What would you like to do?")
    print("Type b to buy stock, type v to view your portfolio")
    selection = input()
    if selection == "b":
    stock = BuyStock()
    print("You have selected:", stock)
elif selection == 'v':
    nogwat
    break

