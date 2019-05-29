'''
从Tushare[https://tushare.pro/]获取信息
'''

from dynaconf import settings
import tushare

class TushareSpider:

    LISTED_COMPANY_SYMBOL="symbol"
    LISTED_COMPANY_NAME="name"
    LISTED_COMPANY_AREA="area"
    LISTED_COMPANY_FULLNAME="fullname"
    LISTED_COMPANY_EXCHANGE="exchange"

    def __init__(self):
        tushare.set_token(settings.TUSHARE_TOKEN)
        self.pro = tushare.pro_api()

    def sync_stock_info(self):
        infos = self.pro.stock_basic(fields='ts_code,symbol,name,area,industry,fullname,market,exchange,list_status,list_date')
        return infos