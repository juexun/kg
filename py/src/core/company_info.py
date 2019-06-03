# -*- coding: utf-8 -*-

from dynaconf import settings
from py2neo.data import Node, Relationship
from py2neo import Graph, GraphError
from model import Company, Person, ListedCompany
from model import collect_stock_markets
from kglib.spider import AskciSpider, TushareSpider, JoinQuantSpider
from kglib.utils import dbhelper
from . import constants

def fetch_stock_list():

    g = Graph(settings.NEO4J_URL, auth=(settings.NEO4J_USER, settings.NEO4J_PASSWD))

    markets = collect_stock_markets()
    for market in markets:
        g.push(market)

    ts = TushareSpider()
    listed_companies = ts.sync_stock_info()

    for index, row in listed_companies.iterrows():  
        c = ListedCompany()
        c.name = row[TushareSpider.LISTED_COMPANY_FULLNAME]
        c.add_markets(row[TushareSpider.LISTED_COMPANY_EXCHANGE], row[TushareSpider.LISTED_COMPANY_SYMBOL])
        g.push(c)
        

def fetch_company_info(name, code):

    spider = AskciSpider()

    holdings = spider.get_holdings(code)
    stockholders = spider.get_stockholders(code)
    executives = spider.get_executives(code)

    g = Graph(settings.NEO4J_URL, auth=(settings.NEO4J_USER, settings.NEO4J_PASSWD))

    a = Company()
    a.name = name
    a.code = code

    for index, row in holdings.iterrows():
        
        c = Company()
        c.name = row[0]

        a.add_ties(c, row[1])

    for index, row in stockholders.iterrows():
        
        c = Company()
        c.name = row[0]

        a.add_stockholders(c)
        g.push(c)

    for index, row in executives.iterrows():
        
        p = Person()
        p.name = row['姓名']
        p.sex = row['性别']
        p.education = row['学历']

        a.add_exectives(p)

        if row['持股数（万股）'] == '--':
            g.push(p)
            continue

        a.add_stockholders(p)
        g.push(p)

    g.push(a)

def sync_listed_company_info():
    '''
    获取上市公司基本信息
    '''

    jq = JoinQuantSpider(settings.JOINQUANT_USER, settings.JOINQUANT_PASSWD)
    df = jq.fetch_fund_info()
    if df is None or df.empty:
        return
    dbhelper.save_df_to_mysql(df, settings.MYSQL_USER, settings.MYSQL_PASSWD, 
        settings.MYSQL_DB, constants.DB_TABLE_FUND_MAIN_INFO)

    # df = jq.fetch_shareholder_floating_top10()
    # if df is None or df.empty:
    #     return
    # dbhelper.save_df_to_mysql(df, settings.MYSQL_USER, settings.MYSQL_PASSWD, 
    #     settings.MYSQL_DB, constants.DB_TABLE_STK_SHAREHOLDER_FLOATING_TOP10)

    # df = jq.fetch_shareholder_top10()
    # if df is None or df.empty:
    #     return
    # dbhelper.save_df_to_mysql(df, settings.MYSQL_USER, settings.MYSQL_PASSWD, 
    #     settings.MYSQL_DB, constants.DB_TABLE_STK_SHAREHOLDER_TOP10)

    # df = jq.fetch_management_info()
    # if df is None or df.empty:
    #     return
    # dbhelper.save_df_to_mysql(df, settings.MYSQL_USER, settings.MYSQL_PASSWD, 
    #     settings.MYSQL_DB, constants.DB_TABLE_STK_MANAGEMENT_INFO)

    # df = jq.fetch_employee_info()
    # if df is None or df.empty:
    #     return

    # dbhelper.save_df_to_mysql(df, settings.MYSQL_USER, settings.MYSQL_PASSWD, 
    #     settings.MYSQL_DB, constants.DB_TABLE_STK_EMPLOYEE_INFO)

    # df = jq.fetch_company_info()
    # if df is None or df.empty:
    #     return
    # dbhelper.save_df_to_mysql(df, settings.MYSQL_USER, settings.MYSQL_PASSWD, 
    #     settings.MYSQL_DB, constants.DB_TABLE_STK_COMPANY_INFO)
    
