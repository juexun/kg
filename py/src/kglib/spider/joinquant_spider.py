# -*- coding: utf-8 -*-

'''
从JoinQuant[https://www.joinquant.com]获取信息
'''

from jqdatasdk import auth, finance, query

class JoinQuantSpider:

    def __init__(self, user, passwd):
        auth(user, passwd)

    def fetch_company_info(self):
        df = finance.run_query(query(finance.STK_COMPANY_INFO))
        df = df.iloc[:, 2:]
        return df
