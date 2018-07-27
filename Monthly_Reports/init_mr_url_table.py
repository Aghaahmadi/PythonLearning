# initialize monthly report table for all namads
import csv
from mr_fn import init_monthly_report_url
import pypyodbc

connection = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=DESKTOP-9SU28DA;"
                              "Database=Codal;"
                              "Trusted_Connection=Yes;")

cursor = connection.cursor()
sqlcommand = "truncate table monthly_report_url"
cursor.execute(sqlcommand)
connection.commit()
connection.close()

with open('namad_all.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    for namad in reader:
        init_monthly_report_url(namad[0])
        print(namad[0])


