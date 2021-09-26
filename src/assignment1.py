from pycoingecko import CoinGeckoAPI # importing CoinGeckoAPI wrapper from pycoingecko library 
cg = CoinGeckoAPI() 
from rich.console import Console # import and construct object Console from rich library which helps 
                                 # to make output in terminal easier to read
console = Console()
from tabulate import tabulate

class Coin:
    def __init__(self, rank, name, market_capitalization, crypto_price):  # creating Coin class to store only needed data 
        self.rank = rank                                    # on the instance of this class 
        self.name = name
        self.market_capitalization = market_capitalization
        self.crypto_price = crypto_price

print("Yoo! Enter some number 'x', to get Top 'x' cryptocurrencies by Market capitalization: ")
x = int(input())  # get the value of input to x variable

allmarket = cg.get_coins_markets(vs_currency='usd') # assigning the get_coin function value to allmarket variable, to store the data in this variable
start = 1      # our iterator which help us get elements until we reach the last element in ranking                                      

allmarket = sorted(allmarket, key=lambda cap: cap['market_cap'], reverse=True) # python in build function to sort data, here is used lambda function 
                                                                          # to sort directly by market_capitalization 
ranking = [] # creating empty list to store sorted cryptocurrencies

for currency in allmarket:  # starting for loop to create instance of Coin class and assigning its value to this list
    name = currency['name']
    market_capitalization = currency['market_cap']
    rank = currency['market_cap_rank']
    price = currency['current_price']
    newcoin = Coin(rank,name,market_capitalization,price) # creating the object of Coin class
    ranking.append(newcoin) # adding into the list
    start = start + 1 # iterating process
    if start > x: # declaring the if statement as a trigger to stop for loop
        break

for i in ranking: # creating another for loop to display cryptocurrencies from list
    console.print(str(i.rank) + "  ", str(i.name) + "  ", str(i.market_capitalization) + "  ", str(i.crypto_price) + "  ")
    #console.print(i.rank, i.name, i.market_capitalization, i.crypto_price)
