
from py2neo.ogm import GraphObject, Property, RelatedTo, RelatedFrom 

from .person import Person
from .exchange import StockExchange

class Company(GraphObject):

    __primarykey__ = "name"

    name = Property()
    # code = Property()

    subsidiary = RelatedTo("Company", "子公司")
    subsubsidiary = RelatedTo("Company", "孙公司")
    othersubsidiary = RelatedTo("Company", "参股")
    joint_ventures = RelatedTo("Company", "合营企业")

    stockholders = RelatedFrom("Company", "持股")
    exectives = RelatedFrom("Person", "高管")

    def add_ties(self, sub, rel):
        if rel == "子公司":
            self.add_subsidiary(sub)
        elif rel == "孙公司":
            self.add_sub_subsidiary(sub)
        elif rel == "其他":
            self.add_othersubsidiary(sub)
        elif rel == "合营企业":
            self.add_joint_ventures(sub)

    def add_subsidiary(self, sub):
        self.subsidiary.add(sub)

    def add_sub_subsidiary(self, sub_subsidiary):
        self.subsubsidiary.add(sub_subsidiary)

    def add_othersubsidiary(self, other_subsidiary):
        self.othersubsidiary.add(other_subsidiary)

    def add_joint_ventures(self, joint):
        self.joint_ventures.add(joint)

    def add_stockholders(self, holder):
        self.stockholders.add(holder)

    def add_exectives(self, p):
        '''
        增加高管信息
        '''
        
        self.exectives.add(p)

class ListedCompany(Company):
    '''
    上市公司
    '''

    markets = RelatedTo("StockExchange", "上市")

    def add_markets(self, market, code):
        se = StockExchange(market)
        props = {"code": code}
        self.markets.add(se, props)

class UnlistedCompany(Company):
    '''
    非上市公司
    '''