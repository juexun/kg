'''
从Sina获取信息
'''

from bs4 import BeautifulSoup
import requests
import time

class SinaSpider:

    FUND_SHORTNAME = '基金简称'
    FUND_FULLNAME = '基金全称'
    FUND_MANAGER = '基金经理'

    def get_fund_info(self, code):
        '''获取基金信息'''

        fundUrl = "http://stock.finance.sina.com.cn/fundInfo/view/FundInfo_JJGK.php?symbol={}".format(code)

        for i in range(1, 10):
            try:
                htmlext = requests.get(fundUrl).text
                break
            except requests.ConnectionError:
                time.sleep(2*i)

        bs = BeautifulSoup(htmlext, "html5lib")

        for _, tb in enumerate(bs.find_all('table')):
            if tb.thead is None or tb.tbody is None:
                continue

            trows = tb.thead.find_all('tr')

            if len(trows) == 0 or len(trows[0].th) is None or trows[0].th.h3 is None:
                continue

            if trows[0].th.h3.string != "基金概况":
                continue

            fund = {}
            for _, trow in enumerate(tb.tbody.find_all('tr')):
                tds = trow.find_all('td')
                for i in range(0, len(tds), 2):
                    fund[tds[i].span.string] = tds[i+1].span.string

            if fund[self.FUND_FULLNAME] is None or fund[self.FUND_SHORTNAME] is None:
                return None

            return fund

    def get_manager_info(code):
        '''获取经理人信息'''

    def get_stock_info(code):
        '''获取股票信息'''