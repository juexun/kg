# coding: utf-8
from sqlalchemy import Column, DECIMAL, Date, Float, String, Text, text
from sqlalchemy.dialects.mysql import BIGINT, CHAR, INTEGER, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class FundMainInfo(Base):
    __tablename__ = 'fund_main_info'

    main_code = Column(VARCHAR(12), primary_key=True)
    name = Column(VARCHAR(100))
    fullname = Column(VARCHAR(100))
    advisor = Column(VARCHAR(100))
    trustee = Column(VARCHAR(100))
    manager = Column(VARCHAR(32))
    operate_mode_id = Column(INTEGER(20))
    operate_mode = Column(VARCHAR(32))
    underlying_asset_type_id = Column(INTEGER(20))
    underlying_asset_type = Column(VARCHAR(32))
    start_date = Column(Date)
    end_date = Column(Date)


class StockBlockInfo(Base):
    __tablename__ = 'stock_block_info'

    class_id = Column(INTEGER(10), primary_key=True)
    class_name = Column(VARCHAR(255), nullable=False)
    parent_class = Column(String(255))
    classfied_by = Column(VARCHAR(255), nullable=False, server_default=text("'csrc'"))


class StockCompanyInfo(Base):
    __tablename__ = 'stock_company_info'

    code = Column(CHAR(20), primary_key=True)
    full_name = Column(Text)
    short_name = Column(Text)
    a_code = Column(CHAR(20))
    b_code = Column(CHAR(20))
    h_code = Column(CHAR(20))
    fullname_en = Column(Text)
    shortname_en = Column(Text)
    legal_representative = Column(Text)
    register_location = Column(Text)
    office_address = Column(Text)
    zipcode = Column(Text)
    register_capital = Column(Float(asdecimal=True))
    currency_id = Column(Float(asdecimal=True))
    currency = Column(Text)
    establish_date = Column(Date)
    website = Column(Text)
    email = Column(Text)
    contact_number = Column(Text)
    fax_number = Column(Text)
    main_business = Column(Text)
    business_scope = Column(Text)
    description = Column(Text)
    tax_number = Column(Text)
    license_number = Column(Text)
    pub_newspaper = Column(Text)
    pub_website = Column(Text)
    secretary = Column(Text)
    secretary_number = Column(Text)
    secretary_fax = Column(Text)
    secretary_email = Column(Text)
    security_representative = Column(Text)
    province_id = Column(Text)
    province = Column(Text)
    city_id = Column(Text)
    city = Column(Text)
    industry_id = Column(Text)
    industry_1 = Column(Text)
    industry_2 = Column(Text)
    cpafirm = Column(Text)
    lawfirm = Column(Text)
    ceo = Column(Text)
    comments = Column(Text)


class StockDaily(Base):
    __tablename__ = 'stock_daily'

    date = Column(Date, primary_key=True, nullable=False)
    code = Column(VARCHAR(255), primary_key=True, nullable=False)
    name = Column(VARCHAR(255))
    open = Column(Float)
    close = Column(Float)
    high = Column(Float)
    low = Column(Float)
    volume = Column(Float(asdecimal=True))
    money = Column(Float(asdecimal=True))


class StockEmployeeInfo(Base):
    __tablename__ = 'stock_employee_info'

    code = Column(CHAR(20), primary_key=True, nullable=False)
    name = Column(CHAR(255), primary_key=True, nullable=False)
    end_date = Column(Date, primary_key=True, nullable=False)
    pub_date = Column(Date)
    employee = Column(Float(asdecimal=True))
    retirement = Column(Text)
    graduate_rate = Column(Float(asdecimal=True))
    college_rate = Column(Float(asdecimal=True))
    middle_rate = Column(Float(asdecimal=True))


class StockManagementInfo(Base):
    __tablename__ = 'stock_management_info'

    code = Column(CHAR(20), primary_key=True, nullable=False)
    company_name = Column(VARCHAR(255), primary_key=True, nullable=False)
    pub_date = Column(Date, primary_key=True, nullable=False)
    person_id = Column(BIGINT(20), nullable=False)
    name = Column(VARCHAR(255), primary_key=True, nullable=False)
    title_class_id = Column(BIGINT(20), primary_key=True, nullable=False)
    title_class = Column(VARCHAR(20), nullable=False)
    title = Column(VARCHAR(40), primary_key=True, nullable=False)
    start_date = Column(Date, primary_key=True, nullable=False)
    leave_date = Column(Date)
    leave_reason = Column(Text)
    on_job = Column(Text)
    gender = Column(Text)
    birth_year = Column(Text)
    highest_degree_id = Column(Float(asdecimal=True))
    highest_degree = Column(Text)
    title_level_id = Column(Float(asdecimal=True))
    title_level = Column(Text)
    profession_certificate_id = Column(Text)
    profession_certificate = Column(Text)
    nationality_id = Column(Float(asdecimal=True))
    nationality = Column(Text)
    security_career_start_year = Column(Text)
    resume = Column(Text)


class StockPledge(Base):
    __tablename__ = 'stock_pledge'

    date = Column(Date, primary_key=True, nullable=False)
    code = Column(VARCHAR(255), primary_key=True, nullable=False)
    name = Column(VARCHAR(255), nullable=False)
    total_tr = Column(INTEGER(20))
    count_ults = Column(Float(20))
    count_lts = Column(Float(20))
    total_shares = Column(Float(20))
    pledge_rate = Column(Float(20))


class StockShareholderFloatingTop10(Base):
    __tablename__ = 'stock_shareholder_floating_top10'

    code = Column(VARCHAR(12), primary_key=True, nullable=False)
    company_name = Column(VARCHAR(100), primary_key=True, nullable=False)
    end_date = Column(Date, primary_key=True, nullable=False)
    pub_date = Column(Date)
    change_reason_id = Column(BIGINT(20))
    change_reason = Column(VARCHAR(120))
    shareholder_rank = Column(BIGINT(20))
    shareholder_id = Column(Float(asdecimal=True))
    shareholder_name = Column(VARCHAR(200), primary_key=True, nullable=False)
    shareholder_name_en = Column(VARCHAR(150))
    shareholder_class_id = Column(BIGINT(20))
    shareholder_class = Column(VARCHAR(150))
    share_number = Column(Float(asdecimal=True))
    share_ratio = Column(DECIMAL(10, 4))
    sharesnature_id = Column(BIGINT(20))
    sharesnature = Column(VARCHAR(120))


class StockShareholderTop10(Base):
    __tablename__ = 'stock_shareholder_top10'

    code = Column(VARCHAR(12), primary_key=True, nullable=False)
    company_name = Column(VARCHAR(100), primary_key=True, nullable=False)
    end_date = Column(Date, primary_key=True, nullable=False)
    pub_date = Column(Date)
    change_reason_id = Column(Float(asdecimal=True))
    change_reason = Column(VARCHAR(120))
    shareholder_rank = Column(BIGINT(20))
    shareholder_name = Column(VARCHAR(200), primary_key=True, nullable=False)
    shareholder_name_en = Column(VARCHAR(200))
    shareholder_id = Column(INTEGER(11))
    shareholder_class_id = Column(INTEGER(11))
    shareholder_class = Column(VARCHAR(150))
    share_number = Column(BIGINT(20))
    share_ratio = Column(DECIMAL(10, 4))
    sharesnature_id = Column(INTEGER(11))
    sharesnature = Column(VARCHAR(120))
    share_pledge_freeze = Column(DECIMAL(10, 4))
    share_pledge = Column(DECIMAL(10, 4))
    share_freeze = Column(DECIMAL(10, 4))
