import pyodbc 

try: 
    connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DEVM\\SQLEXPRESS;DATABASE=gestion_negocio;Trusted_Connection=yes;')
    print("Connection established")
except Exception as ex:
    print(ex)
    