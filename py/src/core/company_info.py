# -*- coding: utf-8 -*-

from dynaconf import settings
from py2neo.data import Node, Relationship
from py2neo import Graph, GraphError
from model import Company, Person
from kglib.spider import AskciSpider

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