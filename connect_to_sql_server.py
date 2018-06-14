import pyodbc
import pandas as pd
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=241989Q1014025;"
                      "Database=db1;"
                      "Trusted_Connection=yes;")


# cursor = cnxn.cursor()
# cursor.execute('SELECT * FROM Table_1')

df = pd.read_sql_query('select * from Table_1', cnxn)

print(df)