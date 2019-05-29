# -*- coding: utf-8 -*-


from core import fetch_company_info, extract_resume_info, fetch_stock_list, sync_listed_company_info

if __name__ == '__main__':

    resume = '''
    姚波先生,非执行董事候选人。1971年出生,北美精算师协会会员(FSA),并获得美国纽约大学工商管理硕士学位。自2009年6月起出任中国平安执行董事,自2010年4月和2009年6月起分别出任中国平安首席财务官和副总经理,于2012年10月起出任中国平安总精算师,于2016年1月起出任中国平安常务副总经理。2010年6月至今,任平安银行(原深圳发展银行)董事。姚波先生于2001年5月加入中国平安,2009年6月至2016年1月任中国平安副总经理,2008年3月至2010年4月任中国平安财务负责人,2007年1月至2010年6月任中国平安总精算师,2004年2月至2007年1月任中国平安财务副总监,2004年2月至2012年2月期间兼任中国平安企划部总经理,2002年12月至2007年1月任中国平安副总精算师,2001年至2002年曾任中国平安产品中心副总经理。自2016年5月30日起担任平安健康医疗科技有限公司非执行董事。
    '''

    # extract_resume_info(resume)

    # ts = fetch_stock_list()
    sync_listed_company_info()


    # fetch_company_info("中国平安保险(集团)股份有限公司", "601318")
    # fetch_company_info("平安银行股份有限公司", "000001")
    # fetch_company_info("招商银行股份有限公司", "600036")
    # fetch_company_info("上海浦东发展银行股份有限公司", "600000")
    # fetch_company_info("美的集团股份有限公司", "000333")
    # fetch_company_info("珠海格力电器股份有限公司", "000651")
    # fetch_company_info("万科企业股份有限公司", "000002")
    # fetch_company_info("安徽海螺水泥股份有限公司", "600585")
    # fetch_company_info("万华化学集团股份有限公司", "600309")
    # fetch_company_info("中国联合网络通信股份有限公司", "600050")
    # fetch_company_info("贵州茅台酒股份有限公司", "600519")
    # fetch_company_info("福耀玻璃工业集团股份有限公司", "600660")
    # fetch_company_info("江苏恒瑞医药股份有限公司", "600276")
    # fetch_company_info("杭州海康威视数字技术股份有限公司", "002415")
    # fetch_company_info("浙江大华技术股份有限公司", "002236")
    # fetch_company_info("佛山市海天调味食品股份有限公司", "603288")
    # fetch_company_info("北京顺鑫农业股份有限公司", "000860")
    # fetch_company_info("宜宾五粮液股份有限公司", "000858")
    # fetch_company_info("青岛海尔股份有限公司", "600690")
    # fetch_company_info("广州视源电子科技股份有限公司", "002841")
