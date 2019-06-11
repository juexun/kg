from bs4 import BeautifulSoup
import requests

fundUrl = "http://stock.finance.sina.com.cn/fundInfo/view/FundInfo_JJGK.php?symbol=000001"
htmlext = requests.get(fundUrl).text
bs = BeautifulSoup(htmlext, "html5lib")

for _, tb in enumerate(bs.find_all('table')):

    if tb.thead is None:
        continue

    trows = tb.thead.find_all('tr')
    if len(trows) == 0:
        continue

    if len(trows[0].th) is None or trows[0].th.h3 is None:
        continue

    if trows[0].th.h3.string != "基金概况":
        continue
        
    if tb.tbody is None:
        continue

    fund = {}
    for _, trow in enumerate(tb.tbody.find_all('tr')):
        tds = trow.find_all('td')
        for i in range(0, len(tds), 2):
            fund[tds[i].span.string] = tds[i+1].span.string

        # for _, td in enumerate(trow.find_all('td')):
        #     print(td.span.string)

    

