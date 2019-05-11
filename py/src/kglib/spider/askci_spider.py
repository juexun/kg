
import pandas as pd

class AskciSpider:

    def get_holdings(self, code):
        '''
        获取子公司信息
        '''

        url = 'http://s.askci.com/stock/summary/{}/holding/'.format(code)
        tbs = pd.read_html(url)
        if len(tbs) != 1: 
            print("没有参股控股公司信息")
            return

        holdings = tbs[0]

        columns = holdings.loc[0].values[0:]
        holdings.columns = columns
        holdings = holdings.iloc[1:, 1:]
        
        return holdings

    def get_executives(self, code):
        '''
        获取董高监信息
        '''

        url = 'http://s.askci.com/stock/executives/{}/'.format(code)
        tbs = pd.read_html(url)
        if len(tbs) < 3: 
            print("没有公司高管信息")
            return

        columns = tbs[0].loc[0].values[0:]
        tbs[0].columns = columns
        tbs[1].columns = columns
        tbs[2].columns = columns

        executives = pd.concat([tbs[1].iloc[1:, 1:], tbs[2].iloc[1:, 1:], tbs[0].iloc[1:, 1:]])

        return executives

    def get_stockholders(self, code):
        '''
        获取十大股东信息
        '''

        url = 'http://s.askci.com/stock/equity/{}/'.format(code)

        tbs = pd.read_html(url)
        if len(tbs) < 3: 
            print("没有股东信息")
            return

        columns = tbs[1].loc[0].values[0:]
        tbs[1].columns = columns
        tbs[2].columns = columns

        stockholders = pd.concat([tbs[1].iloc[1:, :], tbs[2].iloc[1:, :]])
        stockholders.drop_duplicates(['机构或基金名称'], inplace=True)
        
        return stockholders
