#LOGIN USERNAME
import json

f = open("myusersandport.txt")
usersandport = json.load(f)
f.close()

user= input('What is your username? ').lower()
pers_stocks = usersandport[user]
print('Welcome', user, ". Nice to have you back at the Pythonic Lava Investment Game! ")

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
    questionbuy = input('Would you like to buy this stock (yes/no)?')
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

# DEFINE SEE PERFORMANCE PORTFOLIO

def ViewPortfolio():
    print("What do you want to do?")
    view_actions = ["View stocks", "View balance"]
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
        print(SumPortfolio)
    else:
        print("That is not possible")
    return 'You will be redirected to the main menu. '

# #MAIN LOOP

while True:
    print("What would you like to do?")
    actions = ["Buy stock", "View portfolio"]
    teller = 0
    for s in actions:
        print(teller, ":", s)
        teller += 1
    keuze = int(input("Make your choice (0/1): "))
    if keuze == 0:
        BuyStock() #Add option to return to main menu
    elif keuze == 1:
        ViewPortfolio()
    else:
        break

