import pyodbc

conn = pyodbc.connect("Driver={ODBC Driver 13 for SQL Server};Server=tcp:unahvjamaya.database.windows.net,1433;Database=ingreso_vehiculos;Uid=vjamaya;Pwd=Admin203Amaya.;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;")

cursor = conn.cursor()
cursor.execute('SELECT * FROM myExample.Products')

for row in cursor:
    print(row)
