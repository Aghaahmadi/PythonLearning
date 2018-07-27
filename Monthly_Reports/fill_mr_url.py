import pypyodbc
import csv
import requests
from bs4 import BeautifulSoup, SoupStrainer

connection = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=DESKTOP-9SU28DA;"
                              "Database=Codal;"
                              "Trusted_Connection=Yes;")
cursor = connection.cursor()

with open('namad_all.csv', 'r', encoding='utf-8') as csvfile:
    namads = csv.reader(csvfile, delimiter=',')

namads = [['ولساپا']]
for namad in namads:
    search_url = 'http://codal.ir/ReportList.aspx?1=' + \
                 namad[0] + "&3=341005&4=58&5=&6=&7=&8=-1&9=-1&10=0&11=&12=False&13=0&15=-1&16=-1&17=-1&18="
    response = requests.get(search_url)
    for link in BeautifulSoup(response.content, "html.parser", parse_only=SoupStrainer('a', href=True)):
        li = link['href']
        if li[0:7] == "Reports" and 'گزارش' in link.get_text():
            comment = link.get_text()
            comment = comment.replace('\n', '')
            comment = comment.replace('\t', '')
            comment = comment.replace('\r', '')
            comment = comment.replace('r', '')
            if '۱۳۹۷' in comment:
                yr = 1397
            if '۱۳۹۶' in comment:
                yr = 1396
            if '۱۳۹۵' in comment:
                yr = 1395

            if '/۰۱/' in comment:
                mnth = '1'
            if '/۰۲/' in comment:
                mnth = '2'
            if '/۰۳/' in comment:
                mnth = '3'
            if '/۰۴/' in comment:
                mnth = '4'
            if '/۰۵/' in comment:
                mnth = '5'
            if '/۰۶/' in comment:
                mnth = '6'
            if '/۰۷/' in comment:
                mnth = '7'
            if '/۰۸/' in comment:
                mnth = '8'
            if '/۰۹/' in comment:
                mnth = '9'
            if '/۱۰/' in comment:
                mnth = '10'
            if '/۱۱/' in comment:
                mnth = '11'
            if '/۱۲/' in comment:
                mnth = '12'

            if yr == 1396:
                sqlcommand = "update monthly_report_url set year1396='http://www.codal.ir/"+li+"' where namad=N'"+namad[0]+"' and month_no="+mnth

            if yr == 1397:
                sqlcommand = "update monthly_report_url set year1397='http://www.codal.ir/"+li+"' where namad=N'"+namad[0]+"' and month_no="+mnth

            print(sqlcommand)
            cursor.execute(sqlcommand)
            connection.commit()
connection.close()
