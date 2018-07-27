# functions for read monthly reports from codal


def init_monthly_report_url(namad):
    import pypyodbc

    connection = pypyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=DESKTOP-9SU28DA;"
                              "Database=Codal;"
                              "Trusted_Connection=Yes;")

    cursor = connection.cursor()

    for m in range(1, 13):
        sqlcommand = "INSERT INTO monthly_report_url (namad, month_no) VALUES (?, ?)"
        values = [namad, m]
        cursor.execute(sqlcommand, values)
        connection.commit()

        sqlcommand = "INSERT INTO monthly_sales (namad, month_no) VALUES (?, ?)"
        values = [namad, m]
        cursor.execute(sqlcommand, values)
        connection.commit()

    connection.close()

