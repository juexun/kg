# -*- coding: utf-8 -*-

from dynaconf import settings

from py2neo.data import Node, Relationship
from py2neo import Graph, GraphError, NodeMatcher

from kglib.utils import new_db_session
from kglib.utils import neo4jhelper
from model import FundMainInfo

from . import constants

def map_fund_info():

    g = Graph(settings.NEO4J_URL, auth=(settings.NEO4J_USER, settings.NEO4J_PASSWD))

    session = new_db_session()
    funds = session.query(FundMainInfo).all()

    for fund in funds:
        
        fundNode = neo4jhelper.graph_create_node(g, constants.NEO4J_LABEL_FUND, fund.name)
        
        advisor = neo4jhelper.graph_create_node(g, constants.NEO4J_LABEL_COMPANY, fund.advisor)
        neo4jhelper.graph_create_relation(g, fundNode, constants.NEO4J_RELTYPE_FUND_ADVISOR, advisor)

        trustee = neo4jhelper.graph_create_node(g, constants.NEO4J_LABEL_COMPANY, fund.trustee)
        neo4jhelper.graph_create_relation(g, fundNode, constants.NEO4J_RELTYPE_FUND_TRUSTEE, trustee)


