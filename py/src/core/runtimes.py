# -*- coding: utf-8 -*-

from dynaconf import settings
from kglib.utils import init_db

from .block_info import map_industry_blocks
from .exchange_info import map_exchange
from .func_info import map_fund_info

def init_envs():
    '''
        环境初始化
    '''

    init_db(settings.MYSQL_USER, settings.MYSQL_PASSWD, settings.MYSQL_DB)
    map_industry_blocks()
    map_exchange()
    map_fund_info()

