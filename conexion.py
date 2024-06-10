import pyodbc 
 
print(pyodbc.drivers())
try: 
    connection = pyodbc.connect('DRIVER={SQL Server};Server=localhost\\SQLEXPRESS;Database=gestor_admin_it;Trusted_Connection=True;')
    print("Connection established")
except Exception as ex:
    print(ex)
    