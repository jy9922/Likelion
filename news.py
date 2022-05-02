import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import pandas as pd

query = input("검색 키워드를 입력하세요 : ")
page_num = int(input('크롤링할 페이지를 입력해주세요. ex) 1 (숫자만입력) : '))

print('크롤링할 페이지:'+str(page_num)+'페이지')

news_url = 'https://search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q='+query+'&p='+str(page_num)
response = requests.get(news_url)
soup = BeautifulSoup(response.text, 'html.parser')
results = soup.findAll('a','tit_main fn_tit_u')

wb = Workbook()
ws1 = wb.active
ws1.title = "다음 뉴스 스크래핑"
ws1.append([" ","번호","제목"])

rows = []

number = 0
for result in results:
    number += 1
    title = result.get_text()
    row = [number, title]
    rows.append(row)
    ws1.append([number, title])

df = pd.DataFrame(rows, columns = ['번호', '기사제목'])
print(df)

    

wb.save(filename='export_sample.xlsx')