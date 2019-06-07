# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

def init_db(db_user, db_pwd, db_name, db_host='127.0.0.1', db_port=3306):

    global mysql_engine
    global mysql_session

    mysql_engine = create_engine(
        "mysql+pymysql://{user}:{pw}@{host}:{port}/{db}?charset=utf8".format(user=db_user, pw=db_pwd, 
        host=db_host, port=db_port, db=db_name)
    )
    session_factory = sessionmaker(bind=mysql_engine)
    mysql_session = scoped_session(session_factory)
    
def new_db_session():
    return mysql_session()

def save_df_to_mysql(df, db_table): 
    df.to_sql(con=mysql_engine, name=db_table, if_exists='append', index=False)