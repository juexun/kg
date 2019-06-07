# -*- coding: utf-8 -*-

from dynaconf import settings
from py2neo.data import Node, Relationship
from py2neo import Graph, GraphError, NodeMatcher

from kglib.utils import new_db_session
from model import StockBlockInfo
from . import constants

def map_industry_blocks():
    '''映射行业板块'''

    g = Graph(settings.NEO4J_URL, auth=(settings.NEO4J_USER, settings.NEO4J_PASSWD))
    
    session = new_db_session()
    blocks = session.query(StockBlockInfo).filter(StockBlockInfo.parent_class == None).all()

    for block in blocks:
        matcher = NodeMatcher(g)
        industry = matcher.match(constants.NEO4J_LABEL_INDUSTRY, name=block.class_name).first()
        if industry:
            continue

        tx = g.begin()
        industry = Node(constants.NEO4J_LABEL_INDUSTRY, name=block.class_name)

        tx.create(industry)
        sub_blocks = session.query(StockBlockInfo).filter(StockBlockInfo.parent_class == block.class_id).all()
        for sub_block in sub_blocks:
            sub_industry = Node(constants.NEO4J_LABEL_INDUSTRY, name=sub_block.class_name)
            tx.create(sub_industry)
            tx.create(Relationship(industry, constants.NEO4J_RELTYPE_SUBINDUSTRY, sub_industry))
            
        tx.commit()
    session.close()