from sqlalchemy import create_engine

def save_df_to_mysql(df, db_user, db_pwd, db_name, db_table, db_host='127.0.0.1'): 
    engine = create_engine(
        "mysql+pymysql://{user}:{pw}@{host}/{db}".format(user="root", pw="Jx421830", host=db_host, db="quant")
        )

    df.to_sql(con=engine, name=db_table, if_exists='append', index=False)