import csv
import requests
from bs4 import BeautifulSoup, SoupStrainer
import pandas as pd
import numpy as np


with open('namad.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    namads = []
    for row in reader:
        namads.append(row[0])

monthly_reports = []
sales = {}

for namad in namads:
    sales.update({namad: np.empty((12, 4), dtype=int)*np.nan})
    print(type(namad))
    url = ('https://www.codal.ir/ReportList.aspx?1=' +
           namad + "&3=341005&4=58&5=&6=&7=&8=-1&9=-1&10=0&11=&12=False&13=0&15=-1&16=-1&17=-1&18=")

    try:
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
                # سطرها? بالا، نام نماد، تار?خ? که گزارش مربوط به آن دوره است، و ل?نک گزارش را ذخ?ره م?‌کند.

    except:
        print('url error?  ', url)


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
    if '????' in row[1]:
        year = 1397
    if '????' in row[1]:
        year = 1396
    if '????' in row[1]:
        year = 1395

    if '/??/' in row[1]:
        mnth = 1
    if '/??/' in row[1]:
        mnth = 2
    if '/??/' in row[1]:
        mnth = 3
    if '/??/' in row[1]:
        mnth = 4
    if '/??/' in row[1]:
        mnth = 5
    if '/??/' in row[1]:
        mnth = 6
    if '/??/' in row[1]:
        mnth = 7
    if '/??/' in row[1]:
        mnth = 8
    if '/??/' in row[1]:
        mnth = 9
    if '/??/' in row[1]:
        mnth = 10
    if '/??/' in row[1]:
        mnth = 11
    if '/??/' in row[1]:
        mnth = 12
    sales[row[0]][mnth-1, year-1395] = row[2]

    if sales[row[0]][mnth-1, 1] != 0 and sales[row[0]][mnth-1, 2] != 0:
        sales[row[0]][mnth - 1, 3] = (sales[row[0]][mnth-1, 2] - sales[row[0]][mnth-1, 1])/sales[row[0]][mnth-1, 1]*100

np.set_printoptions(precision=0)

print('3 month sale 1396       3 month sale 1397       %increase       namad')
for namad in sales:
    print("{0:,}                 {1:,}          {2:,}       ".format(sales[namad][2, 1], sales[namad][2, 2], sales[namad][2, 3]), namad)

