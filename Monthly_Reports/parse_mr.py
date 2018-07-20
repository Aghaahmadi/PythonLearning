import csv
import requests
from bs4 import BeautifulSoup, SoupStrainer
import pandas as pd
import numpy as np

with open('namad.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    namads = []
    for row in reader:
        namads.append(row[0])

monthly_reports = []
sales = {}

for namad in namads:
    sales.update({namad: np.empty((12, 4), dtype=int)*np.nan})
    print(namad)
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
            # سطرهای بالا، نام نماد، تاریخی که گزارش مربوط به آن دوره است، و لینک گزارش را ذخیره می‌کند.

print('-------------------------------------------------------------')
monthly_sales = []
for row in monthly_reports:
    url = 'http://www.codal.ir/' + row[2]
    read_table = pd.read_html(url, encoding='UTF-8')
    try:
        monthly_sales.append([row[0], row[1], read_table[2].iloc[-1, -1]])
    except IndexError:
        print(row[0])

for row in monthly_sales:
    if '۱۳۹۷' in row[1]:
        year = 1397
    if '۱۳۹۶' in row[1]:
        year = 1396
    if '۱۳۹۵' in row[1]:
        year = 1395

    if '/۰۱/' in row[1]:
        mnth = 1
    if '/۰۲/' in row[1]:
        mnth = 2
    if '/۰۳/' in row[1]:
        mnth = 3
    if '/۰۴/' in row[1]:
        mnth = 4
    if '/۰۵/' in row[1]:
        mnth = 5
    if '/۰۶/' in row[1]:
        mnth = 6
    if '/۰۷/' in row[1]:
        mnth = 7
    if '/۰۸/' in row[1]:
        mnth = 8
    if '/۰۹/' in row[1]:
        mnth = 9
    if '/۱۰/' in row[1]:
        mnth = 10
    if '/۱۱/' in row[1]:
        mnth = 11
    if '/۱۲/' in row[1]:
        mnth = 12
    sales[row[0]][mnth-1, year-1395] = row[2]

    if sales[row[0]][mnth-1, 1] != 0 and sales[row[0]][mnth-1, 2] != 0:
        sales[row[0]][mnth - 1, 3] = (sales[row[0]][mnth-1, 2] - sales[row[0]][mnth-1, 1])/sales[row[0]][mnth-1, 1]*100

print(sales)
