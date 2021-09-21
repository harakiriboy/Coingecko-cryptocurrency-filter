from pycoingecko import CoinGeckoAPI # importing CoinGeckoAPI wrapper from pycoingecko library 
cg = CoinGeckoAPI() 
from rich.console import Console # import and construct object Console from rich library which helps 
                                 # to make output in terminal easier to read
console = Console()

print("Yoo! Enter some number 'x', to get Top 'x' cryptocurrencies by Market capitalization: ")
x = int(input())  # get the value of input to x variable

console.print(cg.get_coins_markets(vs_currency='usd', per_page=x)) # printing out the result
