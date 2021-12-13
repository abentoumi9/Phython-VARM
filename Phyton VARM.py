#LOGIN USERNAME
import json

f = open("myusersandport.txt")
usersandport = json.load(f)
f.close()

user= input('What is your username? ').lower()
pers_stocks = usersandport[user]
print("""
Welcome""", user, """. Nice to have you back at the Pythonic Lava Investment Game! """)

#loginusername
# login = input('Enter username')
# store_user = ["ron", "piemel"]
# if login not in store_user:
#     print('That user does not exist')
#     user = input('Create username')
#     store_user.append(user)
#     print('Welcome,', user, 'What do you want to do?')
# else :
#     user = login
#     print('Welcome,', user, 'What do you want to do?')ino': []

#IMPORTS
import requests
import pandas as pd
import matplotlib.pyplot

# #loginusername
# name = input('Enter username')
# usersandport = {
#     'vera':['ASML'],
#     'ron': ['MSFT', 'ASML', 'AAPL'],
#     'Martino': []
# }

#DEFINE BUYSTOCK
stock = ["ASML", "MSFT", "AAPL"]
individual_portfolio = []

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
    questionbuy = input('Would you like to buy this stock (Yes/No)? ').lower()
    if questionbuy == 'yes':
        pers_stocks.append(stock_select)
        f = open('myusersandport.txt', 'w')
        json.dump(usersandport, f)
        #usersandport[name]=stock_select
        # individual_portfolio.append(stock_select)
        print('Your stock has been added to your Portfolio.')
        print('You now have', ",".join(pers_stocks), 'in your portfolio. ')
    else:
        return 'You will be redirected to the main menu. '

def SellStock():
    print("You can sell the following stocks. ")
    teller = 0
    for s in pers_stocks:
        print(teller, ":", s)
        teller += 1
    sellstock = int(input("Which stock would like to sell (0, 1, or 2)?: "))
    try:
        stocktosell = pers_stocks[sellstock]
        print('You are about to sell', pers_stocks[sellstock], 'from your portfolio. ')
        answer = input('Do you wish to continue (Yes/No)? ').lower()
        if answer == "yes":
            pers_stocks.remove(stocktosell)
            print('You have sold', stocktosell, '. Congrats! ')
            f = open('myusersandport.txt', 'w')
            json.dump(usersandport, f)
        else:
            return 'You will now be redirected to the main menu. '
    except IndexError:
        print('That value does not exist. You will be redirected to the main menu. ')

# DEFINE SEE PERFORMANCE PORTFOLIO

def ViewPortfolio():
    print("What do you want to do? ")
    view_actions = ["View Stocks", "View Balance"]
    teller = 0
    SumPortfolio = 0
    for s in view_actions:
        print(teller, ":", s)
        teller += 1
    keuze = int(input("Make your choice (0/1): "))
    if keuze == 0:
        StockAmount = len(pers_stocks)
        print("You have", StockAmount, "stock in your portfolio, which are:", ",".join(pers_stocks))
    elif keuze == 1:
        for i in pers_stocks:
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={i}&interval=5min&outputsize=full&apikey=73R6EIWTFXMUJFO0'
            r = requests.get(url)
            if r.status_code != 200:
                raise ValueError("Could not retrieve data, code:", r.status_code)
            raw_data = r.json()
            data = raw_data['Time Series (5min)']

            df = pd.DataFrame(data).T.apply(pd.to_numeric)
            df.head()
            prijs = df.iloc[0]['4. close']
            SumPortfolio += prijs
        print('The monetary value of your Portfolio is: ', SumPortfolio, 'USD. ')
    else:
        print("That is unfortunately not possible. ")
    return 'You will be redirected to the main menu. '

# #MAIN LOOP

while True:
    print("What would you like to do? ")
    actions = ["Buy stock", "Sell Stock", "View portfolio"]
    teller = 0
    for s in actions:
        print(teller, ":", s)
        teller += 1
    keuze = int(input("Make your choice (0/1/2): "))
    if keuze == 0:
        BuyStock() #Add option to return to main menu
    elif keuze == 1:
        SellStock()
    elif keuze == 2:
        ViewPortfolio()
    else:
        break