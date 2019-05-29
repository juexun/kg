'''
证券交易所
'''

from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom 

StockExchangeList = [
    "深圳证券交易所",
    "上海证券交易所",
    "香港证券交易所",
    "纽约证券交易所",
    "伦敦证券交易所",
    "纳斯达克证券股票交易所"
]

def collect_stock_markets():

    markets = []
    for market in StockExchangeList:
        markets.append(StockExchange(market))

    return markets

class StockExchange(GraphObject):

    __primarykey__ = "name"
    name = Property()

    def __init__(self, name):
        if name == "SZSE":
            self.name = "深圳证券交易所"
        elif name == "SSE":
            self.name = "上海证券交易所"
        else:
            self.name = name

