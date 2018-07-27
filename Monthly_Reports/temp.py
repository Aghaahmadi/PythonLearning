import pypyodbc
import pandas as pd

connection = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=DESKTOP-9SU28DA;"
                              "Database=Codal;"
                              "Trusted_Connection=Yes;")

cursor = connection.cursor()

sqlcommand = 'select * from monthly_report_url'
cursor.execute(sqlcommand)
results = cursor.fetchone()

while results:
    print(results)
    results = cursor.fetchone()

print(n)
connection.close()