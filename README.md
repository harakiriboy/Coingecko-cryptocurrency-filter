# Python-assignment1

Python code which pulls the data from coingecko.com and filters out top N cryptocurrencies by market capitalization 

## Installation

first of all install the PyPI pycoingecko library

```bash
pip install pycoingecko
```
or from this source

```bash
git clone https://github.com/man-c/pycoingecko.git
cd pycoingecko
python3 setup.py install
```
Then go to download ass1.py python file from src folder above

## Usage
To start using it go to the terminal and open this ass1.py file from here
```bash
cd 'copy your file path here'
it will look like this
cd C:\Users\additionalpath\foldernamewherefilelocated
```
after this write file name and press enter
```bash
ass1.py
```
when code file executes just follow instructions in file
## Examples
### From ass1.py file

```bash
Yoo! Enter some number 'x', to get Top 'x' cryptocurrencies by Market capitalization:
3
[
    {
        'id': 'bitcoin',
        'symbol': 'btc',
        'name': 'Bitcoin',
        'image': 'https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579',
        'current_price': 42511,
        'market_cap': 800152246673,
        'market_cap_rank': 1,
        'fully_diluted_valuation': 892722227882,
        'total_volume': 41668886113,
        'high_24h': 44179,
        'low_24h': 40769,
        'price_change_24h': -1332.515189168858,
        'price_change_percentage_24h': -3.03928,
        'market_cap_change_24h': -25041971480.354248,
        'market_cap_change_percentage_24h': -3.03468,
        'circulating_supply': 18822425.0,
        'total_supply': 21000000.0,
        'max_supply': 21000000.0,
        'ath': 64805,
        'ath_change_percentage': -34.40203,
        'ath_date': '2021-04-14T11:54:46.763Z',
        'atl': 67.81,
        'atl_change_percentage': 62591.65196,
        'atl_date': '2013-07-06T00:00:00.000Z',
        'roi': None,
        'last_updated': '2021-09-21T17:19:53.827Z'
    },
    {
        'id': 'ethereum',
        'symbol': 'eth',
        'name': 'Ethereum',
        'image': 'https://assets.coingecko.com/coins/images/279/large/ethereum.png?1595348880',
        'current_price': 2930.3,
        'market_cap': 344645218111,
        'market_cap_rank': 2,
        'fully_diluted_valuation': None,
        'total_volume': 28629441542,
        'high_24h': 3108.76,
        'low_24h': 2837.14,
        'price_change_24h': -158.384345698431,
        'price_change_percentage_24h': -5.1279,
        'market_cap_change_24h': -19721354539.12378,
        'market_cap_change_percentage_24h': -5.4125,
        'circulating_supply': 117617371.1865,
        'total_supply': None,
        'max_supply': None,
        'ath': 4356.99,
        'ath_change_percentage': -32.74657,
        'ath_date': '2021-05-12T14:41:48.623Z',
        'atl': 0.432979,
        'atl_change_percentage': 676659.49517,
        'atl_date': '2015-10-20T00:00:00.000Z',
        'roi': {'times': 91.1141919425711, 'currency': 'btc', 'percentage': 9111.41919425711},
        'last_updated': '2021-09-21T17:20:52.036Z'
    },
    {
        'id': 'tether',
        'symbol': 'usdt',
        'name': 'Tether',
        'image': 'https://assets.coingecko.com/coins/images/325/large/Tether-logo.png?1598003707',
        'current_price': 1.0,
        'market_cap': 69702624114,
        'market_cap_rank': 3,
        'fully_diluted_valuation': None,
        'total_volume': 79927159662,
        'high_24h': 1.01,
        'low_24h': 0.977012,
        'price_change_24h': 0.00308345,
        'price_change_percentage_24h': 0.3088,
        'market_cap_change_24h': 459218611,
        'market_cap_change_percentage_24h': 0.66319,
        'circulating_supply': 69589506787.1884,
        'total_supply': 69589506787.1884,
        'max_supply': None,
        'ath': 1.32,
        'ath_change_percentage': -24.2968,
        'ath_date': '2018-07-24T00:00:00.000Z',
        'atl': 0.572521,
        'atl_change_percentage': 74.95,
        'atl_date': '2015-03-02T00:00:00.000Z',
        'roi': None,
        'last_updated': '2021-09-21T17:15:44.271Z'
    }
]
```

### From assignment1.py file

```bash
Yoo! Enter some number 'x', to get Top 'x' cryptocurrencies by Market capitalization:
10
1   Bitcoin   819193762057   43508
2   Ethereum   352243629251   3017.32
3   Cardano   73133072713   2.29
4   Tether   69724423875   1.01
5   Binance Coin   53280974775   346.46
6   XRP   44165731090   0.953359
7   Solana   40568489745   137.23
8   USD Coin   31080967721   1.0
9   Polkadot   30527301404   29.64
10   Dogecoin   27263904676   0.207425

```

```bash
Yoo! Enter some number 'x', to get Top 'x' cryptocurrencies by Market capitalization:
23
1   Bitcoin   819193762057   43508
2   Ethereum   352243629251   3017.32
3   Cardano   73133072713   2.29
4   Tether   69724423875   1.01
5   Binance Coin   53280974775   346.46
6   XRP   44165731090   0.953359
7   Solana   40568489745   137.23
8   USD Coin   31080967721   1.0
9   Polkadot   30527301404   29.64
10   Dogecoin   27263904676   0.207425
11   Avalanche   14971846402   68.17
12   Terra   14626488225   36.65
13   Binance USD   13747462152   1.0
14   Uniswap   12096128360   23.41
15   Chainlink   11369103255   25.15
16   Cosmos   10818941506   39.14
17   Litecoin   10168440528   152.31
18   Algorand   10046875989   1.73
19   Bitcoin Cash   9663119561   515.73
20   Wrapped Bitcoin   8928094060   43444
21   Polygon   7523053697   1.14
22   Internet Computer   7230981511   44.28
23   FTX Token   6938525508   57.52
```
