# -*- coding: utf-8 -*-

from dynaconf import settings

from py2neo.data import Node, Relationship
from py2neo import Graph, GraphError, NodeMatcher

from kglib.utils import new_db_session, dbhelper
from kglib.utils import neo4jhelper
from kglib.spider import TushareSpider, JoinQuantSpider, SinaSpider

from model import FundMainInfo

from . import constants

def map_fund_info():
    '''MySQL导入neo4j'''

    g = Graph(settings.NEO4J_URL, auth=(settings.NEO4J_USER, settings.NEO4J_PASSWD))

    session = new_db_session()
    funds = session.query(FundMainInfo).all()

    for fund in funds:
        
        fundNode = neo4jhelper.graph_create_node(g, constants.NEO4J_LABEL_FUND, fund.fullname)
        
        advisor = neo4jhelper.graph_create_node(g, constants.NEO4J_LABEL_COMPANY, fund.advisor)
        neo4jhelper.graph_create_relation(g, fundNode, constants.NEO4J_RELTYPE_FUND_ADVISOR, advisor)

        trustee = neo4jhelper.graph_create_node(g, constants.NEO4J_LABEL_COMPANY, fund.trustee)
        neo4jhelper.graph_create_relation(g, fundNode, constants.NEO4J_RELTYPE_FUND_TRUSTEE, trustee)

        if fund.manager:
            manager = neo4jhelper.graph_create_node(g, constants.NEO4J_LABEL_PERSON, fund.manager)
            neo4jhelper.graph_create_relation(g, fundNode, constants.NEO4J_RELTYPE_FUND_MANAGER, manager)

def sync_fund_info():
    '''同步基金信息'''

    jq = JoinQuantSpider(settings.JOINQUANT_USER, settings.JOINQUANT_PASSWD)
    df = jq.fetch_fund_info()
    if df is None or df.empty:
        return

    df['fullname'] = ''
    df['manager'] = ''
    cols = list(df)
    cols.insert(2, cols.pop(cols.index('fullname')))
    cols.insert(5, cols.pop(cols.index('manager')))
    df = df.loc[:, cols]

    spider = SinaSpider()
    for idx, row in df.iterrows():
        
        fund = spider.get_fund_info(row['main_code'])

        if fund is None:
            print(row['main_code']+" 404 >>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            continue
        df.loc[idx, 'name'] = fund[SinaSpider.FUND_SHORTNAME]
        df.loc[idx, 'fullname'] = fund[SinaSpider.FUND_FULLNAME]
        df.loc[idx, 'manager'] = fund[SinaSpider.FUND_MANAGER]

#     print(df)
    dbhelper.save_df_to_mysql(df, constants.DB_TABLE_FUND_MAIN_INFO)
