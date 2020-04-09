import pyodbc

conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};Server=tcp:myservername.database.windows.net,1433;Database=mydatabase;Uid=myuser;Pwd=mypasword.;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")

cursor = conn.cursor()
cursor.execute('SELECT * FROM myExample.Products')

for row in cursor:
    print(row)