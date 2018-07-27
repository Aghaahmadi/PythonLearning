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
    url1396 = results[2]
    if url1396 != NULL
        read_table = pd.read_html(url1396, encoding='UTF-8')
        try:
            monthly_sales = read_table[2].iloc[-1, -1]
            print(monthly_sales)
        except IndexError:
            print(results)
    print(results)
    results = cursor.fetchone()

connection.close()



