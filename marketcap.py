import requests,time
from pycoingecko import CoinGeckoAPI as ziz
coin = ziz()
cakee = coin.get_price(ids='pancakeswap', vs_currencies='idr')
cake = str(cakee).split("idr': ")[1].split("}")[0]
