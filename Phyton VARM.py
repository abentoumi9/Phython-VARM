#LOGIN USERNAME

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

#DEFINE BUYSTOCK

import requests
import pandas as pd

stock = ["ASML", "RDSA", "AAPL"]
individual_portfolio = []             #lijst maken waar stocks append kunnen worden, PER USER

def BuyStock():
    print("The following stocks are available: ")
    teller = 0
    for s in stock:
        print(teller, ":", s)
        teller += 1
    select = int(input("Which stock would like to buy (0, 1, or 2)?: "))
    stock_select = stock[select]
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={stock_select}&interval=5min&outputsize=full&apikey=73R6EIWTFXMUJFO0'
    r = requests.get(url)
    if r.status_code != 200:
        raise ValueError("Could not retrieve data, code:", r.status_code)
    raw_data = r.json()
    data = raw_data['Time Series (5min)']
    df = pd.DataFrame(data).T.apply(pd.to_numeric)
    df.head()
    prijs = df.iloc[0]['4. close']
    print('Your stock of choice has a price of', prijs, 'USD. ')
    questionbuy = input('Would you like to buy this stock (yes/no)?')
    if questionbuy == 'yes':
        individual_portfolio.append(stock_select)
        print('Your stock has been added to your Portfolio.')
        print('You now have', ",".join(individual_portfolio), 'in your portfolio. ')
    else:
        return 'You will be redirected to the main menu. '

BuyStock()

#DEFINE SEE PERFORMANCE PORTFOLIO

def ViewPortfolio():

#MAIN LOOP

while True:
    print("What would you like to do?")
    print("Type b to buy stock, type v to view your portfolio")
    selection = input()
    if selection == "b":
    stockies = BuyStock()
    print("You have selected:", stockies)
elif selection == 'v':
    print('Which Portfolio would you like to view?')
    selection=input()
    viewport = ViewPortfolio()
    print('You want to view: ', viewport)
    break

