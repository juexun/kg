# -*- coding: utf-8 -*-

from dynaconf import settings

from py2neo.data import Node, Relationship
from py2neo import Graph, GraphError, NodeMatcher

from model import Company, Person, ListedCompany
from model import StockCompanyInfo
from model import StockManagementInfo
from model import collect_stock_markets
from kglib.spider import AskciSpider, TushareSpider, JoinQuantSpider
from kglib.utils import dbhelper, new_db_session
from kglib.utils import neo4jhelper

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
    
    # jq = JoinQuantSpider(settings.JOINQUANT_USER, settings.JOINQUANT_PASSWD)
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

def map_all_company_managers():

    session = new_db_session()

    managers = session.query(StockManagementInfo). \
                    filter(StockManagementInfo.on_job == '1').all()

    g = Graph(settings.NEO4J_URL, auth=(settings.NEO4J_USER, settings.NEO4J_PASSWD))

    for manager in managers:
        companyNode = neo4jhelper.graph_create_node(g, constants.NEO4J_LABEL_COMPANY, manager.company_name)

        managerNode = neo4jhelper.graph_create_node(g, constants.NEO4J_LABEL_PERSON, manager.name)
        neo4jhelper.graph_create_relation(g, companyNode, manager.title, managerNode)
        
    session.close()


def map_company_manager_info(code):
    '''导入公司董高监管理层人员信息到neo4j'''

    session = new_db_session()

    managers = session.query(StockManagementInfo). \
                    filter(StockManagementInfo.code.like(code+'%')). \
                    filter(StockManagementInfo.on_job == '1').all()

    g = Graph(settings.NEO4J_URL, auth=(settings.NEO4J_USER, settings.NEO4J_PASSWD))

    for manager in managers:
        companyNode = neo4jhelper.graph_create_node(g, constants.NEO4J_LABEL_COMPANY, manager.company_name)

        managerNode = neo4jhelper.graph_create_node(g, constants.NEO4J_LABEL_PERSON, manager.name)
        neo4jhelper.graph_create_relation(g, companyNode, manager.title, managerNode)
        
    session.close()

def map_all_companies_info():
    '''导入企业基本信息到neo4j'''

    session = new_db_session()
    g = Graph(settings.NEO4J_URL, auth=(settings.NEO4J_USER, settings.NEO4J_PASSWD))

    companies = session.query(StockCompanyInfo).all()
    for company in companies:
        fill_company_into_map(g, company)

    session.close()

def map_company_info(code):
    '''映射公司信息'''
    
    session = new_db_session()

    company = session.query(StockCompanyInfo).filter(StockCompanyInfo.a_code == code).first()
    if company is None:
        return

    g = Graph(settings.NEO4J_URL, auth=(settings.NEO4J_USER, settings.NEO4J_PASSWD))

    fill_company_into_map(g, company)
    
    session.close()

def fill_company_into_map(g, company):

    companyNode = neo4jhelper.graph_create_node(g, constants.NEO4J_LABEL_COMPANY, company.full_name)
    legal = neo4jhelper.graph_create_node(g, constants.NEO4J_LABEL_PERSON, company.legal_representative)
    neo4jhelper.graph_create_relation(g, companyNode, constants.NEO4J_RELTYPE_COMPANY_LEGAL, legal)

    secretary = neo4jhelper.graph_create_node(g, constants.NEO4J_LABEL_PERSON, company.secretary)
    neo4jhelper.graph_create_relation(g, companyNode, constants.NEO4J_RELTYPE_COMPANY_SECRETARY, secretary)

    district = neo4jhelper.graph_create_node(g, constants.NEO4J_LABEL_DISTRICT, company.province)
    neo4jhelper.graph_create_relation(g, companyNode, constants.NEO4J_RELTYPE_COMPANY_DISTRICT, district)

    industry = neo4jhelper.graph_create_node(g, constants.NEO4J_LABEL_INDUSTRY, company.industry_2)
    neo4jhelper.graph_create_relation(g, companyNode, constants.NEO4J_RELTYPE_COMPANY_INDUSTRY, industry)

    cpafirm = neo4jhelper.graph_create_node(g, constants.NEO4J_LABEL_COMPANY, company.cpafirm)
    neo4jhelper.graph_create_relation(g, companyNode, constants.NEO4J_RELTYPE_COMPANY_CPAFIRM, cpafirm)

    lawfirm = neo4jhelper.graph_create_node(g, constants.NEO4J_LABEL_COMPANY, company.lawfirm)
    neo4jhelper.graph_create_relation(g, companyNode, constants.NEO4J_RELTYPE_COMPANY_LAWFIRM, lawfirm)