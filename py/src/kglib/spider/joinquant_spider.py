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

    def fetch_employee_info(self):
        df = finance.run_query(query(finance.STK_EMPLOYEE_INFO))
        df = df.iloc[:, 2:]
        return df

    def fetch_management_info(self):
        df = finance.run_query(query(finance.STK_MANAGEMENT_INFO))
        df = df.iloc[:, 2:]
        cols = list(df)
        cols.insert(0, cols.pop(cols.index('code')))
        df = df.loc[:, cols]
        return df

    def fetch_shareholder_top10(self):
        df = finance.run_query(query(finance.STK_SHAREHOLDER_TOP10))
        df = df.drop(['id', 'company_id'], axis=1)
        cols = list(df)
        cols.insert(0, cols.pop(cols.index('code')))
        df = df.loc[:, cols]
        return df

    def fetch_shareholder_floating_top10(self):
        df = finance.run_query(query(finance.STK_SHAREHOLDER_FLOATING_TOP10))
        df = df.drop(['id', 'company_id'], axis=1)
        cols = list(df)
        cols.insert(0, cols.pop(cols.index('code')))
        df = df.loc[:, cols]
        return df

    def fetch_fund_info(self):
        df = finance.run_query(query(finance.FUND_MAIN_INFO))
        df = df.drop(['id'], axis=1)
        return df
