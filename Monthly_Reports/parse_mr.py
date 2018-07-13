import csv
import requests
from bs4 import BeautifulSoup, SoupStrainer
import pandas as pd

with open('namad.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    namads = []
    for row in reader:
        namads.append(row[0])

monthly_reports = []

for namad in namads:
    # ساخت آدرس صفحه جستجوی گزارش ماهانه بر اساس نماد
    url = 'http://codal.ir/ReportList.aspx?1=' + \
          namad + "&3=341005&4=58&5=&6=&7=&8=-1&9=-1&10=0&11=&12=False&13=0&15=-1&16=-1&17=-1&18="
    response = requests.get(url)
    for link in BeautifulSoup(response.content, "html.parser", parse_only=SoupStrainer('a', href=True)):
        li = link['href']
        if li[0:7] == "Reports" and 'گزارش' in link.get_text():
            comment = link.get_text()
            comment = comment.replace('\n', '')
            comment = comment.replace('\t', '')
            comment = comment.replace('\r', '')
            comment = comment.replace('r', '')
            monthly_reports.append([namad, comment, li])
monthly_sales = []
for row in monthly_reports:
    url = 'http://www.codal.ir/' + row[2]
    read_table = pd.read_html(url, encoding='UTF-8')
    monthly_sales.append([row[0], row[1], read_table[2].iloc[-1, -1]])

print(monthly_sales)
